import webbrowser
import pyttsx3
import musicLibrary
import browse
from openai import OpenAI

# Initialize and use text-to-speech to speak the provided text aloud
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# Handle and respond to the user's command
def process_command(c):
        try:
# If the command starts with 'open', attempt to open a website from the browse dictionary
            if(c.lower().startswith("open")):
                website = c.lower().split(" ")[1]
                link = browse.browser[website]
                webbrowser.open(link)
# If the command starts with 'play', attempt to play a song from the music library
            elif(c.lower().startswith("play")):
                song = c.lower().split(" ")[1]
                link = musicLibrary.music[song]
                webbrowser.open(link)
# If the command doesn't match known patterns, send it to the OpenAI assistant
            else:
                output = aiProcess(c)
                speak(output)
        except:
            speak("Sorry sir I Can't understand, Repeat your command please!")
# Use OpenAI API to generate a response to a user's command
def aiProcess(command):
    client = OpenAI(api_key="Your-API-Key",)
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Alex skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content
# Main interaction loop: greet the user and continuously process typed commands
if __name__ == "__main__":
    speak("Hello Sir My name is Alex how can I help You")
    while True:
        try:
            command = input("Give command: ")
            process_command(command)

        except:
            speak("Sorry sir I Can't understand, Repeat your command please!")