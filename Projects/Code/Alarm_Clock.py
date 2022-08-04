from datetime import datetime
from playsound import playsound

# Input
alarm_time = input("Please enter the alarm time(eg. 09:50:00 am): \n")
# Hour
alarm_hour = alarm_time[0:2]
# Miniute
alarm_minute = alarm_time[3:5]
# Second
alarm_seconds = alarm_time[6:8]
# AM or PM
alarm_period = alarm_time[9:11].upper()
print("Finish setting the alarm clock...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    # Time judgement
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake up!!!")
                    # Sound of alarm
                    playsound('audio.mp3')
                    break