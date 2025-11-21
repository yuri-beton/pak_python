a = int(input("Please enter your number: "))
if a > 7:
    print("Hello")

name = input("Please enter name: ")
if name == "John":
    print("Hello, John")
else:
    print("There is not such name")

arr = input("Please enter your numeric array: ").split()
for i in range(0, len(arr)):
    arr[i] = int(arr[i])

print("Numbers thar are multiplies of 3:", end=" ")
for i in arr:
    if i % 3 == 0:
        print(i, end=" ")
