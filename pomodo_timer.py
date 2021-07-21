import time
from plyer import notification
def name;
count = 0
print("The pomodoro timer has started, start working!")

if name == "__main__":
    while True:
        time.sleep(1800)
        count += 1
        notification.notify(
            title = "Good work!",
            message = "Take a 10 minute break! You have completed " + str(count) + " pomodoros so far",
        )
        time.sleep(600)
        notification.notify(
            title = "Back to work!",
            message = "Try doing another pomodoro...",
        )
