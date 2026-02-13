def horner_eval(coeffs, x):
    if not coeffs:
        return 0.0 
    
    res = float(coeffs[-1])
    
    for a in reversed(coeffs[:-1]):
        res = res * x + float(a)
    
    return res

# Test
coeffs_example = [3, -2, 0, 5] 
x_example = 2
result = horner_eval(coeffs_example, x_example)
print(f"P({x_example}) = {result}") 

coeffs_example = []
x_example = 5
result = horner_eval(coeffs_example, x_example)
print(f"P({x_example}) = {result}") 