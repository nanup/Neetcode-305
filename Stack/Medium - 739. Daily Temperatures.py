class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()
                answer[stackIndex] = i - stackIndex
            stack.append((temp, i))
        return answer