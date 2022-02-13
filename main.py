# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# Program ask the user put the number
S = 0
N: int= int(input(("Please Insert the Number : ")))
for i in range(1, N+1) :
    S+=i
print("Somme of Numbers is : ", S)

# Programm qui permet d'afficher un table de multiplication

N1 = int(input("Plase put the FIRST Value = "))
N2 = int(input("Please entre tge SECOND value = "))
for i in range(1, N1+1) :
    for j in range(1, N2+1) :
        print(i, " * ", j, end="")
        print(" = ", i * j)



