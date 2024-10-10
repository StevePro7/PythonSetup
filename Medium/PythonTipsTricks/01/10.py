option = input()

match option:
    case "M":
        print("Menu List")
    case "1" | "2":
        print("Menu Option")
    case _:
        print("Exit")