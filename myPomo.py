import time, os
from sys import platform

'''myPomo is a tui-program that enables you to work in the Pomodoro technique. 
    That means 25 min work and after that you take a 5 min break
'''
def main():

    rounds = 0

    while True:

        print('press \'q\' and hit enter to quit the program.')
        print('press \'b\' and hit to begin working for 25 minutes.')

        keyInput = input()

        if keyInput == 'b':

            #clears screen
            os.system('cls' if os.name == 'win32' else 'clear')
            print('start working for 25 min. you will hear an alarm.')
            timer(25)

            playSoundCmd = checkOS()
            playSoundCmd = playSoundCmd + ' alarm.wav'
            os.system(playSoundCmd)

            rounds += 1
            printWorking(rounds)

            print('now have a break for 5 minutes. you will hear the alarm again.')
            timer(5)
            os.system(playSoundCmd)

            # clears screen
            os.system('cls' if os.name == 'win32' else 'clear')

        elif keyInput == 'q':
            exit(0)

def printWorking(rounds):

    print('you worked for 25 min.')
    print('your total working time is ' + str(rounds * 25) + ' min.')


def timer(minutes):

    min = 0
    while(min < minutes):
        time.sleep(60)
        min += 1

def checkOS():

    if platform == "linux" or platform == "linux2":
        return 'aplay'
    elif platform == "darwin":
        return 'afplay'
    elif platform == "win32":
        return 'start /min mplay32 /play /close'

if __name__ == "__main__":
    main()