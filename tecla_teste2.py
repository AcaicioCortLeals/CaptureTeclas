import keyboard


if __name__== '__main__':
    while True:
        if keyboard.read_key() == 'p':
            print("Você precionou P")
            break   