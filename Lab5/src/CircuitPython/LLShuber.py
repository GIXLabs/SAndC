#Huber Loss Implementation
def LLS(x, y, max_iter=20, tol=1e-6, delta=1.0):
    
    n = len(x)
    m, b = 0.0, 0.0

    x_mean = sum(x) / n
    y_mean = sum(y) / n

    num = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    den = sum((xi - x_mean)**2 for xi in x)
    m = num / den
    b = y_mean - m * x_mean

    for _ in range(max_iter):
        residuals = [yi - (m * xi + b) for xi, yi in zip(x, y)]
        weights = []
        for r in residuals:
            abs_r = abs(r)
            if abs_r <= delta:
                weights.append(1.0)
            else:
                weights.append(delta / abs_r)

        
        w_sum = sum(weights)
        xw_mean = sum(w * xi for w, xi in zip(weights, x)) / w_sum
        yw_mean = sum(w * yi for w, yi in zip(weights, y)) / w_sum

        num = sum(w * (xi - xw_mean) * (yi - yw_mean)
                  for w, xi, yi in zip(weights, x, y))
        
        den = sum(w * (xi - xw_mean)**2 for w, xi in zip(weights, x))
        new_m = num / den
        new_b = yw_mean - new_m * xw_mean

        if abs(new_m - m) < tol and abs(new_b - b) < tol:
            break
        m, b = new_m, new_b

    return m, b





# Test

# x = [1, 2, 3, 4, 5]
# y = [0, 3, 8, 9, 15]
# 
# slope, intercept = LLS(x, y)
# print("Slope:", slope)
# print("Intercept:", intercept)




