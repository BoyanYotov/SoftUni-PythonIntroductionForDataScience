balance = float(input())
withdraw = float(input())
limit = float(input())

if withdraw > limit:
    print("The limit was exceeded.")
elif withdraw <= balance:
    print("The withdraw was successful.")
elif withdraw > balance:
    print("Insufficient availability.")
