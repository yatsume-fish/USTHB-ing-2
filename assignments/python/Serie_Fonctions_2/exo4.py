my_list = [2, 45, 654, 348, 153, 657, 153, 94, 62, 357, 476, 123]
check = int(input("check if this number is in list: "))

def existe(l, x):
  is_real = x in l

  return is_real

print(existe(my_list, check))