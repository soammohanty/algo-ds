# Bubble Sort 
# So here we swap each element if its NOT sorted and will not swap if already sorted like -
# [8,5,2,7,5,9,1] -> [5,8,2,7,5,9,1] -> [5,2,8,7,5,9,1] -> [5,2,7,8,5,9,1] -> [5,2,7,5,8,9,1] 
# -> [5,2,7,5,8,9,1] -> [5,2,7,5,8,1,9]
# After all these swaps, last element is the LARGEST element i.e 9 . 
# So now we will sort entire array again excluding last element i.e 9 as we know its already at its right place
#i.e iterate again on [5,2,7,5,8,1]

# So after next round of iteration [.....8, 9] 
# Similary [...7,8,9] -> [...5,7,8,9] -> [..5,5,7,8,9]-> [1,2,5,5,7,8,9]

# Space complexity: O(1)
# Time complexity: O(n^2)

arr = [8,5,2,7,5,9,1]

def swapIt(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]
    
def bubbleSort(arr):
    arraySorted = False
    
    while not arraySorted:
        arraySorted = True
        for i in range(len(arr) - 1):  # -1 to avoid indexOutBound because we swap element to next one.
            if arr[i] > arr[i+1]:
                swapIt(i,i+1,arr)
                arraySorted = False
                
    return arr

#print(bubbleSort(arr))  

# As we know last element is always sorted. So lets not compare last element in every loop

def improvedBubbleSort(arr):
    arraySorted = False
    couter = 0
    while not arraySorted:
        arraySorted = True
        for i in range(len(arr) - 1 - couter):  # -counter for not to compare last element
            if arr[i] > arr[i+1]:
                swapIt(i,i+1,arr)
                arraySorted = False
                
        couter += 1
        
    return arr

print(improvedBubbleSort(arr)) 
    



    
    