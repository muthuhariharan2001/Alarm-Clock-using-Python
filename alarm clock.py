"""import time
import winsound

def set_alarm(hour, minute):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            print("Time to wake up!")
            # Play alarm sound
            winsound.Beep(1000, 2000)  # Change frequency and duration as needed
            break
        else:
            # Check every 10 seconds
            time.sleep(10)

# Set the alarm time (24-hour format)
alarm_hour = 13
alarm_minute = 26

print(f"Alarm set for {alarm_hour}:{alarm_minute}")
set_alarm(alarm_hour, alarm_minute)
"""

"""import time
import pygame

def set_alarm(hour, minute, sound_files):
    pygame.mixer.init()

    for sound_file in sound_files:
        print("Time to wake up my boy...")
        print(f"Playing {sound_file}")
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    pygame.mixer.quit()

# Set the alarm time (24-hour format)
alarm_hour = 23
alarm_minute = 15

# Specify the paths to your audio files
audio_files = [
    "D:\\Music\\Asku-Laska-MassTamilan.fm.mp3",
    "D:\\Music\\Sivakumar-Pondati-MassTamilan.fm.mp3",
    "D:\\Music\\JD-vs-Bhavani-MassTamilan.io.mp3",
    "D:\\Music\\Kandaa-Vara-Sollunga-MassTamilan.fm.mp3"
]

print(f"Alarm set for {alarm_hour}:{alarm_minute}")
set_alarm(alarm_hour, alarm_minute, audio_files)"""

import time
import pygame

def set_alarm(hour, minute, sound_files):
    pygame.mixer.init()
    while True:
        current_time = time.localtime()
        print(f"Current time: {current_time.tm_hour}:{current_time.tm_min}")
        print(f"Alarm time: {hour}:{minute}")
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            print("Time to wake up my boy...")
            for sound_file in sound_files:
                print(f"Playing {sound_file}")
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                # Wait for the audio to finish playing on its own duration.
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            break
        elif current_time.tm_hour > hour or (current_time.tm_hour == hour and current_time.tm_min > minute):
            print("Alarm time has already passed.")
            break
        else:
            time.sleep(5)
    pygame.mixer.quit()
# Set the alarm time (24-hour format) (02 pm -> 14)
alarm_hour = 22
alarm_minute = 35

#List of your audio Files.
audio_files = [
    "D:\Music\Kadharalz.mp3",
    #"D:\Music\Vaathi-Coming-MassTamilan.io.mp3",
    #"D:\\Music\\Sivakumar-Pondati-MassTamilan.fm.mp3",
    'D:\Music\CEO-in-the-House-MassTamilan.org.mp3',
    #'D:\Music\Azhagiya-Soodana-Poovey.mp3',
    "D:\Music\Karikalan-Kala-Pola.mp3",
    "D:\\Music\\JD-vs-Bhavani-MassTamilan.io.mp3",
    "D:\Music\Kattabomman-Oorenakku.mp3",
    #"D:\Music\Endi-Ippadi.mp3",
    #"D:\\Music\\Kandaa-Vara-Sollunga-MassTamilan.fm.mp3",
    "D:\Music\Kasu-Panam.mp3",
    "D:\Music\Ketta-Kodukkira-Boomi.mp3",
    "D:\Music\Magudi-Magudi.mp3",
    "D:\Music\_Nee-Singam-Dhan-MassTamilan.dev.mp3",
    "D:\Music\Per-Vachaalum-Vaikkaama-MassTamilan.io.mp3"
]
print(f"Alarm set for {alarm_hour}:{alarm_minute}")
#FUnction Initiation
set_alarm(alarm_hour, alarm_minute, audio_files)