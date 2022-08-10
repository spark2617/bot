import speech_recognition as sr
import pyautogui


def verificaPalavra(frase):
    if "entenderam" or "entender" or "entenderas" or "tranquilo" or "duvida" or "dúvida" or "duvidas"or "dúvidas" not in frase:
        return False
    else:
        return True


def ouvir_microfone():

    #Habilita o microfone do usuário

    microfone = sr.Recognizer()

    

    #usando o microfone
    with sr.Microphone(device_index=2) as source:

        

        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        

        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        
        microfone.pause_threshold = 0.5
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

        

    try:

        

        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')

        

        #Retorna a frase pronunciada
        # print("Você disse: " + frase)
        if verificaPalavra(frase):
            pyautogui.click()
            pyautogui.write("1")
            pyautogui.press("enter")

        

    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except :
        pyautogui.click()
        pyautogui.write("Desculpe, mas não conseguir entender!")
        pyautogui.press("enter")

        


while True:
    ouvir_microfone()
