from Q3PartA import percentage
import Q3PartA
from Q3PartB import reactor_core_warning
from Q3PartC import guessing_game

num1 = 10
num2 = 20
print("Numbers used 10 and 20")

print("\nQuestion A numbers test\n")
percentage(num1, num2)
print("\nQuestion A invalid test\n")
num1 = -10
num2 = -20
print("Numbers used -10 and -20")
percentage(num1, num2)

print("\nQuestion B Boundry tests\n")
print("Number used 0")
core_temp = int(0)
reactor_core_warning(core_temp)
print("Number used 400")
core_temp = int(400)
reactor_core_warning(core_temp)
print("Number used 700")
core_temp = int(700)
reactor_core_warning(core_temp)
print("Number used 1000")
core_temp = int(1000)
reactor_core_warning(core_temp)
print("Number used 1101")
core_temp = int(1101)
reactor_core_warning(core_temp)

print("\nQuestion C testing\n")
guess = int(30)
print("Number used 30")
guessing_game(guess)
guess = int(66)
print("Number used 66")
guessing_game(guess)
guess = int(42)
print("Number used 42")
guessing_game(guess)
