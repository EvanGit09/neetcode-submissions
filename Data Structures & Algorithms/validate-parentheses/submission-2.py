class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char == ')':
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr != '(':
                    return False
            elif char == '}':
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr != '{':
                    return False
            elif char == ']':
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr != '[':
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True