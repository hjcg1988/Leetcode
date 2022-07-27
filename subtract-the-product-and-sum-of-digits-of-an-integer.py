class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        pod=1
        sod=0
        for i in n:
            pod *= int(i)
            print(pod)
            sod += int(i)
        return pod - sod
