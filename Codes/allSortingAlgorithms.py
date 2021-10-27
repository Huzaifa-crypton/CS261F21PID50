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
# 05 BUCKET SORT
def bucketSort(A):
    B=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(A)):
        B[math.floor(A[i]*10)].append(A[i])
    return allignArray(insertionSort(B))
def allignArray(A):
    output = []
    for r in range(len(A)):
        for c in range(len(A[r])):
            output.append(A[r][c])
    return output
# 06 COUNTING SORT
def countingSort(A):
    size = (max(A) - min(A)) + 1
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
# 10 PIGEONHOLE SORT
def piegeonholeSort(A):
    maxi = max(A)
    mini = min(A)
    rangeSize = maxi - mini + 1
    pHoles = [[] for j in range(rangeSize)]   
    for i in range (len(A)):
        idx = A[i] - mini
        pHoles[idx].append(A[i])
    i = 0
    for r in range(len(pHoles)):
        row = pHoles[r]
        for c in range(len(row)):
            A[i] = row[c]
            i+=1
    return A          
# 11 SHELL SORT
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

