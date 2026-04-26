import speech_recognition as sr
import keyboard
import base64

def deviceNames():
    devices = sr.Microphone.list_microphone_names()
    for index, name in enumerate(devices):
        print(f"{index}: {name}")

def SpeechToText(index=None):
    Ai = sr.Recognizer()
    with sr.Microphone(device_index=index) as source:
        print("Hablando... presione q para salir")
        listening = Ai.listen(source, phrase_time_limit=6)

    try:
        command = Ai.recognize_google(listening, language="es-ES")
        command_bytes = command.encode("utf-8")
        command64 = base64.b64encode(command_bytes)

        print("Has dicho: " + command)
        print("Has dicho en Base64:", command64)

        with open("transcription.txt", "a", encoding="utf-8") as file:
            file.write(command + "\n")

        with open("transcription64.txt", "a", encoding="utf-8") as file:
            file.write(command64.decode("utf-8") + "\n")

    except sr.UnknownValueError:
        print("No entendi")

print("Dispositivos disponibles: ")
deviceNames()

micIndex = int(input("Elije el microfono que desea usar: "))
print("Presiona q para salir ")

while True:
    if keyboard.is_pressed('q'):
        print("Saliendo del programa... ")
        break
    else:
        SpeechToText(index=micIndex)