def IsPrime(n):
    '''Checks if a number is prime.

    Input
    -----
    Argument    Type        Description
    n           integer     This number will be checked for primality.

    Output
    ------
    Return type     Boolean

    Examples
    -------

    >>>IsPrime(25)
    False
    >>>IsPrime(47)
    True
    >>>IsPrime(49)
    False
    '''
    if n==1:
        return False

    if ( n in [2,3] ):
        return True

    if (n%6 in [1,5]):
        # maybe prime
        ans=True
        for i in range(3,n//2+1, 2):
            if n%i==0:
                ans=False
                break
    else:
        ans = False

    return ans



def gcd(l):
    
    '''Compute the greatest common divisor of a list of integers
    Input
    -----
    Variable    Type    Description
    l           list    A list of integers whose GCD is to be computed

    Output
    ------
    Return type     integer
    '''
    ##########################
    def __gcd2(a,b):
        if a<b:
            a,b = b,a

        while b>0:
            a,b = b, a%b
        return a
    ###########################

    assert len(l)>=2, "At least two numbers required to compute gcd."

    ans = __gcd2(l[0],l[1])
    
    if len(l)>2:
        for i in range(2,len(l)):
            ans = __gcd2(ans, l[i])

    return ans


def lcm(l):
    '''Compute the least common multiple of a list of integers
    Input
    -----
    Variable    Type    Description
    l           list    A list of integers whose LCM is to be computed

    Output
    ------
    Return type     integer
    '''

    assert len(l)>=2, "At least two numbers required to compute lcm."
    ans = l[0]
    for i in l[1:]:
        ans = (i*ans)//gcd([ans,i])

    return int(ans)
