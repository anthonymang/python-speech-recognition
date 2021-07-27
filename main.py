import speech_recognition as sr

sample_rate = 48000

chunk_size = 2048


r = sr.Recognizer()

audio_source = input('To record audio, Enter 1.\nTo upload audio, Enter 2.\n')

def record():
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


def upload():
    audio_file = input('Please enter path/name of audio file\n')
    AUDIO_FILE = audio_file

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        print(f"Transcription:\n{r.recognize_google(audio)}")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
 
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")



if int(audio_source) == 1:
    record()

elif int(audio_source) == 2:
    upload()