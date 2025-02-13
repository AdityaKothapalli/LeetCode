class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # Start from the largest possible W, which is sqrt(area)
        w = int(math.sqrt(area))
        l =0               
        while area % w != 0:
            w -= 1  # Reduce W until we find a divisor                                     
        l = area // w  # Compute the corresponding L
        return [l, w]  