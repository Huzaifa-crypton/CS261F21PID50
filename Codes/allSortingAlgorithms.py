import math
# 01 SELECTION SORT
def selectionSort(A):
    for i in range(len(A)):
        for n in range(i+1,len(A)):
            if A[n] < A[i]:
                new =  A[i]
                A[i] = A[n]
                A[n] = new
    return A
# 02 INSERTION SORT
def insertionSort(A):
    for i in range(1, len(A)):
        currentNum = A[i]
        for j in range (i-1 , -1 , -1):
            if (currentNum < A[j]):
                A[j+1] = A[j]
                A[j] = currentNum
            else :
                A[j+1] = currentNum
                break
    return A
# 03 MERGE SORT
def mergeSort(A , a , b):
    if a!=b : 
        mid = (a + b) // 2
        mergeSort(A , a , mid)
        mergeSort(A , mid + 1 , b)
        merge(A , a  , mid , b)
    return A
def merge(A , a , mid , b):
    L = []
    R = []
    for i in range(a , mid+1):
        L.append(A[i])
    for i in range(mid+1 , b+1):
        R.append(A[i])    
    i = a
    j = 0
    k = 0
    while (j < len(L) and k < len(R)):
        if (L[j] < R[k]): 
            A[i] = L[j]
            j+=1
            i+=1
        else:
            A[i] = R[k]
            k+=1
            i+=1
    while (j < len(L)):
        A[i] = L[j]
        i+=1
        j+=1
    while (k < len(R)):
        A[i] = R[k]
        k+=1
        i+=1
# 04 BUBBLE SORT
def bubbleSort(A):
    a = 0
    j = len(A)-2
    while a < j:
        for i in range(j+1):
            if(A[i] > A[i+1] ):
                y = A[i]
                A[i] = A[i+1]
                A[i+1] = y
        j-=1
    return A
# 05 BUCKET SORT
def calculateDivNumber(n):   # calculates the number with which each number will be divided in bucket sort
    tens = "1"
    for i in range(n):
        tens += "0"
    return int(tens)
def bucketSort(A):
    B=[[],[],[],[],[],[],[],[],[],[]]
    maxi = max(A)
    divNum = calculateDivNumber(len(str(maxi)))  # Number with which each number is going to be divided
    for i in range(len(A)):
        floatNum  = A[i]/divNum
        B[math.floor(floatNum*10)].append(A[i]) # Appending numbers in their corresponding buckets
    return allignArray(insertionBucketSort(B))
def allignArray(A):                             # Align and store the buckets back to original array
    output = [] 
    for r in range(len(A)):
        for c in range(len(A[r])):
            output.append(A[r][c])
    return output
def insertionBucketSort(A):
    for i in range(0, len(A)):
        row = A[i]
        insertionSort(row)
    return A
A=[110, 45, 65,50, 90,602, 24, 2, 66]
print(bucketSort(A))
# 06 COUNTING SORT
def key(A, i):              
    ascii = []
    for character in A:
        if type(character) == str:
            ascii.append(ord(character[0]))
        else:
            ascii.append(ord(character))

    return (ascii[i]+(-1*min(ascii)))
def checkType(A):
    i = 0
    num = ""
    while i < len(A):
        b = ord(A[i])
        if (ord(A[i]) >= 48 and ord(A[i]) <= 57 or ord(A[i]) == 46 ):
            num = num+A[i]
        else:
            num = A
            break
        i+=1
    if(i == len(A)):
        num = int(num)
    return num           
def countingSort(A):

    ascii = []
    for character in A:
        type = checkType(character)
        if type == character :
            ascii.append(ord(character[0]))
        else:
            asc = 0
            power = len(character)-1
            for i in character:
                a = ord(i) - 48
                asc += a *10**(power)
                power -= 1
            ascii.append(asc)

    size = (max(ascii) - min(ascii)) + 1
    count = []
    output = [0]*(len(A)) 
    #  Making an array of size with 0 stored at each place
    for i in range(size+1):
        count.append(0)
    #  counting the occurence of each element
    for i in range(len(A)):
        count[key(A,i)]+=1        
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in range(len(A)-1 , -1 , -1):
        count[key(A,i)]-=1
        output[count[key(A,i)]]= A[i]
    return output
# 07 RADIX SORT
def CountingSortforRadix(A , index , maximum):
    currentIDXARRAY = []
    sortedarr = [0]*len(A)
    for i in range(len(A)):
        num = len(str(A[i]))
        if(num < maximum):
            newNum = addZeros(A[i] , maximum)
            currentIDXARRAY.append(int(newNum[index]))
        else:
            newNum = str(A[i])
            currentIDXARRAY.append(int(newNum[index]))
    size = (max(currentIDXARRAY) - min(currentIDXARRAY)) + 1
    count = []
    output = [0]*(len(A))
    #  Making an array of size with 0 stored at each place
    for i in range(size+1):
        count.append(0)
    #  counting the occurence of each element
    for i in range(len(currentIDXARRAY)):
        count[key(currentIDXARRAY,i)]+=1        
    
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in range(len(currentIDXARRAY)-1 , -1 , -1):
        count[key(currentIDXARRAY,i)] -= 1
        output[i] = count[key(currentIDXARRAY,i)] 
    for i in range(len(output)):
        sortedarr[output[i]] = A[i]
    A = sortedarr    
    return(A)
def key(A , i):
    return(A[i]+(-1*min(A)))
def addZeros(A , digits):
    length = len(str(A))
    diff = digits - length
    for i in range(diff):
        A = "0"+str(A)
    return A
def radixSort(A):
    maximum = len(str(max(A)))
    for i in range (maximum-1,-1,-1):
        A = CountingSortforRadix(A , i , maximum)
    return(A)    
# 08 QUICK SORT
def quickSort(A , low , high):
    if low < high :
        pi = partition(A , low , high)
        quickSort(A , low , pi-1)
        quickSort(A , pi+1 , high)
    return A
def partition(A , low , high):
    pivot = A[high]
    i = low
    for j in range (low , high):
        if (A[j]<pivot):
            y = A[i]
            A[i] = A[j]
            A[j] = y
            i+=1
    A[high] = A[i]
    A[i] = pivot
    return i
# 09 HEAP SORT
def maxHeapify(A, n, i):
    largest = i 
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child
    if left < n and A[largest] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, n, largest)
def heapSort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i] 
        maxHeapify(A, i, 0)
    return A    
# 10 PIGEONHOLE SORT
def pigeonholeSort(A):         
    ascii = []
    for character in A:
        type = checkType(character)
        if type == character :
            ascii.append(ord(character[0]))
        else:
            ascii.append(int(character))
    maxi = max(ascii)
    mini = min(ascii)
    rangeSize = maxi - mini + 1
    pHoles = [[] for j in range(rangeSize)]   
    for i in range (len(A)):
        idx = ascii[i] - mini
        pHoles[idx].append(A[i])
    i = 0
    for r in range(len(pHoles)):
        row = pHoles[r]
        for c in range(len(row)):
            A[i] = row[c]
            i+=1
    return A         
# 11 SHELL SORT
def shellSort(A):
    n = len(A)
    gap = n//2

    while gap > 0:
        i = 0
        k = gap

        while k < n:
            if A[i] > A[k]:
                A[i],A[k] = A[k],A[i]
            i += 1
            k += 1
            j = i
            while j-gap > -1:
                if A[j-gap] > A[j]:
                    A[j-gap],A[j] = A[j],A[j-gap]
                j -= 1
        gap = gap // 2
    return A                        
# 12 COMB SORT
def combSort ( A ) :
    gap = len(A)
    while gap != 1 :
        gap = gap/1.3
        gap = int(gap)
        for i in range ( 0, len(A)-gap ) :
            if A[i] > A[i+gap] :
                temp = A[i+gap]
                A[i+gap] = A[i]
                A[i] = temp
    return A
# 13 GNOME SORT 
def gnomeSort ( A ) :
    i = 0
    while i < len(A) :
        if i == 0 :
            i += 1
        if A[i] >= A[i-1] :
            i+= 1
        else :
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
            i -= 1
    return A

