class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        i = 0

        while i < len(s):
            if s[i] != ')':
                stack.append(s[i])
                # print(stack)
            else:
                x = ''
                while stack[-1] != '(' and len(s) >= 1:
                    y = stack.pop()
                    x += y[::-1]
                stack.pop()
                stack.append(x)
                # print(stack)
            i += 1

        # print('final: ',stack)

        ans = ''
        for i in range(len(stack)):
            if stack[i] != '(' and stack[i] != ')':
                ans += stack[i]

        
        
        return ans