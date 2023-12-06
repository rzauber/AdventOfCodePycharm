import math
input = """Time:        56     97     77     93
Distance:   499   2210   1097   1440"""

inputMap = {56:499, 97:2210, 77:1097, 93:1440}

waysToBeatCounts = 1
for key in inputMap:
  maxTime = key
  distanceToBeat = inputMap[key]
  
  waysToBeat = []
  for i in range(0, maxTime + 1):
    speed = i
    distance = i * (maxTime - i)
    if distance > distanceToBeat:
      waysToBeat.append(i)
  waysToBeatCounts *= len(waysToBeat)
 
print(waysToBeatCounts)

inputMap = {56977793:499221010971440}

waysToBeat = []
for key in inputMap:
  maxTime = key
  distanceToBeat = inputMap[key]
  
  for i in range(0, maxTime + 1):
    speed = i
    distance = i * (maxTime - i)
    if distance > distanceToBeat:
      waysToBeat.append(i)
 
print(len(waysToBeat))

inputMap = {56977793:499221010971440}

waysToBeatCounts = 1
for key in inputMap:
  maxTime = key
  distanceToBeat = inputMap[key]
  
  minimumAverageSpeedRequired = distanceToBeat / maxTime
 
  minimumAmountOfTimeToHold = math.ceil(minimumAverageSpeedRequired)
  
  numberOfSecondsRequiredToTravelAtMaxSpeed = distanceToBeat / maxTime
  
  # maxTime - fastest travel speed - speed loss from max travel speed
  temp = maxTime - numberOfSecondsRequiredToTravelAtMaxSpeed
  
  maximumAmountOfTimeToHold = temp - 
  
  waysToBeatCounts = (maximumAmountOfTimeToHold - minimumAmountOfTimeToHold)
 
print(waysToBeatCounts)