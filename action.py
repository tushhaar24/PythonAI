import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
import wikipedia
import pyjokes


def Action(data):
    if data is None:
        print("Error: Input data is None")
        return None

    user_data = data.lower()

    if "what is your name" in user_data:
        response = "My name is Simba"
        text_to_speech.text_to_speech(response)
        return response

    elif any(greeting in user_data for greeting in ["hello", "hey"]):
        response = "Hey, sir! How can I help you?"
        text_to_speech.text_to_speech(response)
        return response

    elif "good morning" in user_data:
        response = "Good morning, sir"
        text_to_speech.text_to_speech(response)
        return response

    elif "time now" in user_data:
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {current_time}"
        text_to_speech.text_to_speech(response)
        return current_time

    elif "shutdown" in user_data:
        response = "Ok sir"
        text_to_speech.text_to_speech(response)
        return response

    elif "play music" in user_data:
        webbrowser.open("https://wynk.in/music")
        response = "Songs are ready for you"
        text_to_speech.text_to_speech(response)
        return response

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        response = "Opening YouTube"
        text_to_speech.text_to_speech(response)
        return response

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        response = "Opening Google"
        text_to_speech.text_to_speech(response)
        return response

    elif "weather update" in user_data:
        weather_response = weather.get_weather()
        text_to_speech.text_to_speech(weather_response)
        return weather_response

    elif "search for" in user_data:
        search_query = user_data.replace("search for", "").strip()
        try:
            search_result = wikipedia.summary(search_query, sentences=2)
            response = f"Here is what I found: {search_result}"
            text_to_speech.text_to_speech(response)
            return search_result
        except wikipedia.exceptions.DisambiguationError as e:
            response = f"There are multiple results for {search_query}. Please be more specific."
            text_to_speech.text_to_speech(response)
            return response
        except wikipedia.exceptions.PageError as e:
            response = f"Sorry, I couldn't find any information on {search_query}."
            text_to_speech.text_to_speech(response)
            return response

    elif "tell me a joke" in user_data:
        
        joke = pyjokes.get_joke()
        
        
        response = f"Sure, here's a joke for you: {joke}"
        text_to_speech.text_to_speech(response)
        return response

    else:
        response = "I am not able to understand"
        text_to_speech.text_to_speech(response)
        return response

