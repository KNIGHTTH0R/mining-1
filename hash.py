#!/usr/bin/python3

total = 0;
count = 0;

while (True):
  x = input("Paste here:");
  tokens = x.split()
  print(tokens)
  try:
    i = tokens.index("H/s")
    y = int(tokens[i-1])
    total += y
    print("Total %s" % total)
    count += 1
  except ValueError as e:
    print(e)
  if (len(tokens) == 0):
    break

print("Avg: %3.3f" % (total / ((10.0**6)* count)))

