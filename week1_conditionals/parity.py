def is_even(n):
    #return True if n % 2 == 0 else False
    # most elegant version
    return n % 2 == 0

def main():
    x = int(input("Give X: "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

main()
