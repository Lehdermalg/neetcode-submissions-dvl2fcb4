class Solution:


    def evalRPN(self, tokens: List[str]) -> int:
        # LIFO stack
        stack = []
        for token in tokens:
            if token in "+-*/":
                o2 = stack.pop()
                o1 = stack.pop()
                if token == "+":
                    r = o1 + o2
                elif token == "-":
                    r = o1 - o2
                elif token == "*":
                    r = o1 * o2
                elif token == "/":
                    r = o1 / o2
            else:
                r = int(token)
            stack.append(int(r))
        return int(r)