while True:
    try:
        num1 = int(input(">>>"))
        num2 = int(input(">>>"))
        character = input(">>>")

        match character:
            case '+': print(num1 + num2)
            case '-': print(num1 - num2)
            case '*': print(num1 * num2)
            case '/': print(num1 / num2)

    except ZeroDivisionError:
        print("division by zero")
    
    except ValueError:
        print("unknown character")