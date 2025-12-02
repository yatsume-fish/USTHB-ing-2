my_list = ["banana", "orange", "apple", "grapes", "figs"]
long_list = ["transistor", "diode", "capacitor", "resistor", "wire", "PCB", "solder", "coil", "oscilloscope", "LED"]


def compter(l):
  compt = 0
  for i in l:
    compt += 1
  return compt

print(compter(my_list))
print(compter(long_list))