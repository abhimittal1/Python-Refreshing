# Use the external module 

# I am using the pyttsx module -
# Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

# pip install pyttsx3 --> install using the pip 
# use --> import 

import pyttsx3 #importing 
engine = pyttsx3.init() #storing in variable
a = "I am speaking using the external module. This is too easy."
engine.say(a) #line what to speak
engine.runAndWait() # run
