class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        i=5
        for _ in range(n):
            if i>n:
                break
            count+=n//i
            i*=5
        return count



        