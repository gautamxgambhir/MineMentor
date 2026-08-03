<div align="center">
  <img src="https://i.ibb.co/zWgvrRm3/minementor.png" alt="MineMentor Logo"><br>
</div>

-----------------

# MineMentor: AI-Powered Minecraft Assistant Bot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-red)
![Minecraft](https://img.shields.io/badge/Minecraft-Bot-orange)

## What is MineMentor?

MineMentor is an **AI-powered assistant bot** for **Minecraft servers** that provides instant answers to players' in-game questions. Whether you need crafting recipes, gameplay tips, or strategies, MineMentor is always ready to help!

## Features

- **Bring Your Own API Key**: Works with any OpenAI-compatible AI provider — OpenAI, Groq, Together AI, Mistral, OpenRouter, and more.
- **Fully Configurable**: Set your provider, model, and API key via a simple `.env` file.
- **Continuous Movement**: Automatically moves in a square pattern to **avoid AFK kicks** (can be toggled).
- **Quick Command Responses**: Uses the `?` prefix for quick in-game queries.
- **Auto-Reconnect**: If disconnected, MineMentor will attempt to **reconnect automatically**.
- **Error Handling**: Gracefully handles AI errors and notifies the player in chat.

## How It Works

1. The bot listens for messages in the chat.
2. When a player asks a question using the `?` prefix, MineMentor processes it.
3. It sends the query to your configured AI provider and receives a response.
4. The bot replies **directly in the chat**, ensuring a seamless experience.
5. Meanwhile, it **keeps moving** to prevent being kicked from the server.

## Supported AI Providers

MineMentor uses the **OpenAI-compatible API standard**, which is supported by most modern AI providers:

| Provider | Base URL | Example Models |
|---|---|---|
| **OpenAI** | `https://api.openai.com/v1` | `gpt-4o-mini`, `gpt-4o` |
| **Groq** | `https://api.groq.com/openai/v1` | `llama-3.1-8b-instant`, `mixtral-8x7b-32768` |
| **Together AI** | `https://api.together.xyz/v1` | `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` |
| **Mistral** | `https://api.mistral.ai/v1` | `mistral-small-latest` |
| **OpenRouter** | `https://openrouter.ai/api/v1` | `openai/gpt-4o-mini`, `google/gemini-flash-1.5` |

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/gautamxgambhir/MineMentor.git
cd MineMentor
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Node.js dependencies
```bash
npm install
```

### 4. Configure your `.env` file

Copy the example below into a `.env` file in the project root and fill in your details:

```env
# Your AI provider API key
API_KEY=your_api_key_here

# Base URL of the provider's OpenAI-compatible API endpoint
API_BASE_URL=https://api.openai.com/v1

# The model to use (must be available on your chosen provider)
MODEL=gpt-4o-mini
```

> **Groq example** (free tier available at [console.groq.com](https://console.groq.com)):
> ```env
> API_KEY=your_groq_api_key
> API_BASE_URL=https://api.groq.com/openai/v1
> MODEL=llama-3.1-8b-instant
> ```

### 5. Configure server connection

Open `bot.py` and update these two lines to match your Minecraft server:
```python
server_host = "your.server.ip"
server_port = your_server_port
```

### 6. Run the bot
```bash
python bot.py
```

## Usage

### In-Game Commands

Use the **`?` prefix** followed by your question:

- `?How do I craft a diamond sword?` → The bot replies with the recipe.
- `?Where do I find Netherite?` → The bot provides an answer.
- `?What does Silk Touch do?` → Instant explanation in chat.

## Dependencies

- [**Mineflayer**](https://github.com/PrismarineJS/mineflayer) — Minecraft bot framework.
- [**openai**](https://pypi.org/project/openai/) — OpenAI-compatible Python client (works with any provider).
- [**javascript**](https://pypi.org/project/javascript/) — Runs Node.js from Python.
- [**simple-chalk**](https://pypi.org/project/simple-chalk/) — Colored terminal output.
- [**python-dotenv**](https://pypi.org/project/python-dotenv/) — Loads `.env` configuration.

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
