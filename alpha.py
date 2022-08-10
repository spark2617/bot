from distutils.log import error
from time import sleep
import speech_recognition as sr
import pyautogui


def verificaPalavra(frase):
    if "entender"in frase:
        return True
    elif  "beleza" in frase:
        return True
    elif  "tranquilo" in frase:
        return True
    elif  "entendeu" in frase:
        return True
    else:
        return False

def ouvir_microfone():

    #Habilita o microfone do usuário

    microfone = sr.Recognizer()

    

    #usando o microfone
    with sr.Microphone(device_index=2) as source:

        

        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        

        #Frase para o usuario dizer algo
        print("ouvindo.... ")

        
        #microfone.pause_threshold = 0.7
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

        

    try:

        

        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')

        

        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        if verificaPalavra(frase):
            pyautogui.click(x=1199, y=660)
            pyautogui.write("1")
            pyautogui.press("enter")
            print("certo")

        

    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except :
        # pyautogui.click(x=1199, y=660)
        # pyautogui.write("Desculpe, mas não conseguir entender!")
        # pyautogui.press("enter")
        print("erro")
        
def colocaMensagem(mensagem):
    pyautogui.click(x=1199, y=660)
    pyautogui.write(mensagem)
    pyautogui.press("enter")

#para dizer que esta ligado
print("ativo!")
# tempo para entrar no zoom
sleep(5)
colocaMensagem("ativando bot ....")
sleep(2)
colocaMensagem("pronto!")
# print(verificaPalavra("a segunda opção não seria meu resultante"))
while True:
    ouvir_microfone()
