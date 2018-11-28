#Given a list of numbers and a number k, 
#return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def solve(numbers,k):
    for n in range(0,len(numbers)-1):
        for m in range(n+1,len(numbers)):
            if (numbers[n]+numbers[m]) == k:
                return True
    return False

def solve_improved(numbers,k):
    pairs={}
    for num in numbers:
        if num in pairs.keys():
            return True
        pairs[k-num]=1

    return False


print solve([10, 15, 3, 7],17)
print solve([10, 15, 3, 8],17)

print solve_improved([10, 15, 3, 7],17)
print solve_improved([10, 15, 3, 8],17)