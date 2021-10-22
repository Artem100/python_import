def say_hello(name):
    print(f"Hi, {name}")

def summa(*args):
    return sum(args)

def factorial (n):
    pr = 1
    for i in range(1, n+1):
        pr*=i
    return pr

my_srt = "Test string"
num1 = 1
num2 = 3


# Будет срабатывать, если код будет исполянться с текущего модуля
if __name__ == '__main__':
    print(123)
    print('Hi!')