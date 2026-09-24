def suiteSyraccus(x):
    suite=[x]
    while x>1:
        if x%2==0:
            x=x/2
        else:
            x=x*3+1
        suite.append(x)
    return suite