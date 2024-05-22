from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--disable-audio")
opt.add_argument("--disable-video")
# # Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 2,
"profile.default_content_setting_values.media_stream_camera": 2,
"profile.default_content_setting_values.geolocation": 2,
"profile.default_content_setting_values.notifications": 2
})
opt.add_argument("--disable-blink-features=AutomationControlled")
#Gives path to chrome webdriver and loads classroom webpage
driver = webdriver.Chrome(options = opt)
# To join the video meeting, click this link: https://meet.google.com/yfi-pdvj-uqc
# Otherwise, to join by phone, dial +1 314-649-4870 and enter this PIN: 950 288 359#
# To view more phone numbers, click this link: https://tel.meet/yfi-pdvj-uqc?hs=5
meet_link = "imi-rbmq-zoc"
# driver = webdriver.Chrome(executable_path='ChromeDrivers/mac64 m1/chromedriver')
driver.get(f'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmeet.google.com%2F{meet_link}%3Fauthuser%3D1%26hs%3D49&hl=en&theme=mn&flowName=GlifWebSignIn&flowEntry=AccountChooser')

#Logs in the classroom
# username=driver.find_element_by_id('identifierId')
username = driver.find_element(By.ID, 'identifierId')
username.click()
username.send_keys('bot email id')

# next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
# next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[2]')

wait = WebDriverWait(driver, 10)
next = wait.until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
next.click()

password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
password.click()
password.send_keys('bot password')

# next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next = wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
next.click()
# time.sleep(500)
time.sleep(5)

#print(driver.title)

join = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[25]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')))
# join=driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[25]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')
join.click()

import pyaudio
import wave

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 120  # Adjust the duration as per your requirements
OUTPUT_FILE = "recording.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the recording stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording started...")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a WAV file
with wave.open(OUTPUT_FILE, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))

print("Audio file saved as", OUTPUT_FILE)

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

# Specify the path to your audio file
audio_file_path = "recording.wav"

# Call the transcribe_audio function
transcription = transcribe_audio(audio_file_path)

# Print the transcription
print(transcription)
# from fpdf import FPDF
 
 
# # save FPDF() class into a 
# # variable pdf
# pdf = FPDF()
 
# # Add a page
# pdf.add_page()
 
# # set style and size of font 
# # that you want in the pdf
# pdf.set_font("Arial", size = 15)
 
# # create a cell
# pdf.cell(200, 10, txt = transcription, 
#          ln = 1, align = 'L')
 
# # save the pdf with name .pdf
# pdf.output("GFG.pdf") 