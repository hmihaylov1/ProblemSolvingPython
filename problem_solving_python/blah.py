#def sum(n):
 #   s = 0
 #   for i in range(1, n + 1):
 #       s += i*i
  #  return s


#print(sum(4))

def sum(n):
    if n == 1:
        return 1
    #Base Case
    else:
        return pow(n, n) + sum(n - 1)
    #Recursive Step


print(sum(3))