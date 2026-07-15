class Solution:
    def countPrimes(self, n: int) -> int:
        arr =[True] *n
        if n<=2:
            return 0
        arr[0],arr[1]=False,False
        for i in range(2,int(n ** 0.5 )+1):
            if arr[i]:
                for j in range(i*i,n,i):
                    arr[j]=False
        ans=sum(arr)
        return ans



        