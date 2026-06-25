import menucli as menu

class ExitMenuException(Exception):
    pass

def My_callback(value):
    print()
    print("Hello from the callback, this is what i recieved : ", value)

def My_function():
    print()
    print("Hello from the function")

def exit_loop():
    return False


Menu : menu.MenuItem = [
    menu.MenuItem("String", "Enter a String : ", str, My_callback),
    menu.MenuItem("Int", "Enter a number : ", int, My_callback),
     menu.MenuItem("Int 5-10", "Enter a number : ", int, My_callback, 5, 10),
    menu.MenuItem("Function","", callable, My_function),
    menu.MenuItem("Exit","",callable,exit_loop)
]

print("\n Start \n")

menu.goToMenu(Menu)

try:
    while menu.render():
        print()
except KeyboardInterrupt:
    print("\nKeyboard interrupt!")

print("Exited loop")