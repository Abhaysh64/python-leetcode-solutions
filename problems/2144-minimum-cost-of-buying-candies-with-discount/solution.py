class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        amount = 0
        i = 0
        if len(cost) < 3:
            return sum(cost)
        for i in range(0,len(cost),3):
            amount  = amount + cost[i] 
            if i+1 <= len(cost)-1:
                amount += cost[i+1] 

        return amount

        