
def speech():
    import speech_recognition as sr
    import pyttsx3
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    def get_microphone():
        microphone_list = sr.Microphone.list_microphone_names()
        print("Available microphones:")
        for i, microphone_name in enumerate(microphone_list):
            print(f"{i}: {microphone_name}")
        while True:
            try:
                choice = 1
                return sr.Microphone(device_index=choice)
            except ValueError:
                print("Invalid choice. Please enter the index of the microphone.")

    microphone = get_microphone()
    def listen():
        with microphone as source:
            print("Speak something...")
            recognizer.adjust_for_ambient_noise(source) 

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
    def speak(text):
        print("System speaking:", text)
        engine.say(text)
        engine.runAndWait()

  
    while True:
        user_input = listen()  
        if user_input:
            speak("You said: " + user_input)
        
        




