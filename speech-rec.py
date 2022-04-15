import speech_recognition as sr
import json
from datetime import datetime

run = True 
data = {}
r = sr.Recognizer()

with open("notepad.json", "r") as f:
    data = json.load(f)

while run:
    with sr.Microphone() as source:
        print("Recognizing.....")
        audio_text = r.listen(source)
        print("Done!")

        try: 
            text = r.recognize_google(audio_text)
            print(json.dumps(data, indent = 4))
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            data["notes"].append({
                str(timestamp) : text
                })
            with open("notepad.json", "w") as outfile:
                outfile.write(json.dumps(data, indent = 0))
        except KeyboardInterrupt:
            print("Stopped")
        except:
            print("Couldn't Recognize")
            run = False