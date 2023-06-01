#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        print("X is less that Y")

    elif x == y:
        print("x equals y")
    else:
        print("x is greater than y")

    # conditional statements let you use "a if C else b"

    # match-case makes it easy to compare multiple values
    value = "one"

if __name__ == "__main__":
    main()
