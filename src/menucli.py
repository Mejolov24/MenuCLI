from collections.abc import Callable


class MenuItem:
    def __init__(self, name : str, type : type, value_name : str = None , target : Callable[[any], None] = None, value_min = None, value_max = None):
        self.name = name
        self.value_name = value_name
        self.type = type
        self.target = target
        self.value_min = value_min
        self.value_max = value_max

class SubMenu: pass
class Exit: pass

menu_stack : list[list[MenuItem]] = []

def goToMenu(menu : list[MenuItem], append = False):
    if append:
        menu_stack.append(menu)
    else:
        menu_stack.clear()
        menu_stack.append(menu)

def goBack():
    menu_stack.pop()

def _ask_value(type : type, text : str, min = None, max = None):
    while True:
        while True:
            try:
                answer = input(text)
                result = type(answer)
                if (min == None and max == None) : return result
                if (type == int):
                    if not (result < min or result > max) : return result
                    else: print("\033[31m", "[ERR] Invalid input, must be btween {min} and {max}!","\033[0m")
            except ValueError:
                print("\033[31m", f"[ERR] Invalid input, must be a {type.__name__}!","\033[0m")

def render(zero_indexed : bool = False, separator : str = ""):
    if len(menu_stack) == 0 : return False
    current_menu : list[MenuItem] = menu_stack[-1]
    current_menu_length : int = len(current_menu)
    print(separator)
    for index, item in enumerate(current_menu):
        print(index + int(not zero_indexed), item.name)
    selection_index : int = _ask_value(int, " Select an option : ",0 + int(not zero_indexed),current_menu_length) - int(not zero_indexed)
    selection : MenuItem = current_menu[selection_index]
    match (selection.type):
        case x if x is callable:
            result = selection.target()
            if result is False : return result
        
        case x if x is SubMenu:
            print(separator)
            goToMenu(selection.target,True)
            return render()

        case x if x is Exit:
            if (len(menu_stack) > 0):
                print(separator)
                goBack()
                return render()
            else : return False

        case _:
            selection_value = _ask_value(selection.type, "  " + selection.value_name, selection.value_min, selection.value_max)
            if (selection.target): selection.target(selection_index,selection_value)
    return True
