# OpenAI Chatbot with Gradio

A simple chatbot powered by OpenAI's GPT-3.5-turbo model with a Gradio web interface.

## Features

- 💬 Real-time chat with OpenAI's GPT-3.5-turbo
- 📝 Maintains conversation history for context-aware responses
- 🎨 Clean and user-friendly Gradio interface
- 🔄 Reset conversation history anytime
- 🛡️ Error handling for API issues

## Requirements

- Python 3.8+
- OpenAI API key

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   
   Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

Run the chatbot:
```bash
python chatbot.py
```

The Gradio interface will start at `http://127.0.0.1:7860`

## How It Works

1. Type your message in the text box
2. Click "Send" or press Enter
3. The chatbot responds using OpenAI's API
4. Conversation history is maintained for context
5. Click "Reset Chat" to start a new conversation

## Configuration

You can customize the chatbot by modifying `chatbot.py`:

- **Model**: Change `"gpt-3.5-turbo"` to `"gpt-4"` or another model
- **Temperature**: Adjust `temperature=0.7` (0-1, higher = more creative)
- **Max tokens**: Change `max_tokens=500` to control response length
- **Server port**: Modify `server_port=7860` in the launch settings

## Troubleshooting

- **"Invalid API key" error**: Check your `.env` file and ensure your OpenAI API key is correct
- **"Rate limit exceeded"**: Wait a moment and try again. Your free trial may have usage limits
- **Gradio not starting**: Ensure port 7860 is available on your machine

## License

MIT
