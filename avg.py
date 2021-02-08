def calAvg(num):
  sumNum = 0
  for t in num:
    sumNum = sumNum + t

  avg = sumNum / len(num)
  return avg


a = float(input("enter number: "))
b = float(input("enter number: "))
c = float(input("enter number: "))
d = float(input("enter number: "))
e = float(input("enter number: "))

print("The average: ", calAvg([a,b,c,d,e]))
