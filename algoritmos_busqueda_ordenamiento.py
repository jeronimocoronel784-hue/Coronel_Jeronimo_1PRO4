'''-------------------------
MÉTODOS DE ORDENAMIENTO
------------------------- '''

# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 2. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 4. Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge ordenado
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Elementos restantes
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


'''-------------------------
MÉTODOS DE BÚSQUEDA
------------------------- '''

# 1. Búsqueda Lineal
def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # devuelve el índice
    return -1  # no encontrado


# 2. Búsqueda Binaria
def busqueda_binaria(arr, x):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        mid = (inicio + fin) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            inicio = mid + 1
        else:
            fin = mid - 1

    return -1  # no encontrado