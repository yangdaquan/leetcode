'''
1 Array Partition I
'''


class Solution(object):
    def arrayPairSum(self, nums):
        sum = 0

        sort_nums = sorted(nums)
        for x in sort_nums[::2]:
            sum += x

        return sum


l1 = [1, 4, 3, 2, 6, 8, 10, 44]
s = Solution()
print('s.arrayPairSum', s.arrayPairSum(l1))

# sum(sorted(nums[::2]))

'''
2 Toeplitz Matrix	
'''


class Solution(object):
    def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True


m = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
s = Solution()
print('s.arrayPairSum', s.isToeplitzMatrix(m))

# all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0]))-1)

'''
3 Reshape the Matrix
'''


def matrixReshape(nums, r, c):
    if len(nums) * len(nums[0]) == r * c:
        new_nums = []
        for m in nums:
            new_nums.extend(m)

        result = []
        if r > 1 and c > 1:
            for i in range(r):
                result.append(new_nums[i * c: (i + 1) * c])
        else:
            return [new_nums]
    else:
        return nums


nums = [[1, 2], [3, 4]]
r = 1
c = 4
print('matrixReshape', matrixReshape(nums, r, c))


import numpy as np

def reshape(nums, r, c):
    try:
        return np.reshape(nums, (r, c)).tolist()
    except:
        return nums

print('reshape', reshape(nums, r, c))

