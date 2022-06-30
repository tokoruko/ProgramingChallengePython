def recursive_call(n):
    if type(n) != int :
        print("Put an integer in the variable 'n'! ")
    
    elif type(n) == int :
        if n <= 0 :
            return 0
        else:
            return n**2 + recursive_call(n-1)

def print_recursive(n):
    total = recursive_call(n)
    print(total)