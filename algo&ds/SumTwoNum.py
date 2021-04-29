# Sum of two numbers should be equal to target value
arr = [10,20,30,25,22,44,1]
sum = 45        

#################################################################

# 1st Approch
# Space Complexity O(1)
# Time Complexity O(n²)

def sumOfTwoNumbers(arr,targetSum):
    for i in range(0,len(arr)-1):         #from first to 2nd last element
        firstNum = arr[i]           
        for j in range(i+1,len(arr)):     #from next of i to last element
            secondNum = arr[j]
            if(firstNum + secondNum == targetSum):
                print('%d and %d sum is %d'%(firstNum,secondNum,targetSum))
        
#sumOfTwoNumbers (arr,sum)         

#################################################################

# 2nd Approch
# Space Complexity O(n). #As hash table used i.e Dictonary
# Time Complexity O(n)

def sumOfTwoNumbersUsingHashTable(arr,targetSum):
     numSeen = {} # Dictonary
     
     for num in arr:
         if targetSum - num in numSeen:         #if number is in hashtable whose sum = targetSum
             print('%d and %d sum is %d'%(num,targetSum-num,targetSum))
         else:
             numSeen[num]= True         #Add the num in the hash table
             
             
#sumOfTwoNumbersUsingHashTable(arr,sum)

#################################################################
# 2nd Approch
# Space Complexity O(1)
# Time Complexity O(nlog(n))

def sumOfTwoNumbersUsingSort(arr,targetSum):
    arr.sort()           #sort() has been using the Timsort. Complexity : O(n.logn)
    left = 0             #It will go towards right
    right = len(arr)-1   #It will go towards left
    
    while left < right:
        presentSum = arr[left] + arr[right]
        if presentSum == targetSum:
            return[arr[left], arr[right]]
        elif presentSum < targetSum:        
            left += 1           #since presentSum is less, we need to increase it. So move towards right
        else:
            right -= 1          #since presentSum is more, we need to decrease it. So move towards left
    return ['No match']      
    
print(sumOfTwoNumbersUsingSort(arr,sum))


