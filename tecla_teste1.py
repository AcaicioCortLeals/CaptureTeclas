from pynput import keyboard

def on_press(key):
    try:
        print('Chave alfanumérica pressionada {0}' .format(key))
    except ArithmeticError:
        print('Chave Especial Pressionada {0}' .format(key))    


def on_release(key):
    print('Chave Precionada: {0}'.format(key))
    
    if key == keyboard.Key.esc:
        return False


#Coletando Eventos Until Release
with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()

