# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.

# Return the number of good triplets.

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        numlen = len(arr)
        gt = 0
        
        for i in range(0, numlen-2):
            for j in range(i+1, numlen-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, numlen):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    elif abs(arr[i] - arr[k]) > c:
                        continue
                    else:
                        gt += 1
        return gt