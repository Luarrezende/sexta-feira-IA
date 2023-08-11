import speech_recognition as sr
import pyttsx3
# import wikipediaapi
# import pywhatkit

# import openai

audio = sr.Recognizer
maquina = pyttsx3.init()


def listen_command():
    try:
        with sr.Microphone as source:
            print('Escutando...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'sextafeira' in comando:
                comando = comando.replace('sextafeira', '')
                maquina.say(comando)
                maquina.runAndWait()
    except Exception as e:
        print(f'um erro inesperado aconteceu: {e}')
    return comando
