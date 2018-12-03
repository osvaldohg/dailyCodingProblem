
# Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def solve(numbers):
    numbers.sort()
    index=1

    for i in range(0,len(numbers)):
        if numbers[i]>0:
            if numbers[i]==index:
                if i+1 < len(numbers):
                    if numbers[i+1]!=index:
                        index+=1
                else:
                    index+=1
            else:
                return index
            
    return index
    
def test_solve():
    assert solve([3, 4, -1, 1]) == 2
    assert solve([1, 2, 0]) == 3
    assert solve([2, 3, 7, 6, 8, -1, -10, 15]) == 1
    assert solve([2, 3, -7, 6, 8, 1, -10, 15]) == 4
    assert solve([1, 1, 0, -1, -2]) == 2
    assert solve([-1,-2,0,3]) == 1
    assert solve([-1,-2,0,1]) == 2
    assert solve([-1,-2,0,1,1,2,2]) == 3
    assert solve([-1,-2,0,1,1,3,3]) == 2
