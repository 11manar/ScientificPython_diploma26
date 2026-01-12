import time

#1st
start = time.time()
list_1 = []
i = 0
while (i < 1000):
  if (i % 3 == 0):
    list_1.append(i)
  i = i + 1
end = time.time()
print("Naive loop time:", end - start)

#2nd
start = time.time()
lst = [list_2 for list_2 in range(1000) if list_2%3==0]
end = time.time()
print("List comprehension time:", end - start)

#3rd
start = time.time()
numbers = list(range(1000))
list_3 = numbers[0:1000:3]
end = time.time()
print("Slicing time:", end - start)

#4th
start = time.time()
list_4 = list(range(0, 1000, 3))
end = time.time()
print("Range step time:", end - start)

  
