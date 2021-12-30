def uppercaseTransform(func):
    def wrapper(text: str):
        return func(text).upper()

    return wrapper


from datetime import date, datetime


def cowsay(func):
    def wrapper(text):
        length = len(text)
        print(" _" + length * "_" + "_ ")
        print("< " + text + " > ")
        print(" -" + length * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\       )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")
        #func(text)

    return wrapper


@cowsay
def messagePrint(text):
    print("**", text)


@uppercaseTransform
def message(nombre):
    return f"{nombre}, you have a message"


if __name__ == "__main__":
    print(message("Nico"))
    messagePrint("Nico")
