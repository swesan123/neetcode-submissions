class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case "+":
                        r = a + b
                    case "-":
                        r = a - b 
                    case "*":
                        r = a * b 
                    case "/":
                        r = int(a / b)  # or a // b if you want truncation toward zero
                stack.append(r)
        return stack[-1]
