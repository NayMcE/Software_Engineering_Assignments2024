def recap(aNumber):
    for num in range (aNumber + 1):
        if num == 42:
            print("Found the meaning of life")
            return
    print("Did not find 42")

recap(50)