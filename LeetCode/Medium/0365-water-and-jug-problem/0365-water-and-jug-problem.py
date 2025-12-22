class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x+y:
            return False
        r = gcd(x,y)
        return target%r == 0