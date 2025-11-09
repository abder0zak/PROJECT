import winsound as ws
import time
text = input("Enter text to convert to Morse code: ").upper()
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
morse_code = ''


def text_to_morse():
    global morse_code
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char]+' '
        elif char == ' ':
            morse_code += " /"
    print("Morse Code:", morse_code)
    return morse_code


def play_morse_code():
    global morse_code
    dot_duration = 100
    dash_duration = dot_duration * 4
    frequency = 750

    for symbol in morse_code:
        if symbol == '.':
            ws.Beep(frequency, dot_duration)
        elif symbol == '-':
            ws.Beep(frequency, dash_duration)
        elif symbol == ' ':
            time.sleep(0.2)
        elif symbol == '/':
            time.sleep(3)


text_to_morse()
play_morse_code()
