# Greeting
def greeting():
    name = input("Welcome to space wave studios, May I have your name?")
    print(f"Thank you, {name}")


# Ask the user to put an pick from the following list.

def select():
    selction = input("Please pick from the following lists please "
                     "[1]Ice cream, [2]Fire power, [3]Tools of chaos")
    if selction == '1':
        ice_cream()
        return
    if selction == '2':
        fire_power()
        return
    if selction == '3':
        tools_of_chaos()
        return


def ice_cream():
    cream = input('Please select the type of ice cream')
    print(cream)
    return

def fire_power():
    power = ("We have the latest fire power in the world.")
    print(power)
    return

def tools_of_chaos():
    chaos = ("We have the latest tools of chaos ")
    print(chaos)
    return

greeting()
select()
