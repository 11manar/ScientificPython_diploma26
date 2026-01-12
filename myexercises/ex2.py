def recaman_sequence(n):
  a0 = 0
  ls = [a0]
  for i in range(n):
    num1 = ls[i] - (i+1)
    num2 = ls[i] + (i+1)
    if (num1 > 0) and (num1 not in ls):
      ls.append(num1)
    else:
      ls.append(num2)   
  return ls

n = int(input("Enter an integer number: "))
seq = recaman_sequence(n)
print(seq)
