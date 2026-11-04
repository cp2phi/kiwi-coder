# 🔢 int()：把文字变成数字  int(): turn text into a number
# test-input: 12
# input() 给你的永远是文字，想算数就要先 int()  input() always gives text; to do maths you need int() first

age = int(input("你几岁了？ "))

print(f"明年你就 {age + 1} 岁啦！")
print(f"如果你是一只狗，你已经 {age * 7} 岁了 🐶")
print(f"再过 {18 - age} 年你就是大人了。")
