def LLS(x, y):
    
    n = len(x)
    
    # Calculate means of x and y
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    
    
    # Numerator and Denominator Calculations for slope
    num = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denom = sum((x[i] - x_mean) ** 2 for i in range(n))
    
    
    # Slope and Intercept Calculations
    m = num / denom
    b = y_mean - m * x_mean
    
    return m, b





# Test

# x = [1, 2, 3, 4, 5]
# y = [0, 3, 8, 9, 15]
# 
# slope, intercept = LLS(x, y)
# print("Slope:", slope)
# print("Intercept:", intercept)


