import speech_recognition as sr

mic_name = ""

sample_rate = 48000

chunk_size = 2048

r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    print(i, mic_list[i])
    
mic_input = input('Which microphone would you like to use? Enter the number below:')
device_id = int(mic_input)

with sr.Microphone(device_index = device_id, sample_rate= sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print('Say Something')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

    except sr.UnknownValueError:
        print('Speech recognition could not understand audio')

    except sr.RequestError as e:
        print(f"could not request results. error; {e}")
