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

print solution([1,2,3,4,5])
print solution([3,2,1])
print solution([10, 3, 5, 6, 2])