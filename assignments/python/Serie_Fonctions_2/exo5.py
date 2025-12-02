my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
long_list = [2, 45, 654, 348, 153, 657, 153, 94, 62, 357, 476, 123]



def pair(l):
  compt = 0
  for i in l:
    if i % 2 :
      compt += 1 
  return compt

print(pair(my_list))
print(pair(long_list))