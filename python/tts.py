#relevant imports for the script to run
#gtts (Google-Text-To-Speech) to convert text to audio files which can be played/listened to
from gtts import gTTS
import os

#filehandler which contains the .txt file with the text to be converted
fh = open("text.txt", "r")
myText = fh.read().replace("\n", "")

#language the text-to-speech algorithm will process
language = "en"

#setting the input, language format and speed of the output 
output = gTTS(text = myText, lang = language, slow = False)

#output file saved as an mp3 which will be played with the system's default audio file manager
output.save("output.mp3")

#closing the file handler
fh.close()
os.system("start output.mp3")