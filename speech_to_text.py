import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

        try:
            voice_data = recognizer.recognize_google(audio)
            print("You said:", voice_data)
            return voice_data

        except sr.UnknownValueError:
            print("Error: Could not understand audio")

        except sr.RequestError as e:
            print(f"Error making request to Google Speech Recognition service: {e}")

# Example usage:
# text = speech_to_text()
# print("Text obtained:", text)
