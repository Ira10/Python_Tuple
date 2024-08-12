
def sum_and_prod(L):
    """ L is a list of numbers 
    Return a tuple where the first value is the 
    sum of all elements in L and the second value 
    is the product of all elements in L 
    """
    s, p = 0, 1 ## product has to be 1, other wise it will become 0
    
    for i in L:
      s += i
      p *= i
    return (s, p)

print(sum_and_prod([1,2,3,4]))   # prints (10, 24)
print(sum_and_prod([12,6,2,7]))   # prints (27, 1008)


#############################################
################## AT HOME ####################
#############################################

# Trace this code:
# Figure out what it returns and then run it to check yourself.
def always_sunny(t1, t2):
    """ t1, t2 are non-empty """
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)

print(always_sunny(('cloudy' ), ('cold',)))  # returns what? ('sunny', 'ccold')



def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    # your code here
    # if f1 < f2:
    #     return f1 
    # else:
    #     return f2

    ############## correct ##############
    # max_value = float('-inf')  # Start with the lowest possible value
    # for i in range(n + 1):
    #     max_value = max(max_value, f1(i), f2(i))
    # return max_value
    return max(f1(n), f2(n))

print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


def sublist_sum(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    # your code here
    sum_ = 0
    sum_1 = 0
    for i in L:
        for j in i:
            sum_ += j
        # sum_1 += sum_  ## returns 21
    # sum_1 += sum_   ## returns 18
    # return sum_1
    return sum_   ##returns 18
            

print(sublist_sum([[1,2], [4,5,6]])) # prints 18

###### 12 august, 10:15 PM
#############################################
################## ANSWERS TO AT HOME ####################
#############################################

# def max_of_both(n, f1, f2):
#     """ n is an int
#         f1 and f2 are functions that take in an int and return a float
#     Applies f1 and f2 on all numbers between 0 and n (inclusive). 
#     Returns the maximum value of all these results.
#     """
#     # your code here
#     maxval = f1(0)
#     for i in range(n+1):
#         if f1(i) > maxval:
#             maxval = f1(i)
#         if f2(i) > maxval:
#             maxval = f2(i)
#     return maxval

# # print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# # print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


# def sublist_sum(L):
#     """ L is a list whose elements are lists with int elements
#     Returns the sum of all int elements. """
#     ## One way by using the sum function over the sublist
#     tot = 0
#     for subL in L:
#         tot += sum(subL)
#     return tot
#     ## Alternate way by nesting a for loop that 
#     ## iterates over the sublist's int elements
#     tot = 0
#     for subL in L:
#         for e in subL:
#             tot += e
#     return tot
    

# # print(sublist_sum([[1,2], [4,5,6]])) # prints 18
