#play.py

def factorial(n):
    if n <= 1:
        return 1
        
    return n * factorial(n-1)
    
print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))
