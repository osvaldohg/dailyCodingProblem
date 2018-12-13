#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#Follow-up: Can you do this in O(N) time and constant space?


def solution(numbers):
    exc=0
    inc=0

    for i in range(0,len(numbers)):
        temp=inc
        inc=max(exc+numbers[i],inc)
        exc=temp

    return inc


print solution([-2,4,6,2,5])#13
print solution([5,1,1,5])#10
print solution([5,5,10,100,10,5])#110
print solution ( [-5, -5, -5, 10, -5])#10