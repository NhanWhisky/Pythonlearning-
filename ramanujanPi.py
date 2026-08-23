import math

def Estimate_pi():
    epsilon = 1e-15
    total_sum = 0
    k = 0
    coeff = (2 * math.sqrt(2)) / 9801
    
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = (math.factorial(k) ** 4) * (396 ** (4 * k))
        division = num / den
        
        total_sum += division
        
        if (coeff * division) < epsilon:
            break
        k += 1
        
    return 1 / (coeff * total_sum)