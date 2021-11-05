import math
import time
import sys

def checkType(A):
    i = 0
    num = ""
    floatFlag = False
    B = str(A)
    while i < len(B):
        if (ord(B[i]) >= 48 and ord(B[i]) <= 57 or ord(B[i]) == 46 ):
            if(ord(B[i]) == 46):
                floatFlag = True
            num = num+B[i]
        else:
            num = B
            break
        i+=1
    if(i == len(B)):
        if floatFlag:
            num = float(num)
        else:    
            num = int(num)
    return num           


# 01 SELECTION SORT
global diff
diff = 0
def selectionSort(A ,indexArray):
    start = time.time()
    B = A.copy()
    for i in range(len(B)):
        for n in range(i+1,len(B)):
            if B[n] < B[i]:
                B[i] , B[n] = B[n] , B[i]
                indexArray[i] , indexArray[n] = indexArray[n] , indexArray[i]
    end = time.time()
    global diff
    diff = (end - start)
    print(diff)
    return B , indexArray
# 02 INSERTION SORT
def insertionSort(A , indexArray):
    B = A.copy()
    start = time.time()
    for i in range(1, len(B)):
        currentNum = B[i]
        currentIdx = indexArray[i]
        for j in range (i-1 , -1 , -1):
            if (currentNum < B[j]):
                B[j+1] = B[j]
                B[j] = currentNum
                indexArray[j+1] = indexArray[j]
                indexArray[j] = currentIdx
            else :
                B[j+1] = currentNum
                indexArray[j+1] = currentIdx
                break
    end = time.time()
    global diff
    diff = (end - start)
    print(diff)
    return indexArray
# 03 MERGE SORT
def mergeSort(A , a , b , indexArray):
    if a!=b : 
        mid = (a + b) // 2
        copyIndex = indexArray.copy()
        mergeSort(A , a , mid , indexArray)
        mergeSort(A , mid + 1 , b ,indexArray)
        merge(A , a  , mid , b , indexArray)
    return indexArray
def merge(A , a , mid , b , indexArray):
    L = []
    R = []
    Li = []
    Ri = []
    copyIndex = indexArray.copy()
    for i in range(a , mid+1):
        L.append(A[i])
        Li.append(copyIndex[i])
    for i in range(mid+1 , b+1):
        R.append(A[i])
        Ri.append(copyIndex[i])    
    i = a
    j = 0
    k = 0
    while (j < len(L) and k < len(R)):
        if (L[j] < R[k]): 
            indexArray[i] = Li[j]
            A[i] = L[j]

            j+=1
            i+=1
        else:
            A[i] = R[k]
            indexArray[i] = Ri[k]
            k+=1
            i+=1
    while (j < len(L)):
        A[i] = L[j]
        indexArray[i] = Li[j]
        i+=1
        j+=1
    while (k < len(R)):
        indexArray[i] = Ri[k]
        A[i] = R[k]
        k+=1
        i+=1
# 04 BUBBLE SORT

def bubbleSort(A , indexArray):
    a = 0
    j = len(A)-2
    while a < j:
        for i in range(j+1):
            if(A[i] > A[i+1] ):
                indexArray[i],indexArray[i+1] = indexArray[i+1],indexArray[i]
                A[i] , A[i+1] = A[i+1] , A[i]
        j-=1
    return indexArray
# 05 BUCKET SORT
def calculateDivNumber(n):   # calculates the number with which each number will be divided in bucket sort
    tens = "1"
    for i in range(n):
        tens += "0"
    return int(tens)
def bucketSort(A , indexArray):
    B=[[],[],[],[],[],[],[],[],[],[]]
    idx=[[],[],[],[],[],[],[],[],[],[]]
    typechr = checkType(str(A[0]))
    if type(typechr) == str:
        return 0
    maxi = max(A)
    divNum = calculateDivNumber(len(str(maxi)))  # Number with which each number is going to be divided
    for i in range(len(A)):
        floatNum  = A[i]/divNum
        B[math.floor(floatNum*10)].append(A[i]) # Appending numbers in their corresponding buckets
        idx[math.floor(floatNum*10)].append(indexArray[i])
    return allignArray(insertionBucketSort(B , idx))
def allignArray(A):                             # Allign and store the buckets back to original array
    output = [] 
    for r in range(len(A)):
        for c in range(len(A[r])):
            output.append(A[r][c])
    return output
def insertionBucketSort(A , indexArray):
    for i in range(0, len(A)):
        row = A[i]
        irow = indexArray[i]
        insertionSort(row , irow)
    return indexArray

# 06 COUNTING SORT
def key(A, i):              
    ascii = []
    for character in A:
        if type(character) == str:
            ascii.append(ord(character[0]))
        else:
            ascii.append(character)

    return (ascii[i]+(-1*min(ascii)))

def countingSort(A , indexArray):
    A = list(map(str, A))
    copyIdx = indexArray.copy()
    ascii = []
    for character in A:
        typechr = checkType(character)
        if typechr == character :
            ascii.append(ord(character[0]))
        elif type(typechr) == float:
            return 0
        else:
            ascii.append(typechr)
    size = (max(ascii) - min(ascii)) + 1
    count = []
    output = [0]*(len(A)) 
    #  Making an array of size with 0 stored at each place
    for i in range(size+1):
        count.append(0)
    #  counting the occurence of each element
    for i in range(len(A)):
        count[key(ascii,i)]+=1        
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in range(len(A)-1 , -1 , -1):
        count[key(ascii,i)]-=1
        output[count[key(ascii,i)]]= A[i]
        indexArray[count[key(ascii,i)]]= copyIdx[i]

    return indexArray
# 07 RADIX SORT                 not run in case of string and float
def CountingSortforRadix(ascii , index , A , indexArray):
    currentIDXARRAY = []
    sortedarr = [0]*len(ascii)
    copyIndex = indexArray.copy()
    
    for i in range(len(ascii)):
        num = len(str(ascii[i]))
        if(num < A):
            newNum = addZeros(ascii[i] , A)
            currentIDXARRAY.append(int(newNum[index]))
        else:
            newNum = str(ascii[i])
            currentIDXARRAY.append(int(newNum[index]))
    size = (max(currentIDXARRAY) - min(currentIDXARRAY)) + 1
    count = []
    output = [0]*(len(ascii))
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
        # indexArray[key(currentIDXARRAY,i)], indexArray[i] = indexArray[i],indexArray[key(currentIDXARRAY,i)]
        
    for i in range(len(output)):
        sortedarr[output[i]] = ascii[i]
        copyIndex[output[i]] = indexArray[i]
            
    ascii = sortedarr
    indexArray = copyIndex
      
    return ascii ,indexArray 
def key(A , i):
    return(A[i]+(-1*min(A)))
def addZeros(A , digits):
    length = len(str(A))
    diff = digits - length
    for i in range(diff):
        A = "0"+str(A)
    return A
def radixSort(A , indexArray):
    typechr = checkType(A[0])
    ascii = []
    if (type(typechr) == str):
        for i in range(len(A)):
            ascii.append(ord(A[i][0]))
    elif type(typechr) == float:
        return 0
    else:
        ascii = A
    A = len(str(max(ascii)))
    for i in range (A-1,-1,-1):
        ascii ,indexArray = CountingSortforRadix(ascii , i , A, indexArray)
    return(indexArray) 
# 08 QUICK SORT
def quickSort(A , low , high , indexArray):
    # sys.setrecursionlimit(10**9)
    if low < high :
        pi = partition(A , low , high , indexArray)
        quickSort(A , low , pi-1 , indexArray)
        quickSort(A , pi+1 , high , indexArray)
    return indexArray
def partition(A , low , high , indexArray):
    pivot = A[high]
    i = low
    for j in range (low , high):
        if (A[j]<pivot):
            A[i] , A[j] = A[j],A[i]
            indexArray[i] , indexArray[j] = indexArray[j],indexArray[i]
            i+=1
    A[high] = A[i]
    indexArray[high] , indexArray[i] = indexArray[i] , indexArray[high]
    A[i] = pivot
    return i
# 09 HEAP SORT
def maxHeapify(A, n, i , indexArray):
    largest = i 
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child
    if left < n and A[largest] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        indexArray[i], indexArray[largest] = indexArray[largest], indexArray[i]
        maxHeapify(A, n, largest , indexArray)
def heapSort(A , indexArray):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(A, n, i , indexArray)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        indexArray[i], indexArray[0] = indexArray[0], indexArray[i] 
        maxHeapify(A, i, 0 , indexArray)
    return indexArray    
# 10 PIGEONHOLE SORT
def pigeonselectionSort(A , ridx):
    for i in range(len(A)):
        for n in range(i+1,len(A)):
            if A[n] < A[i]:
                new =  A[i]
                A[i] = A[n]
                A[n] = new
                ridx[i] , ridx[n] = ridx[n] , ridx[i]
    return A , ridx
def pigeonholeSort(A , indexArray):         
    ascii = []
    floatType = False

    for character in A:
        typechr = checkType(character)
        if type(typechr) == str :
            ascii.append(ord(character[0]))
        elif type(typechr) == float:
            # return 0
            ascii.append(typechr)
            floatType = True
        else:
            ascii.append(typechr)
    maxi = math.floor(max(ascii))
    mini = math.floor(min(ascii))
    rangeSize = maxi - mini + 1
    pHoles = [[] for j in range(rangeSize)]
    pHolesidx = [[] for j in range(rangeSize)]
       
    for i in range (len(A)):
        idx = math.floor(ascii[i] - mini)
        pHoles[idx].append(A[i])
        pHolesidx[idx].append(indexArray[i])
        
    i = 0
    for r in range(len(pHoles)):
        row = pHoles[r]
        rowidx = pHolesidx[r]
        if floatType:
            row , rowidx= pigeonselectionSort(row , rowidx)
        for c in range(len(row)):
            A[i] = row[c]
            indexArray[i] = rowidx[c]
            i+=1
    return indexArray        
A = [0.4,0.234,5.2,7.3,1.5,0.1]
indexArray = [0,1,2,3,4,5]
print(pigeonholeSort(A , indexArray))
# 11 SHELL SORT
def shellSort(A , indexArray):
    n = len(A)
    gap = n//2

    while gap > 0:
        i = 0
        k = gap

        while k < n:
            if A[i] > A[k]:
                A[i],A[k] = A[k],A[i]
                indexArray[i],indexArray[k] = indexArray[k],indexArray[i]
            i += 1
            k += 1
            j = i
            while j-gap > -1:
                if A[j-gap] > A[j]:
                    A[j-gap],A[j] = A[j],A[j-gap]
                    indexArray[j-gap],indexArray[j] = indexArray[j],indexArray[j-gap]
                j -= 1
        gap = gap // 2
    return indexArray                        
# 12 COMB SORT
def combSort (A , indexArray) :
    gap = len(A)
    while gap != 1 :
        gap = gap/1.3
        gap = int(gap)
        for i in range ( 0, len(A)-gap ) :
            if A[i] > A[i+gap] :
                A[i] , A[i+gap] = A[i+gap] , A[i] 
                indexArray[i] , indexArray[i+gap] = indexArray[i+gap] , indexArray[i] 
               
    return indexArray
# 13 GNOME SORT 
def gnomeSort (A , indexArray ) :
    i = 0
    while i < len(A) :
        if i == 0 :
            i += 1
        if A[i] >= A[i-1] :
            i+= 1
        else :
            
            A[i] , A[i-1] = A[i-1],A[i]
            indexArray[i] , indexArray[i-1] = indexArray[i-1],indexArray[i]
            i -= 1
    return indexArray

