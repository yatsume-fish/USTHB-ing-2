num = int(input("donnez n pour avoir sa table de multiplication: "))

def table(n):
  for i in range(11):
    product = n * i
    print(n, "x", i, "=", product)

table(num)