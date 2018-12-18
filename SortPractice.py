import timeit
import random
import time
#creates a group of random integers that must be sorted and benchmarks them
def generator(n):
    m = []
    while n > 0:
        m = random.randrange(1000)
        n = n -1
        
    return m
        
def bubbles(m):
    for passnum in range(len(m)-1,0,-1):
        for i in range(m):
            if m[i] > m[i+1]:
                temp = m[i]
                m[i] = m[i+1]
                m[i+1] = temp
                
    print(bubbles(m))

def selection(m):
   for f range(len(m)-1,0,-1):
       Max=0

       for x in range(1,f+1):

           if m[x]> m[Max]:
               Max = x

       temp = m[f]
       m[f] = m[Max]
       m[Max] = temp

    print(selection(m))
    
def insertion(m):
   for i in range(1,len(m)):
     c = m[i]
     x = i

     while x>0 and m[x-1] > c:
         m[x]=m[x-1]
         x = x-1

     m[x]=c
     print(insertion(m))

       
def gap(m):
    for i in range(0,len(m),3):

        currentvalue = m[i]
        x = i

        while x >= 0 and m[x - 3]> currentvalue:
            m[x]= m[x - 3]
            x = x - 3

        m[x]=currentvalue

    print(gap(m))

def mergeSort(m):
    print("Splitting ",m)
    if len(alist)>1:
        mid = len(m)//2
        lefthalf = m[:mid]
        righthalf = m[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                m[k]=m[i]
                i=i+1
            else:
                m[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            m[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            m[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",m)

mergeSort(m)
print(m)

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
    
        
    
