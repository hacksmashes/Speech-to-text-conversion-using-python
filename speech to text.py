import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak something.......")             # plss speak after this statement printed in the output window 
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("user said : ",end=" ")
        print(query)

    except Exception as e:
        print("say that again please")          # if it is not able to recognize ur voice means, this will print in the output window 
