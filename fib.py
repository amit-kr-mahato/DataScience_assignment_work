def get_number(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Please enter a  number not the text\n")

n = get_number(("Enter number of fibonacissicus: "))

a = 0   # first term
b = 1   # second term

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
