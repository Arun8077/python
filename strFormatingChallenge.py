# Average of 3 numbers
num1, num2, num3 = input("Please enetr three numbers ").split()
avg = (int(num1)+int(num2)+int(num3))/3
print(f"The average of three number entered {num1}, {num2} and {num3} is {avg}")
print("The average of three number entered {}, {} and {} is {}".format(num1, num2, num3, avg))

# num1, num2, num3 = int(input("Please enetr three numbers ").split())
num1, num2, num3 = map(int, input("Please enetr three numbers ").split())

sum = num1+num2+num3
print(sum)