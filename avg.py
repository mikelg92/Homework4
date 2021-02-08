def calAvg(num):
  sumNum = 0
  for t in num:
    sumNum = sumNum + t

  avg = sumNum / len(num)
  return avg

print("The average: ", calAvg([18,25,3,41,5]))
