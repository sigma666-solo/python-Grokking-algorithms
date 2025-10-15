def findSmallest(arr):

    smallest=arr[0]#для хранения наименьшего значения
    smallest_index=0#для хранения индекса наименьшего значения

    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort (arr):

    newArr =[]
    
    for i in range(len(arr)):

        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort ([5,2,3,1,4]))

