def count(n):
    if n == 0:
        print("partenza")
    else:
        print(n)
        count(n - 1)

def main():
    n = int(input("da quanto conto? "))
    count(n)

if __name__ == "__main__":
    main()