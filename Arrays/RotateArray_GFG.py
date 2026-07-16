# Problem: Rotate Array
# Platform: Geeks For Geeks
# URL: https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1
# Difficulty: Medium
class Solution:
    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        def reversee(arr,left,right):
            while left<right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        reversee(arr,0,d-1)
        reversee(arr,d,n-1)
        reversee(arr,0,n-1)
            