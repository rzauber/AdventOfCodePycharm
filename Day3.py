
def isSymbol(val):
    return not val.isdigit() and not val == '.'

def findNumber(input, row, col):
    digits = [input[row][col]]
    currCol = col
    while(True):
        if currCol == 0:
            break
        currCol -= 1
        if (input[row][currCol].isdigit()):
            digits.insert(0, input[row][currCol])
        else:
            break
    currCol = col
    while(True):
        if currCol == len(input[row]) - 1:
            break
        currCol += 1
        if (input[row][currCol].isdigit()):
            digits.append(input[row][currCol])
        else:
            break
    return int(''.join(digits))

def search(input, row, start, end):
    print('Open Search ' + str(row) + ' start[' + str(start) + '] end[' + str(end) + ']')
    for l in input[row-1 if row > 0 else 0:row+2]:
        print(l)
        for c in l[start-1 if start > 0 else 0:end+1]:
            if isSymbol(c):
                return True

def searchForNumbers(input, row, col):
    numbers = []
    for currRow in range(row-1 if row > 0 else 0, row+2):
        print(input[currRow])
        wasDigit = False
        for currCol in range(col-1 if col > 0 else 0, col+2):
            #print(input[currRow][currCol])
            if input[currRow][currCol].isdigit():
                if not wasDigit:
                    numbers.append(findNumber(input, currRow, currCol))
                wasDigit = True
            else:
                wasDigit = False
    print(numbers)
    return numbers


input = open('inputs/Day3.input').read().split('\n')
total = 0
for row, l in enumerate(input):
    #digits = 0
    #number = 0
    for col, c in enumerate(l):
        if c == '*':
            nums = searchForNumbers(input, row, col)
            if len(nums) == 2:
                total += nums[0] * nums[1]
        #if c.isdigit():
        #    if number > 0:
        #        number *= 10
        #    number += int(c)
        #    digits += 1
        #    if col != len(l) - 1:
        #        continue
        #    else:
        #        digits -= 1 # simulate moving to next digit for below work
        #elif number == 0:
        #    continue

        #print(number)
        #if search(input, row, col - digits, col):
        #    print(number)
        #    total += number
        #digits = 0
        #number = 0


print(total)