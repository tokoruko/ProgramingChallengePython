def loop(n):
    if type(n) != int :
        print("Put an integer in the variable 'n'! ")

    elif type(n) == int :
        if n >= 0 :
            cnt = 0
            for i in range(n+1):
              cnt += i**2
            print(cnt)
        elif n < 0 :
            print("I don't want to work." )
    else:
        print("It's not my business")
        pass

        

    
