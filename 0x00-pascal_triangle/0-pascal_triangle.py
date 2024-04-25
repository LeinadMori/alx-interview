def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(binomial_coefficient(i, j))
        triangle.append(row)
    
    return triangle