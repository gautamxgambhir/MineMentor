from javascript import require, On, off
from simple_chalk import chalk
from openai import OpenAI
import random
import time
from threading import Thread
from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()

# --- AI Provider Configuration ---
# These are read from your .env file.
# Works with any OpenAI-compatible provider (OpenAI, Groq, Together AI, Mistral, etc.)
API_KEY: Final[str] = os.getenv("API_KEY")
API_BASE_URL: Final[str] = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL: Final[str] = os.getenv("MODEL", "gpt-4o-mini")

if not API_KEY:
    raise ValueError("API_KEY is not set in your .env file. Please add it before running the bot.")

client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)

mineflayer = require("mineflayer")

server_host = "localhost"
server_port = 50334
reconnect = True
prefix = "?"  # Set your prefix


class MCBot:
    def __init__(self, bot_name):
        self.bot_args = {
            "host": server_host,
            "port": server_port,
            "username": bot_name,
            "hideErrors": False,
            "verbose": True,
        }
        self.reconnect = reconnect
        self.bot_name = bot_name
        self.start_bot()

    def log(self, message):
        print(f"[{self.bot.username}] {message}")

    def start_bot(self):
        self.bot = mineflayer.createBot(self.bot_args)
        self.start_events()
        self.start_square_movement()  # Start square movement in a separate thread

    def start_events(self):
        @On(self.bot, "login")
        def login(this):
            self.bot_socket = self.bot._client.socket
            self.log(
                chalk.green(
                    f"Logged in to {self.bot_socket.server if self.bot_socket.server else self.bot_socket._host}"
                )
            )

        @On(self.bot, "spawn")
        def spawn(this):
            self.bot.chat("MineMentor is here to help!")

        @On(self.bot, "kicked")
        def kicked(this, reason, loggedIn):
            if loggedIn:
                self.log(chalk.redBright(f"Kicked whilst trying to connect: {reason}"))

        @On(self.bot, "messagestr")
        def messagestr(this, message, messagePosition, jsonMsg, sender, verified=None):
            if messagePosition == "chat":
                self.log(f"Received message: {message}")
                if f"{prefix}" in message:
                    query = message.split(prefix, 1)[1].strip()
                    if query:
                        try:
                            system_instruction = {
                                "role": "system",
                                "content": (
                                    "You are a Minecraft bot named MineMentor. Players will ask you queries, "
                                    "and you must respond concisely in a single line. "
                                    "Ensure your answers are correct and achievable in Minecraft."
                                ),
                            }
                            completion = client.chat.completions.create(
                                model=MODEL,
                                messages=[
                                    system_instruction,
                                    {"role": "user", "content": query},
                                ],
                                temperature=0.7,
                                top_p=1.0,
                            )
                            generated_response = completion.choices[0].message.content
                            self.log(f"Sent response: {generated_response}")
                            self.bot.chat(f"{generated_response}")
                        except Exception as e:
                            self.log(chalk.red(f"AI error: {e}"))
                            self.bot.chat("Sorry, I couldn't process that right now.")

        @On(self.bot, "end")
        def end(this, reason):
            self.log(chalk.red(f"Disconnected: {reason}"))
            off(self.bot, "login", login)
            off(self.bot, "spawn", spawn)
            off(self.bot, "kicked", kicked)
            off(self.bot, "messagestr", messagestr)

            if self.reconnect:
                self.log(chalk.cyanBright(f"Attempting to reconnect"))
                self.start_bot()

            off(self.bot, "end", end)

    def start_square_movement(self):
        def movement_loop():
            directions = ["forward", "right", "back", "left"]
            while True:
                try:
                    for direction in directions:
                        # Move in the current direction for ~2 blocks
                        self.bot.setControlState(direction, True)
                        time.sleep(1)
                        self.bot.clearControlStates()

                        # Jump at each corner
                        self.bot.setControlState("jump", True)
                        time.sleep(0.5)
                        self.bot.clearControlStates()

                        # Wait before next movement
                        time.sleep(random.uniform(2, 5))

                except Exception as e:
                    self.log(chalk.red(f"Error in movement loop: {e}"))
                    break

        # Uncomment the line below to enable AFK movement
        # Thread(target=movement_loop, daemon=True).start()


bot = MCBot("MineMentor")
