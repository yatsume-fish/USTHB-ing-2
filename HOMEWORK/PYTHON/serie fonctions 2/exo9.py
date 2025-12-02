my_list = [23, 54, 635, 78, 321, 69, 8, 7, 42321, 456, 86, 2, 432, 54, 78, 698, 63, 5]

limit = int(input("entrez le seuil: "))

def filtre(l, seuil):
  new_list = list()
  for i in l:
    if i > seuil:
      new_list.append(i)
  return new_list

print(filtre(my_list, limit))