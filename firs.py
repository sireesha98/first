# function to print the first m multiple
# of a number n without using loop.
def multiple(m, n1):
 
    # inserts all elements from n to 
    # (m * n1)+1 incremented by n.
    a = range(n, (m * n1)+1, n1)
     
    print(*a)
 
# driver code 
m = 4
n1 = 3
multiple(m, n1)
