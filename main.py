from ENGINE.STT.speech_recog import speech_recognition_model, close_driver
from ENGINE.TTS.deepAI import speak
#from BRAIN.TEXT.API import openrouter
from BRAIN.TEXT.API import deepInfra_TEXT
from BRAIN.IMAGE import deepInfra_IMG

try:
    while True:
        speech = speech_recognition_model()
        if speech:
            print("Kunal >>", speech)

            speak("Sure Kunal, Generating image for you")
            images_link = deepInfra_IMG.generate(speech)
            print(images_link)

            ai_response = deepInfra_TEXT.generate(speech)
            #ai_response = openrouter.generate(speech)
            print("AI >>",ai_response)
            speak(ai_response)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    close_driver()