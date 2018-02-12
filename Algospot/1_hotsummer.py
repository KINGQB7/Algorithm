building = int(input())
for i in range(building):
    #print(i+1, "/", building)
    goal = int(input())
    consumption= input()
    division = map(int, consumption.split())
    #print("Goal: ", goal)
    total = sum(division)
    #print("Total: ", total)
    if goal>=total:
      print("YES")
    else:
      print("NO")