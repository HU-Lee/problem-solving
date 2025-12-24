class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n, odd_n = n // 2, n - n // 2
        even_m, odd_m = m // 2, m - n // 2
        return even_n * odd_m + odd_n * even_m