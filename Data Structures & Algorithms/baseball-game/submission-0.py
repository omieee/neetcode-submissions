class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for ops in operations:
            if ops == "+":
                results.append(results[-1] + results[-2])
            elif ops == "D":
                results.append(results[-1] * 2)
            elif ops == "C":
                results.pop()
            else:
                results.append(int(ops))
        return sum(results)
        