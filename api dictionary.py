import requests
import speech_recognition
from playsound import playsound
from gtts import gTTS

def voicedict():
    voice=speech_recognition.Recognizer()#creating voice recognizer
    #now setting microphone as the source of voice....
    with speech_recognition.Microphone() as source:
        print("Speak the Word ......")
        voiceword=voice.listen(source)#using the listen function to listen voice through Microphone using recognizer.
        
        try:
            textword=voice.recognize_google(voiceword,language="en-us")#now converting the speech recognized in text in english language using recognize_google( ) function with recognizer(voice).
            print(textword)
            api_link="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+textword#getting the meaning using api
            api_get_request=requests.get(api_link)#now creating a get request
            api_data=api_get_request.json()#now taking the data in json format

            meaning=(api_data[0]["meanings"][0]["definitions"][0]["definition"])#now finding the meaning of word from the list(which contains dictionary)
            print(meaning)
            tts=gTTS(meaning,lang="en-us")#now converting the value of key from text to speech using gTTS function..
            tts.save("meaning.mp3")#now saving the file using save( ).
            playsound("meaning.mp3")#and now playing the sound file using playsound( ) function.
        except:
            print("unable to find")

if __name__=="__main__":
    voicedict()
