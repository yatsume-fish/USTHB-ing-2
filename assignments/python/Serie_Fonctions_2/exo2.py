my_list = [1, 5, 6784, 245, 65424, 6547, 8765, 24, 343, 5878, 453, 687, 654, 54]

def max_list(l):
  max_number = l[0]
  for i in l:
    if i > max_number:
      max_number = i
  return max_number

print(max_list(my_list))