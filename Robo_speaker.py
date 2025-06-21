# if not working in vs code terminal type pip install pytysx3
# import it then 
# import pyttsx3   
# This initializes the text-to-speech engine.
# You can think of engine as your virtual speaker.
# init() sets up everything needed for speaking.

import pyttsx3   

# # Initialize the text-to-speech engine
# #engine is just a variable holdnig engine object you can change the name as you want 
# engine = pyttsx3.init()

# # First sentence
text = "Hello, I am your Robo Reader. How can I assist you today?"
engine.say(text)
engine.runAndWait()

# # Loop for user input
while True:
    text1 = input("Enter the text you want me to speak (or type 0 to exit):\n")
    
    if text1 == "0":
        engine.say("Bye bye! You pressed 0. 🙌")
        engine.runAndWait()
        break

    engine.say(text1)
    engine.runAndWait()






# to change voice h=of our system 
print(" 1 for female and 0 index value  for male ")
import pyttsx3

# Initialize
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Print all available voices (optional, to explore)
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.id}")

# Set voice (0 for male, 1 for female on most Windows system
engine.setProperty('voice', voices[1].id) 
# Change index to 0 or 1  
# Test message
engine.say("Hello, I am using a different voice now.")
engine.runAndWait()
