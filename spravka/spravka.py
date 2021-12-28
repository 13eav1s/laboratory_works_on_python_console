import random as r

def selectionsort(arr): #Сортировка выбором
    for i in range(len(arr)):
        minind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minind]:
                minind = j
        arr[i],arr[minind] = arr[minind],arr[i]
    return arr


def bubblesort(arr): #Пузырьковая сортировка
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(i,' : ', *arr)
    return arr


def bubblesortwithflag(arr): #Пузырек с флагом
    n = len(arr)
    for i in range(n-1):
        flag = True
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = False
        if flag:
            break
        print(i,' : ', *arr)
    return arr


def shakersort(arr): #Шейкер-сортировка
    left = 0
    right = len(arr) - 1
    print(left, right)
    while left < right:
        r_new = left
        for i in range(left,right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                r_new = i
            right = r_new
            print(*arr, ' | ', left, right)
            l_new = right
            for i in range(right - 1, left - 1, -1):
                if (arr[i] > arr[i+1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    l_new = i
            left = l_new
        print(*arr, ' | ', left, right)
    return arr

def insertionsort(arr): #Сортировка вставками

    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while (j >= 0 and cur < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = cur
        print(i,' : ', arr[:i], ' | ', arr[i:])
    return arr

def insertionsortwithbarrier(arr): #Вставками с барьером
    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[0] = arr[i]
        j = i - 1
        while (arr[0] < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = arr[0]
    print(i,' : ', arr[:i], ' | ', arr[i:])
    return arr[1:]


def insertionsortwithbinsearch(arr): #Вставками с бинарным поиском

    for i in range(1, len(arr)):
        cur = arr[i]
        lo = 0
        hi = i
        if lo == hi:
            lo += 1
        else:
            while lo < hi:
                mid = (lo + hi)//2
                if cur < arr[mid]: hi = mid
                else:
                    lo = mid + 1
        j = i
        while (j > lo and j > 0):
            arr[j] = arr[j-1]
            j = j - 1
        arr[lo] = cur
    return arr


def shellSort(data, length):
        gap = length//2
        while gap > 0:
            for iIndex in range(gap, length):
                temp = data[iIndex]
                jIndex = iIndex
                while jIndex >= gap and data[jIndex - gap] > temp:
                        data[jIndex] = data[jIndex - gap]
                    jIndex -= gap
                data[jIndex] = temp
            gap //= 2
        return data


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

# еще один тип квиксорта
def different_quicksort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[r.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


def sort_file(filename, size):              #сортировка вставкой бинарного файла
    with open(filename, 'rb+') as f:
        lines = getsize(filename) // size
        for i in range(1, lines):
            f.seek(size*i)
            cur = struct.unpack('q', f.read(size))[0]
            j = i-1
            f.seek(size*j)
            n = struct.unpack('q', f.read(size))[0]
            while j >= 0 and cur < n:
                f.write(struct.pack('q',n))
                j -= 1
                f.seek(size*(j+1))
                f.write(struct.pack('q', cur))
                if j >= 0:
                    f.seek(size*j)
                    n = struct.unpack('q', f.read(size))[0]


a = [-1,2,55,-2,-3,69]

b = quicksort(a,0,len(a))
print(b)
