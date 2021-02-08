def calAvg(num):
  sumNum = 0
  for t in num:
    sumNum = sumNum + t

  avg = sumNum / len(num)
  return avg

while True:
    try:
        a = float(input("enter number: "))
        b = float(input("enter number: "))
        c = float(input("enter number: "))
        d = float(input("enter number: "))
        e = float(input("enter number: "))
        break
    except ValueError:
        print("invalid number, only positive numbers.")

print("The average: ", calAvg([a,b,c,d,e]))
