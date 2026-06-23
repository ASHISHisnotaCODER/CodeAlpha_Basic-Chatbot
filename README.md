# CodeAlpha_Basic-Chatbot: H E R M I T

H E R M I T is a simple, rule-based conversational chatbot written in Python. It's designed to respond to basic greetings, answer simple questions, tell jokes, and even fetch the current weather and time!

![HERMIT Chatbot Demo](chatbot.png)

This project was built as part of the **CodeAlpha Internship**.

## Features

- **Basic Conversation:** Responds to greetings, farewells, and inquiries about its identity or capabilities.
- **Weather Information:** Fetches real-time weather data for a specified location (or your current location) using the `wttr.in` service.
- **Time Check:** Tells you the current local time.
- **Entertainment:** Can tell you a programming joke.
- **No External Dependencies:** Built entirely with Python's standard library (`urllib`, `datetime`, etc.), so no need to install external packages like `requests`.

## Prerequisites

- Python 3.x installed on your system.
- An active internet connection (required for the weather feature).

## Installation & Usage

1. Clone this repository or download the source code.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the chatbot using the following command:

   ```bash
   python chatbot.py
   ```

5. Start chatting! You can try typing queries like:
   - *"Hello"*
   - *"What is your name?"*
   - *"Weather in London"*
   - *"What time is it?"*
   - *"Tell me a joke"*
   - *"Quit"* or *"Bye"* to exit.

## Code Structure

- `start_chat()`: Initializes the chat loop and handles user input/output.
- `get_bot_response(user_input)`: Core logic that parses the user's text and determines the appropriate response based on keywords.
- `get_weather(location)`: Helper function that reaches out to the `wttr.in` API to get current weather conditions without needing an API key.

## Author

Created by **Ashish Kumar** (as part of the CodeAlpha Internship).
