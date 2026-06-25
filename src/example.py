import menucli as menu

class ExitMenuException(Exception):
    pass

def My_callback(value):
    print()
    print("Hello from the callback, this is what i recieved : ", value)

def My_function():
    print()
    print("Hello from the function")

SubMenu : menu.MenuItem = [
    menu.MenuItem("String", str,"Enter a String : ", My_callback),
    menu.MenuItem("Exit",type=menu.Exit)
]

Menu : menu.MenuItem = [
    menu.MenuItem("String", str ,"Enter a String : ", My_callback),
    menu.MenuItem("Int", int, "Enter a number : " , My_callback),
    menu.MenuItem("Int 5-10", int, "Enter a number : " , My_callback, 5, 10),
    menu.MenuItem("Function",type=callable, target=My_function),
    menu.MenuItem("SubMenu",type=menu.SubMenu,target=SubMenu),
    menu.MenuItem("Exit",type=menu.Exit)
]

print("\n Start \n")

menu.goToMenu(Menu)

try:
    while menu.render():
        print()
except KeyboardInterrupt:
    print("\nKeyboard interrupt!")

print("Exited loop")