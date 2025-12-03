import os
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, RateLimitError
import gradio as gr

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize conversation history
conversation_history = []

def chat(user_message):
    """
    Send a message to OpenAI and get a response.
    Maintains conversation history for context.
    """
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract assistant response
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    except AuthenticationError:
        return "Error: Invalid API key. Please check your OPENAI_API_KEY in the .env file."
    except RateLimitError:
        return "Error: Rate limit exceeded. Please try again later."
    except Exception as e:
        return f"Error: {str(e)}"

def reset_conversation():
    """Reset the conversation history."""
    global conversation_history
    conversation_history = []
    return "Conversation reset. Start a new chat!"

# Create Gradio interface
with gr.Blocks(title="OpenAI Chatbot") as demo:
    gr.Markdown("# 🤖 OpenAI Chatbot")
    gr.Markdown("Chat with OpenAI's GPT-3.5-turbo model. The chatbot maintains conversation context.")
    
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(label="Chat History", height=400, type="messages")
            msg = gr.Textbox(
                label="Message",
                placeholder="Type your message here...",
                lines=1
            )
        
        with gr.Column(scale=1):
            submit_btn = gr.Button("Send", variant="primary")
            reset_btn = gr.Button("Reset Chat")
    
    def respond(message, chat_history):
        """Process user message and update chat history."""
        bot_message = chat(message)
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": bot_message})
        return "", chat_history
    
    def reset_chat(chat_history):
        """Reset chat."""
        reset_conversation()
        return []
    
    # Connect button clicks and text submission
    submit_btn.click(
        respond,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )
    msg.submit(
        respond,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )
    reset_btn.click(
        reset_chat,
        inputs=[chatbot],
        outputs=[chatbot]
    )

if __name__ == "__main__":
    demo.launch(share=False, server_name="127.0.0.1")
