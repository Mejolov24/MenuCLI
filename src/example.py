import menucli as menu

def My_menu_callback(index, value = None): # will return none if it doesnt hold a value
    print("Hello from the menu callback, this is what i recieved : ", value, " From index : ", index)

def My_custom_callback(value = None): # will return none if it doesnt hold a value
    print("Hello from the custom callback, this is what i recieved : ", value)


def My_function():
    print("Hello from the function")

SubMenu = menu.Menu([
    menu.MenuItem("String", str,"Enter a String : "),
    menu.MenuItem("Exit",menu.Exit)
],
My_menu_callback, True, "\033[H\033[2J")

Menu = menu.Menu([
    menu.MenuItem("String", str ,"Enter a String : "),
    menu.MenuItem("Int", int, "Enter a number : " ),
    menu.MenuItem("Int 5-10", int, "Enter a number : " , 5, 10),
    menu.MenuItem("Int custom callback", int, "Enter a number : " , callback=My_custom_callback),
    menu.MenuItem("Function",callable, target=My_function),
    menu.MenuItem("SubMenu - zero indexed",menu.Menu,target=SubMenu),
    menu.MenuItem("Exit",menu.Exit)
],
My_menu_callback, False, "\033[H\033[2J")

print("\nStart\n")

menu.goToMenu(Menu)

try:
    while menu.render():
        print()
except KeyboardInterrupt:
    print("\nKeyboard interrupt!")

print("Exited loop")