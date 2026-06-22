import urllib.request
import urllib.parse
from datetime import datetime

def get_weather(location=""):
    try:
        url = "https://wttr.in/" + urllib.parse.quote(location) + "?format=%l:+%C+%t"
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.68.0'})
        response = urllib.request.urlopen(req, timeout=5)
        weather_data = response.read().decode('utf-8').strip()
        # Clean up degree symbol for windows console
        weather_data = weather_data.replace('°', ' degrees ')
        return weather_data
    except Exception:
        return "I'm having trouble checking the weather right now."

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm doing well, thanks for asking! How about you?"
    elif user_input in ["what is your name", "who are you"]:
        return "I am H E R M I T."
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    elif user_input == "help":
        return "I can answer basic questions."
    elif user_input == "thank you" or "thanks" in user_input:
        return "You're welcome!"
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "weather" in user_input:
        if "weather in " in user_input:
            location = user_input.split("weather in ")[1].strip()
            return get_weather(location)
        else:
            return get_weather()
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    elif "what can you do" in user_input or "capabilities" in user_input:
        return "I can chat with you, tell a simple joke, and answer basic questions."
    elif "age" in user_input or "how old are you" in user_input:
        return "I'm just a few lines of code, so I don't have an age!"
    elif "favorite color" in user_input:
        return "I don't have eyes, but I imagine blue is a nice color."
    elif "where do you live" in user_input or "where are you from" in user_input:
        return "I live right here inside your computer!"
    elif "who made you" in user_input or "creator" in user_input:
        return "I was created as a project by a human programmer!"
    else:
        return "I'm sorry, I don't understand that. Could you try asking something else?"

def start_chat():
    print("Chatbot: Hello! I am H E R M I T.")
    print("Chatbot: You can say 'hello', 'how are you', or 'bye' to exit.")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        
        if not user_input.strip():
            continue
            
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower().strip() in ["bye", "goodbye", "see you", "exit", "quit"]:
            break

if __name__ == "__main__":
    start_chat()
