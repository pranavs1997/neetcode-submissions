class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for c in tokens:
            if c in ops:
                a = stack.pop()
                b = stack.pop()

                if c == "+":
                    res = b + a
                elif c == "-":
                    res = b - a
                elif c == "*":
                    res = b * a
                else:
                    res = int(b / a)

                stack.append(res)
            else:
                stack.append(int(c))

        return stack[-1]