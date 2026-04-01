class Solution:
    def calPoints(self, operations: List[str]) -> int:
        c = []
        for i in operations:
            if i != "C" and i != "D" and i != "+":
                c.append(int(i))
            elif i == "C":
                c.pop()
            elif i == "D":
                c.append(2*c[-1])
            elif i == "+":
                c.append(c[-2]+c[-1])
        return sum(c)
                