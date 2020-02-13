
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np


nPut = int(input("Enter The number of terms: ")) 
nterms =  nPut

exTimer = []

def fibo_rec(n):

   if n <= 1:
       return n
   else:
       return(fibo_rec(n-1) + fibo_rec(n-2))

if nterms <= 0:
   print("Negative Integers is not allowed")

else:
   print("Fibonacci sequence:")

for i in range(nterms):
    print(fibo_rec(i))

start = timer()
res = fibo_rec(nterms)
end = timer()

fib1_time = end-start
exTimer.append(fib1_time)
print ( "The "+ str(nPut)+"th term is "+ str(res))
print("recursion time: ", fib1_time)


print("\n")

def fibo_Iter():
    start = timer()

    i = 1
    if nPut == 0:
        fib = []
    elif nPut == 1:
        fib = [1]
    elif nPut == 2:
        fib = [1,1]
    elif nPut > 2:
        fib = [1,1]
        while i < (nPut - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
    

res = (fibo_Iter())
end = timer()
result = (res[nPut-1])

fib2_time = end-start
exTimer.append(fib2_time)

print("Fibonacci sequence:")
print(res)

print( "The "+ str(nPut)+"th term is "+ str(result))
print("iteration time: ", fib2_time)

print("\n")


def fibo_better():
  start = timer()
  n = 0
  a = 0
  b = 1
  number =[]
  while(n<nterms):
    if ( n <= 1 ):
      number= n
      n+=1
    else:
      number = a + b
      a = b
      b = number
      n+=1
      print(number)

print("Fibonacci sequence:")
fibo_better()
end = timer()

fib3_time = end-start
exTimer.append(fib3_time)

print( "The "+ str(nPut)+"th term is "+ str(result))
print("Other Method time: ", fib3_time)

print("\n")

print("Timer:")
print(exTimer)

names = ['recursion', 'Iternate', 'Other']
values = [exTimer[0], exTimer[1], exTimer[2]]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Execution Time')
plt.show()