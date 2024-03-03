#With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 5:
    continue
  print(i)