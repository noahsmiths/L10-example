def createString():
    # print("Running createString loop...")

    s = ""
    for i in range(1000):
        s += str(i)

    # print("Done running createString loop.")

def count():
    # print("Running count...")

    n = 0
    for i in range(1000):
        n *= i

    # print("Done running count.")

def main():
    createString()
    count()

main()