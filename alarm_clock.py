#-----------------alrm clock :
from playsound import playsound
import time



def alarm(seconds) :

    time_ealpsed = 0
    while time_ealpsed < seconds :

        time.sleep(1)
        time_ealpsed += 1
        
        time_left = seconds - time_ealpsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60
        print(f"{minutes_left :02d}:{seconds_left :02d}", end = '\r')
    playsound("alarm.mp3")

minutes = int(input("How many Minutes to Wait: "))
seconds = int(input("How Many Seconds to Wait: "))
total_seconds = minutes * 60 + seconds 

alarm(total_seconds)
