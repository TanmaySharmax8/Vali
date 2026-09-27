from openai import OpenAI
import json
import os

client = OpenAI()

# =========================
# MEMORY SETTINGS
# =========================

MEMORY_FILE = "memory.json"
MAX_MEMORY_MESSAGES = 30


# =========================
# LOAD MEMORY
# =========================

def load_memory():
    """Load saved conversation memory from disk."""

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


# =========================
# SAVE MEMORY
# =========================

def save_memory():
    """Save conversation memory to disk."""

    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(
                conversation_history,
                file,
                indent=4,
                ensure_ascii=False
            )

    except OSError:
        pass


# =========================
# CONVERSATION MEMORY
# =========================

conversation_history = load_memory()


# =========================
# VALI AI BRAIN
# =========================

def ask_vali(user_message):
    """
    Sends the user's message to Vali's AI brain
    while keeping persistent conversation memory.
    """

    # Add user's message
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Keep memory from becoming unnecessarily large
    recent_history = conversation_history[-MAX_MEMORY_MESSAGES:]

    response = client.responses.create(
        model="gpt-5.6-luna",

        instructions="""
You are Vali, a personal AI assistant.

Your personality:
- Calm
- Intelligent
- Helpful
- Professional
- Concise when possible
- Friendly but not overly casual

You are being developed as a hybrid AI assistant that will eventually
control a laptop and communicate with a phone.

You have access to conversation history from previous sessions.

Use the conversation history to understand context and remember
information that the user has previously shared.

Always refer to yourself as Vali when appropriate.
""",

        input=recent_history
    )

    # Get Vali's response
    answer = response.output_text

    # Save Vali's response
    conversation_history.append({
        "role": "assistant",
        "content": answer
    })

    # Save everything locally
    save_memory()

    return answer