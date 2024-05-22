import speech_recognition as sr
def transcribe_audio(audio_file):
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        # Read the entire audio file
        audio = recognizer.record(source)

    try:
        # Use Google Speech Recognition to transcribe the audio
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
audio_file_path = "recording.wav"

# Call the transcribe_audio function
transcription = transcribe_audio(audio_file_path)

# Print the transcription
print(transcription)