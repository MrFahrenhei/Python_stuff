# print even numbers between 1 to 10
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
print("_--_")
# Código do Mosh
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")
