class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        s_ast = sorted(asteroids)
        flag = True
        for ast in s_ast:
            if mass >= ast:
                mass += ast
            else:
                flag = False
        return flag
            
             