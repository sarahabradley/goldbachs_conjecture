import math

def findAllPrimes(max = 10000):
    # Use the sieve of sundaram to get a list of all prime numbers less than a maximum value
    if max < 3:
        return []
    n = int(max / 2) + 1
    primes = [] # Instantiate empty list of primes
    if max > 2:
        primes.append(2)

    marked = [True] * n

    for i in range(1, int((math.sqrt(max) - 1) / 2) + 1):
        for j in range(((i * (i + 1)) << 1), n, 2 * i + 1):
            marked[j] = False

    for i in range(1, n):
        if (marked[i] == True and (2 * i + 1) <= max):
            primes.append(2 * i + 1)
    return primes

def findGoldbachPrimes(n, primes, firstOnly=True):
    if (n <= 2 or n% 2 != 0):
        return False
    i = 0
    primePairs = []
    while (primes[i] <= n // 2):
        diff = n - primes[i]
        if diff in primes:
            if (firstOnly):
                return (primes[i], diff, n)
            else:
                primePairs.append((primes[i], diff, n))
        i += 1
    return primePairs

def tryParseInt(s, base = 10, default = None):
    try:
        return int(s, base)
    except ValueError:
        return default

def main():
    findAllPrimes(10)
    print("\nWelcome to the Godbach's conjecture checker\n------------------------------------------\n")
    max = 10000
    primesUnderMax = findAllPrimes(max)
    replay = True
    while (replay):
        validInput = False
        loopCount = 0
        userInt = 0
        userInput = input("Please enter an integer to check: ")
        while (validInput == False and loopCount < 10):
            userInt = tryParseInt(userInput)
            if (userInt is not None):
                validInput = True
            else:
                print("Invalid input, make sure that you enter a integer")
            loopCount += loopCount
        
        firstOnly = False if input("Would you like to find all possible pairs of primes for this number or just a single pair?\nEnter a for all or s for single: ") == 'a' else True
        if (userInt > max):
            primesUnderMax = findAllPrimes(userInt)
            max = userInt
        primePairs = findGoldbachPrimes(userInt, primesUnderMax, firstOnly)
        if primePairs != False:
            if firstOnly:
                print(primePairs[0], "+", primePairs[1], "=", primePairs[2])
            else:
                for pair in primePairs:
                    print(pair[0], "+", pair[1], "=", pair[2])
        else:
            print("The number is not a positive even integer greater than 2 and so doesn't fit Goldbach's conjecture!")
        
        replay = False if input("Would you like to enter another number? Enter q to quit or any other character to proceed: ") == 'q' else True

if __name__=="__main__":
    main()
