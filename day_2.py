def factorial(num):
    if num == 0:
      return 1
    return num * factorial(num - 1)
print('Enter an interger...')
num = int(input())
print(factorial(num))
