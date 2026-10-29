elements = list(input().split())
dict = {}

while len(elements) > 0:
    key = elements.pop(0)
    value = elements.pop(0)
    dict[key] = value

products = list(input().split())

for product in products:
    if product not in dict.keys():
        print(f'Sorry, we don\'t have {product}')
    else:
        print(f'We have {dict[product]} of {product} left')
