class Solution(object):
    def isPowerOfThree(self, n):
        if n <=1:
            return n==1
        else:
            return n%3==0 and self.isPowerOfThree(n/3)



"""
Solution 1 [[using MATHS AND  BITS SIZE]]

if n<=0: #this works because the 32bit is near to 3**19 so we use max number division
    return False
elif 3**19 % n ==0 or n==1:
    return True
else:
    return False"""
        
