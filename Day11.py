input = """.....#...............#......................................................................#.............................#..........#......
........................................#............................#......#...............................................................
..............................#..............#....................................#..............................................#..........
..............#........................................................................#....................................................
..#...........................................................................................#.............................................
..................#.....................................#.....#......................................#.........#.......#....................
...........#......................................#.....................#...........#................................................#......
.............................#............................................................#.....................................#...........
.....#..................#.................#.........................#......................................#................................
....................................#.................#........................#..........................................................#.
................#..............................#....................................................#.......................................
..............................................................#.........................#.......................#.....................#.....
............#...............#......................#.....................#..............................#...................................
......................................#...............................................................................#.....................
.........................................................#..................................................................................
..............................................#.............................................................................................
..#.................#.....................................................................#.....#..........#..............#......#..........
..............................................................................#.............................................................
..........................................#.........................#..............................................#........................
.....#........#.............#...........................#...........................................#.......................................
..................................#...............#.............#.................#..........................#.....................#........
.......................................................................#....................................................................
...............................................................................................................................#.........#..
#.......................................#....................................................#.........................#....................
........#...............#....................................#...........................................#..................................
...............................#............................................................................................................
.........................................................#..................................................................................
..#..........................................#........................................#.............#............................#..........
......................#............................#.................#........#.............................................................
.........#.......#...........................................................................#.....................#.........#.........#....
................................#............................................................................#..............................
.........................................................................................#..................................................
.#.........................................#.........#..........#.......................................................#...................
....................#.................#...............................................................#.....................................
............................................................................#...............................................................
........................#.........................................................................................#.................#.......
.............#.......................................................#......................................................#...............
.......#.................................#.....#..............................................................#.............................
#...............................#...............................................................#.....................#.....................
.....................................#...................#.......................#.....#.......................................#............
..........................#.................#......#...................................................................................#....
..............#.............................................................................................................................
...#..........................................................................#............................................#................
.............................................................................................#.....................#......................#.
.......................................#..........................................................................................#.........
.......................................................................................................#....................................
.....#.........#.................#.................#............#.........................#.................#...............................
............................#.....................................................#.........................................................
...........................................#................................................................................................
....................................#.......................#.........................#............................#.....#..................
............................................................................................................................................
.....................#..................#................................#......#.....................................................#.....
.......................................................#.........#...............................#.....#....................................
............#.................................................................................................................#.............
..............................................#..............#.......#.................................................#....................
................................................................................................................#...........................
.........#.............................................................................#............#.......................................
.............................#...........................................#.....#............................................................
.....#..........#.....#...........#.............#.....#.............................................................................#.......
...........................................#............................................................#.....#.............................
......................................#.........................#.........................#.....................................#...........
............................................................................................................................................
.......#.....#.....#........................................#.................................#.............................................
.........................................#................................................................#.....#......#....................
........................#.......#..................#.................................#.......................................#.......#......
..............................................#.............................................................................................
...............................................................................#............................................................
......................................................#..........#..........................................................................
...#......#.................#.............#.............................#..........................#...............................#........
.............................................................#........................#..........................#.........#................
......................................#....................................................#.............................................#..
............................................................................................................................................
...............#......#.......................#.....#.......................................................#...............................
.#......#.......................#.........................#.......#....................................#....................................
...............................................................................................#........................#......#.......#....
............#...............#............#....................#........#..........#.........................................................
...............................................................................................................#............................
..........................................................................................................#.................#...............
......................#........#.........................................................................................................#..
....................................................................................#.....#.....#....................#......................
.#.........#...............#........................................#...............................................................#.......
..................#......................................................#..........................#.......................................
.................................#.............#................................................................#.......#...................
........................#......................................................#..............#................................#............
.....#..........................................................#.....#.................#..................................................#
.....................................#......#.........#...............................................#.....................................
............................................................................................................................................
............................................................................................................................................
.................................#..........................................#................#...................#..............#...........
.......#....................#............#.............................................#...................................#................
..#................#........................................#.......#..............................#........................................
........................#...........................................................................................................#.......
...........#..........................................#.........................#......................#....................................
...........................................#................................................................................................
......#...............................................................................#.........#...........................................
............................#.....................#................#........................................#...........#...................
..................#.........................................#...............................................................................
........................#...............#................................#.......#..............................#............#..............
............#......................#.................#..................................................#..................................#
..#................................................................................................#........................................
.........................................................................................................................#..................
..................................................................#................................................#................#.......
.......#.....................................#..............................................................................................
.................#...............#......#.....................#.............................................................................
....................................................................................#..................................#....................
..............................................................................................#............#................................
....#......................#................................................................................................................
......................................................#.................................#..........................#.............#..........
..........#.................................................................................................................#...............
.................................#..........#..................................#............................................................
.......................................................................................................................................#....
.......................................#..................................................................#......#..........................
.............................#.........................................................#.......#............................................
.........#....................................#............#.................................................................#..............
...#...............................................................................#.................#......................................
..................................................................................................................................#.........
....................#.............#...................................................................................#....................#
....................................................#...........#...........#...............................................................
.........................................................................................................#..................................
..........#...............................#............................#....................................................................
.............................................................#....................#.............................#..............#............
.#...............#..........................................................................#..........................................#....
............................#...............................................................................................................
............#......................................#............#..................................................................#........
.......#...............................................................................................................#....................
..................................#.......#..........................#........#...............#..........#....................#.............
....................#....................................#............................#..........................#.......................#..
..............................................................#.............................................................................
..#............................#............................................................................#...............................
..............#.....................#...............................................................................................#.......
..........................#........................................#....................................#...........#.......................
..........................................#.................................#.................#.............................................
................................................#...........#..........#.....................................................#..............
.........#..................................................................................................................................
...................................................................................#............................#.......#...................
....#.............................#.............................#.......................................................................#...
.........................................#.........................................................#........................................
....................#...........................................................................................................#...........
..............#........................................#..................................#...................#......................#......
.........#.................#........................................#...........#........................................#.................."""

example_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

current_input_lines = input.splitlines()
#part 1
updated_y_lines = []
for l in current_input_lines:
  updated_y_lines.append([*l])
  if l.find('#') == -1:
    updated_y_lines.append([*l])

columns_that_need_expansion = []
for x,c in enumerate(updated_y_lines[0]):
  if c == '.':
    allDots = True
    for l in updated_y_lines:
      allDots &= (l[x] == '.')
    if allDots:
      columns_that_need_expansion.append(x)
      
updated_input_lines_for_expansion = []
for y,l in enumerate(updated_y_lines):
  line = []
  for x,c in enumerate(l):
    line.append(c)
    if x in columns_that_need_expansion:
      line.append(c)
  updated_input_lines_for_expansion.append(line)
  
def printGrid(input):
  for l in input:
    line = ''
    for c in l:
      line += c
    print(line)

printGrid(updated_input_lines_for_expansion)

def getRange(val, val2): 
  if val > val2:
    return range(val2, val + 1)
  else:
    return range(val, val2 + 1)

class Galaxy:
  def __init__(self, y, x): 
    self.x = x
    self.y = y
  def __str__(self): 
    return '(' + str(self.x) + ',' + str(self.y) + ')' 
  def distanceToOther(self, other):
    return abs(other.x - self.x) + abs(other.y - self.y)
  def distanceToOtherWithExpansions(self, other, columns_that_need_expansion, rows_that_need_expansion, expansion_size):
    totalDistance = abs(other.x - self.x) + abs(other.y - self.y)
    for i in getRange(other.x, self.x):
      if i in columns_that_need_expansion:
        totalDistance += expansion_size - 1
    for i in getRange(other.y, self.y):
      if i in rows_that_need_expansion:
        totalDistance += expansion_size - 1
    return totalDistance

galaxies = []
for y,l in enumerate(updated_input_lines_for_expansion):
  for x,c in enumerate(l):
    if c == '#':
      galaxies.append(Galaxy(y,x))

totalDistance = 0
for i,galaxy in enumerate(galaxies):
  for otherGalaxy in galaxies[i+1:]:
    #print(str(galaxy.distanceToOther(otherGalaxy)) + str(galaxy) + str(otherGalaxy)) 
    totalDistance += galaxy.distanceToOther(otherGalaxy)
print('Galaxies len:' + str(len(galaxies)))
print(totalDistance)

# part 2

rows_that_need_expansion = []
for y, l in enumerate(current_input_lines):
  if l.find('#') == -1:
    rows_that_need_expansion.append(y)

columns_that_need_expansion = []
for x,c in enumerate(current_input_lines[0]):
  if c == '.':
    allDots = True
    for l in current_input_lines:
      allDots &= (l[x] == '.')
    if allDots:
      columns_that_need_expansion.append(x)

print(rows_that_need_expansion)
print(columns_that_need_expansion)

galaxies = []
for y,l in enumerate(current_input_lines):
  for x,c in enumerate(l):
    if c == '#':
      galaxies.append(Galaxy(y,x))

totalDistance = 0
for i,galaxy in enumerate(galaxies):
  for otherGalaxy in galaxies[i+1:]:
    #print(str(galaxy.distanceToOther(otherGalaxy)) + str(galaxy) + str(otherGalaxy)) 
    totalDistance += galaxy.distanceToOtherWithExpansions(otherGalaxy, columns_that_need_expansion, rows_that_need_expansion, 1000000)
print('Galaxies len:' + str(len(galaxies)))
print(totalDistance)
