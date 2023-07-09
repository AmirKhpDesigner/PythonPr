python
numbers = []
for i in range(10):
    number = int(input("لطفاً یک عدد وارد کنید: "))
    numbers.append(number)

sorted_numbers = sorted(numbers)
print("اعداد مرتب شده: ", sorted_numbers)

print("اعداد زوج: ", end="")
for number in sorted_numbers:
    if number % 2 == 0:
        print(number, end=" ")