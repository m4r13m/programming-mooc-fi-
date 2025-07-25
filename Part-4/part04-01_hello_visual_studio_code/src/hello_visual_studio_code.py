while True:
    editor = input("Editor: ").lower().strip()
    if editor == "word" or editor == "notepad":
        print("awful")
    elif editor == "vim" or editor == "emacs" or editor == "atom":
        print("not good")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break