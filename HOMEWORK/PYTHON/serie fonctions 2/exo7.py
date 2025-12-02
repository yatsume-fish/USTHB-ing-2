my_list = [1, 2, 3, 4]
long_list = [1, 5, 6784, 245, 65424, 6547, 8765, 24, 343, 5878, 453, 687, 654, 54]

def compter(l):
  compt = 0
  for i in l:
    compt += 1
  return compt

def somme_liste(l):
  total_sum = 0
  for i in l:
    total_sum = total_sum + i
  return total_sum

def moyenne(l):
  mean = somme_liste(l) / compter(l)
  return mean

print(moyenne(my_list))
print(moyenne(long_list))