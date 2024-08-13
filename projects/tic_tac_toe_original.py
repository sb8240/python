import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        # print(e)
        return "None"
    return query


def sum(a,b,c):
    return a+b+c

def print_board(x,z):
    zero = 'X' if x[0] else ('O' if z[0] else 0)
    one = 'X' if x[1] else ('O' if z[1] else 1)
    two = 'X' if x[2] else ('O' if z[2] else 2)
    three = 'X' if x[3] else ('O' if z[3] else 3)
    four = 'X' if x[4] else ('O' if z[4] else 4)
    five = 'X' if x[5] else ('O' if z[5] else 5)
    six  = 'X' if x[6] else ('O' if z[6] else 6)
    seven = 'X' if x[7] else ('O' if z[7] else 7)
    eight = 'X' if x[8] else ('O' if z[8] else 8)
    print(f'\t\t\t {zero} | {one} | {two} ')
    print(f'\t\t\t---|---|---')
    print(f'\t\t\t {three} | {four} | {five} ')
    print(f'\t\t\t---|---|---')
    print(f'\t\t\t {six} | {seven} | {eight} ')

def check_win(x,z):
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in win:
        if(sum((x[w[0]]), (x[w[1]]), (x[w[2]])) == 3):
            print(f'{your1} won the match')
            return 1
        if(sum((z[w[0]]), (z[w[1]]), (z[w[2]])) == 3):
            print(f'{your2} won the match')
            return 0
    return -1


if __name__ == '__main__':
    print("say the name of player one:")
    your1 = take_command()

    print("say the name of player two:")
    your2 = take_command()

    print("player1 : ", your1)
    print("player2 : ", your2)
    
    time.sleep(5)

    x = [0,0,0,0,0,0,0,0,0]
    z = [0,0,0,0,0,0,0,0,0]

    turn = 1
    print('\t\t WELCOME TO TIC TAC TOE \t\t\t\n')

    while(True):
        print_board(x, z)
        if(turn == 1):
            print(f'this is {your1} chance')
            speak("Please say a value...")       #print("X's Chance")
                                                #value = int(input("Please enter a value: ")
            print('Please say a value...')
            plen = int(take_command())
            x[plen] = 1
        else:
            print(f'this is {your2} chance')
            speak("Please say a value...")
            print('Please say a value...')
            plen = int(take_command())
            x[plen] = 1
        cwin = check_win(x, z)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn