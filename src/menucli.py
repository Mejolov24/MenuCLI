import colors
from collections.abc import Callable


class MenuItem:
    def __init__(self, name : str, value_name : str, type : type, callback : Callable[[any], None] = None, value_min = None, value_max = None):
        self.name = name
        self.value_name = value_name
        self.type = type
        self.callback = callback
        self.value_min = value_min
        self.value_max = value_max

menu_stack : list[list[MenuItem]] = []

def goToMenu(menu : list[MenuItem], append = False):
    if append:
        menu_stack.append(menu)
    else:
        menu_stack.clear()
        menu_stack.append(menu)


def _ask_value(type : type, text : str, min = None, max = None):
    while True:
        while True:
            try:
                answer = input(text)
                result = type(answer)
                if (min == None and max == None) : return result
                if (type == int):
                    if not (result < min or result > max) : return result
                    else: colors.colorprint(f"[ERR] Invalid input, must be btween {min} and {max}!","red")
            except ValueError:
                colors.colorprint(f"[ERR] Invalid input, must be a {type.__name__}!","red")

def render():
    stack_length = len(menu_stack)
    if stack_length == 0 : return
    current_menu : list[MenuItem] = menu_stack[-1]
    current_menu_length : int = len(current_menu)

    for index, item in enumerate(current_menu):
        print(index + 1, item.name)
    print()
    selection : MenuItem = current_menu[_ask_value(int, "Select an option : ",0 + 1,current_menu_length) - 1]
    if (selection.type is not callable):
        selection_value = _ask_value(selection.type, selection.value_name, selection.value_min, selection.value_max)
        if (selection.callback): selection.callback(selection_value)
    else :
        result = selection.callback()
        if result is False : return result
    return True
