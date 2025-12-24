class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                answer += num1 // num2
                num1 = num1 % num2
            else:
                answer += num2 // num1
                num2 = num2 % num1
        return answer
            