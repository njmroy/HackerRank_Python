# Print a list of integers from 1 through n without spaces

def print_range(x):
    numlist = []
    try:
        # Try to cast input to int
        num = int(x)
        # Add i in range from 0 to number
        for i in range(0, num, 1):
            numlist.append(i + 1)

        # Join elements in numlist as cast strings from ints
        print("".join(str(n) for n in numlist))
    except:
        num = input("Invalid input, try again:\n")
        print_range(num)


def main():
    print_range("foobar")
    print("Demo of more numbers...\n")
    for i in range(0, 8):
        print_range(i)


main()
