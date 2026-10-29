from unittest import case

fruit = str(input())

match fruit:
    case "banana":
        print("fruit")
    case "apple":
        print("fruit")
    case "lemon":
        print("fruit")
    case "kiwi":
        print("fruit")
    case "cherry":
        print("fruit")
    case "cucumber":
        print("vegetable")
    case "pepper":
        print("vegetable")
    case "carrot":
        print("vegetable")
    case "cucumber":
        print("vegetable")
    case _:
        print("unknown")
