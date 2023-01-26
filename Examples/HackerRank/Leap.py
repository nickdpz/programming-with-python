def is_leap(year):

    leap = False
    isMultipleFour = year % 4 == 0
    if (isMultipleFour):
        isMultipleHundred = year % 100 == 0
        leap = not isMultipleHundred or (year % 400 == 0 and isMultipleHundred)

    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))
