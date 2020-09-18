"""
Write a program which will print integers from 0 to 100 but it will print Research if it's multiple of 3,
Square if it's multiple of 5 or Research_Square if it's multiple of 15.

"""


def main():
    i = 0
    while i < 100:
        if ((i % 3) is 0) & ((i % 5) is 0):
            print("Research_Square")
        elif i % 3 is 0:
            print("Research")
        elif i % 5 is 0:
            print("Square")
        else:
            print(i)

        i = i + 1


main()
