class Solution(object):
    def maxArea(self, height):
        result = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                width = min(height[i],height[j])
                length = j-i
                result = max(result,length*width)
        return result
        
