'''
def rotation(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    new_nums = [0]*n
    
    for i in range(n):
        new_index = (i + k) % n
        new_nums[new_index] = nums[i]
    
    return new_nums
a = list(map(int,input().split()))
k = int(input())
a = rotation(a,k)
print(a)
# time complexity: O(n) space complexity: O(n)
'''

'''
def rotation(nums,k):
    n = len(nums)
    if n == 0:
        return nums
    k = k%n 
    for _ in range(k):
        m = nums[-1]
        for i in range(n-1,0,-1):
            nums[i] = nums[i-1]
        nums[0] = m
    return nums
a = list(map(int,input().split()))
k = int(input())
a = rotation(a,k)
print(a)
# time complexity: O(n*k) space complexity: O(1)
'''

def rotation(nums,k):
    n = len(nums)
    if n == 0:
        return nums
    k = k%n 
    def reverse(nums,start,end):
        while start<end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums
a = list(map(int,input().split()))
k = int(input())
a = rotation(a,k)
print(a)
# time complexity: O(n) space complexity: O(1)

'''
1. the optimal time complexity is O(n) when we choose the first and third method since each element must be accessed at least once, the second method has a time complexity of O(n*k) which is not optimal when k is large.
2. when we choose the second method, the time complexity is O(n*k) so if k is large, the time taken will be significantly higher than the first and third method which have a time complexity of O(n).
3. The temporary array method is preferred for simplicity, the one-by-one method for small k, and the reverse method for performance-critical scenarios.
'''