<div align="center">
  <img src="https://i.ibb.co/zWgvrRm3/minementor.png" alt="MineMentor Logo"><br>
</div>

-----------------

# MineMentor: AI-Powered Minecraft Assistant Bot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-red)
![Together-AI](https://img.shields.io/badge/Together%20AI-0f6fff)
![Minecraft](https://img.shields.io/badge/Minecraft-Bot-orange)

## What is MineMentor?

MineMentor is an **AI-powered assistant bot** for **Minecraft servers** that provides instant answers to players' in-game questions. Whether you need crafting recipes, gameplay tips, or strategies, MineMentor is always ready to help!

## Features

- **AI-Powered Responses**: Uses **Together AI** to generate real-time responses to Minecraft-related queries.
- **Continuous Movement**: Automatically moves in a square pattern to **avoid AFK kicks**.
- **Quick Command Responses**: Uses the `?` prefix for quick in-game queries.
- **Auto-Reconnect**: If disconnected, MineMentor will attempt to **reconnect automatically**.
- **Customizable Bot Name**: You can change the bot’s display name when launching.

## How It Works

- The bot listens for messages in the chat.
- When a player asks a question using the `?` prefix, MineMentor processes it.
- It sends the query to Together AI for an accurate response.
- The bot replies **directly in the chat**, ensuring a seamless experience.
- Meanwhile, it **keeps moving** to prevent being kicked from the server.

## Where to Get It?

MineMentor is open-source and available on GitHub:

🔗 **[GitHub Repository](https://github.com/gautamxgambhir/MineMentor)**

## Installation and Setup

### 1. Clone the repository:
```bash
 git clone https://github.com/gautamxgambhir/MineMentor.git
```

### 2. Install dependencies:
```bash
cd MineMentor
pip install -r requirements.txt
```

### 3. Install Node.js dependencies:
```bash
npm install
```

### 4. Set up API keys
- Obtain a **Together AI API Key** from [Together AI](https://www.together.ai/).
- Store the API key in an **.env** file:
```env
API_KEY=your_together_api_key
```

### 5. Configure Server Connection
- Open `bot.py` and modify the following variables to match your server:
```python
server_host = "your.server.ip"
server_port = your_server_port
```

### 6. Run the bot:
```bash
python bot.py
```

## Usage

### In-Game Commands
- Use the **`?` prefix** followed by your question.
- Example:
  - `?How do I craft a diamond sword?` → The bot will reply with the recipe.
  - `?Where do I find Netherite?` → The bot will provide an answer.
- The bot **continuously moves** to avoid being kicked for inactivity.

## Dependencies

- [**Mineflayer**](https://github.com/PrismarineJS/mineflayer) - Minecraft bot framework.
- [**Together API**](https://www.together.ai/) - AI-powered question-answering system.
- [**Flask**](https://flask.palletsprojects.com/en/3.0.x/) - API backend.
- [**Minecraft Protocol**](https://github.com/PrismarineJS/node-minecraft-protocol) - Handles Minecraft server interactions.

## Contributing

Contributions are welcome! To contribute:
- Fork the repo.
- Create a new branch (`git checkout -b feature-branch`).
- Commit changes (`git commit -m "Added new feature"`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.

## License

This project is licensed under the **MIT License**.

## Contact

- **GitHub**: [@gautamxgambhir](https://github.com/gautamxgambhir)
- **Email**: ggambhir1919@gmail.com
- **Instagram**: [gautamxgambhir](https://www.instagram.com/gautamxgambhir)
- **Twitter**: [gautamxgambhir](https://www.twitter.com/gautamxgambhir)
