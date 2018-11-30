#Given an array of integers, return a new array such that each element at 
#index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], 
#the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def solution(numbers):
    ans=[]
    total=1

    for num in numbers:
        total=total*num
    
    for num in numbers:
        ans.append(total/num)
    
    return ans

#not using division
def improved_solution(numbers):
    left=[1 for i in range(len(numbers))]
    right=[1 for i in range(len(numbers))]
    prod=[]

    for i in range(1,len(numbers)):
        left[i]=numbers[i-1]*left[i-1]
        
    
    for i in range(len(numbers)-2,-1,-1):
        right[i]=numbers[i+1]*right[i+1]

    for i in range(0,len(left)):
        prod.append(left[i]*right[i])

    return prod

print solution([1,2,3,4,5])
print solution([3,2,1])
print solution([10, 3, 5, 6, 2])

print improved_solution([1,2,3,4,5])
print improved_solution([3,2,1])
print improved_solution([10, 3, 5, 6, 2])