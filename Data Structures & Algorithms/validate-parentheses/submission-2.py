class Solution:
    def isValid(self, s: str) -> bool:
        # FILO stack
        stack = []
        mapping = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        for c in s:
            ls = len(stack)
            print(f"ls: {ls}, c: {c}")
            if c in "([{":
                stack.append(c)
                print(f"stack: {stack}")
            else:
                if ls>0 and stack[ls-1] == mapping[c]:
                    stack.pop(ls-1)
                else:
                    return False
        return len(stack) == 0