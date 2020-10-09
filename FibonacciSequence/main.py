import time


def writefile(finnum, lastnum, numlen, elapsed):
    elapsedmin = elapsed / 60
    elapsedmin = round(elapsedmin, 1)
    f = open("FinalNumber.txt", "w")
    f.write("-" * 80 +
            "\n" +
            "The " + str(lastnum) + " number in the Fibonacci Sequence is " + str(numlen) + " digits long." +
            "\n" +
            "It took " + str(elapsedmin) + " minutes to calculate, or " + str(elapsed) + " seconds" +
            "\n" +
            "The number is printed below." +
            "\n" +
            "-" * 80 +
            "\n")
    f.write(str(finnum))


def countwd(endnum):
    start = time.time()
    a = 0
    b = 1
    for i in range(0, int(endnum)):
        c = a + b
        a = b
        b = c
        print(c)
        i += 1
    end = time.time()

    numberLength = len(str(c))
    print("Your number is: " + str(numberLength) + " digits long")
    elapsed = end - start
    elapsed = round(elapsed, 3)
    print("Time Elapsed: " + str(elapsed) + " seconds")
    writefile(c, endnum, numberLength, elapsed)


def count(endnum):
    print("Calculating...")
    start = time.time()
    a = 0
    b = 1
    x = 0
    for i in range(0, int(endnum)):
        c = a + b
        a = b
        b = c
        i += 1

        x += 1
        if x == 250000:
            print("Calculating...")
            x = 0

    end = time.time()

    numberLength = len(str(c))
    print("Your number is: " + str(numberLength) + " digits long")
    elapsed = end - start
    elapsed = round(elapsed, 3)
    print("Time Elapsed: " + str(elapsed) + " seconds")
    writefile(c, endnum, numberLength, elapsed)


decision = input("Would you like to see the digits as they are being counted?(1 for no, 2 for yes): ")


if int(decision) == 1:
    num = input("How high would you like to go?: ")
    count(int(num))
else:
    num = input("How high would you like to go?: ")
    countwd(int(num))











