from ENGINE.STT.speech_recog import speech_recognition_model, close_driver
from ENGINE.TTS.deepAI import speak
#from BRAIN.TEXT.API import openrouter
from BRAIN.TEXT.API import deepInfra_TEXT
#from BRAIN.IMAGE import deepInfra_IMG

print('L.U.N.A Ai is Processing!')
print('Made By: Kunal Jain ~~~')
print('Model Initialized...')

try:
    while True:
        speech = speech_recognition_model()
        if speech:
            print("Kunal >>", speech)

        
        #ai_response = openrouter.generate(speech)
        ai_response = deepInfra_TEXT.generate(speech)
        print("L.U.N.A >>", ai_response)
        speak(ai_response)

        #speak("Sure Kunal, Generating image for you")
        #images_link = deepInfra_IMG.generate(speech)
        #print(images_link)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    close_driver()