my_list = [1, 2, 3, 4]
long_list = [1, 5, 6784, 245, 65424, 6547, 8765, 24, 343, 5878, 453, 687, 654, 54]

def somme_liste(l):
  total_sum = l[0]
  for i in l:
    total_sum = total_sum + i - 1
  return total_sum

print(somme_liste(my_list))
print(somme_liste(long_list))