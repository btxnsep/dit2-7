
numbers = []

for i in range(5):
    num = int(input(f"ตัวเลขที่ {i+1}: "))
    numbers.append(num)


numbers.sort()


print("ตัวเลขจากน้อยไปมาก", numbers)