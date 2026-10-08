#1-masala
count = 0

while True:
    son = int(input("Son kirit: "))
    if son == 0:
        break

    if son > 10:
        count += 1
print(f"10 dan katta sonlar: {count}")
