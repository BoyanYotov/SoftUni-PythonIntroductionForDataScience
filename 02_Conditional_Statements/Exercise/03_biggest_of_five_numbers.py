numer1 = int(input())
numer2 = int(input())
numer3 = int(input())
numer4 = int(input())
numer5 = int(input())

# if numer1 > numer2 and numer1 > numer3 and numer1 > numer4 and numer1 > numer5:
#     print(numer1)
# elif numer2 > numer3 and numer2 > numer4 and numer2 > numer5 and numer2 > numer1:
#     print(numer2)
# elif numer3 > numer4 and numer3 > numer5 and numer3 > numer1 and numer3 > numer2:
#     print(numer3)
# elif numer4 > numer5 and numer4 > numer1 and numer4 > numer2 and numer4 > numer3:
#     print(numer4)
# else: print(numer5)

biggest = numer1
if numer2 > biggest:
    biggest = numer2
if numer3 > biggest:
    biggest = numer3
if numer4 > biggest:
    biggest = numer4
if numer5 > biggest:
    biggest = numer5

print(biggest)
