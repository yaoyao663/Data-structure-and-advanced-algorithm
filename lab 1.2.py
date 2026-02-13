def check(x, y):
    return (x == "(" and y == ")") or \
           (x == "[" and y == "]") or \
           (x == "{" and y == "}")

def is_valid_parentheses(s):
    stack = []
    comparison_time = 0
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if not stack:
                return False, comparison_time
            top = stack.pop()
            comparison_time += 1
            if not check(top, c):
                return False, comparison_time
        else:
            return False, comparison_time
    return len(stack) == 0, comparison_time

#Test
if __name__ == "__main__":
    test_cases = [
        ("([]){}", True),   
        ("({[]})", True),   
        ("()[]{}", True),    
        ("([)]", False,),    
        ("((())", False),    
        ("((()))", True),  
        ("({[)})", False),
        ("", True),          
    ]
    for s, expected in test_cases:
        result = is_valid_parentheses(s)
        print(f"Input: {s:8} Expected: {expected} Result: {result} Comparison time: {result[1]} {'✓' if result[0] == expected else '✗'}")