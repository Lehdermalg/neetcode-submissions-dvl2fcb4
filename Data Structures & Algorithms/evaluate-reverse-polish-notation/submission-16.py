class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # LIFO stack
        stack = []
        for token in tokens:
            if token in {"+","-","*","/"}:
                o2 = stack.pop()
                o1 = stack.pop()
                if token == "+":
                    stack.append(int(o1 + o2))
                elif token == "-":
                    stack.append(int(o1 - o2))
                elif token == "*":
                    stack.append(int(o1 * o2))
                elif token == "/":
                    stack.append(int(o1 / o2))
            else:
                stack.append(int(token))
        return stack[0]