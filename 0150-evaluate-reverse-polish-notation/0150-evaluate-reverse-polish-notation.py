class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        main = []
        reserve = []
        
        sy = ['+','-','*','/']
        
        for i in range(len(tokens)-1,-1,-1):
            main.append(tokens[i])
            
        print(main)
        print(main[-1])
        print(main)
        
        while len(main)!=0:
            if main[-1] not in sy:
                x = main.pop()
                reserve.append(x)
            else:
                a = reserve.pop()
                b = reserve.pop()
                c = main.pop()
                print('a: ',a)
                print('b: ',b)
                print('c:' ,c)
                if c == '+':
                    ans = int(b)+int(a)
                if c == '-':
                    ans = int(b)-int(a)
                if c == '*':
                    ans = int(b)*int(a)
                if c == '/':
                    ans = int(b)/int(a)
                print('ans:', ans)
                reserve.append(ans)
                
        return int(reserve[0])