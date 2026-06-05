class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(num1,num2+1):
            wavy = 0
            if num < 100:
                continue
            while len(str(num)) >= 3:
                r = num % 10
                m = (num//10) % 10
                l = ((num//10)//10) % 10
                if  m > max(l,r) or m < min(l,r):
                    wavy += 1
                num = num // 10
            ans += wavy
        return ans





        