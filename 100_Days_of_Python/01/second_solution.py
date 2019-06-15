class Solution(object):
    def maxArea(self, height):
        result = 0
        front = 0
        end = len(height)-1
        while(True):
            length = end - front
            if(not length): return result #break result
            
            width = min(height[front],height[end])
            result = max(result,width*length)
            
            if(height[end] >= height[front]):
                front += 1
            else: end -= 1
            
