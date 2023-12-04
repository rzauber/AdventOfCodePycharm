sum = 0
limits = {'red': 12, 'green': 13, 'blue': 14}
gameNum = 1

totalPower = 0
for l in open('inputs/Day2.input'):
  isValid = True
  required = {}
  games = l.strip().split(':')[1].split(';')
  for game in games:
      colors = game.strip().split(',')
      for color in colors:
          vals = color.strip().split(' ')
          color = vals[1]
          number = int(vals[0])
          if limits[color] < number:
              isValid = False

          if color not in required or required[color] < number:
              required[color] = number
  if isValid:
      sum+=gameNum
  gameNum+=1

  power = 1
  for color in required:
     power *= required[color]
  totalPower += power
print('Sum is: ' + str(sum))
print('Power is: ' + str(totalPower))

