import time 
import winsound
def pomodoro(work_duration, break_duration, cycles):
    frequency = 440   
    buzzer_duration = 2000
    for i in range(cycles):
        print("Cycle", i+1, "of", cycles)
        winsound.Beep(frequency, buzzer_duration) 
        print("Work phase started. Focus!")
        time.sleep(work_duration)  
        print("Work phase completed. Take a break!")
        winsound.Beep(frequency, buzzer_duration) 
        time.sleep(break_duration) 