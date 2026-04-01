class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        maxArea = 0
        for i, h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                print("\n")
                print(i,stack)
                idx = stack.pop()
                height = heights[idx]
                if stack:
                    left_boundary = stack[-1]
                    area = (i-1-left_boundary)* height
                    print(i,left_boundary, area, stack)
                else:
                    area = height * i
                if area > maxArea:
                    maxArea = area
            stack.append(i)
        right_boundary = len(heights)
        while stack:
            idx = stack.pop()
            height = heights[idx]

            if stack:
                left_boundary = stack[-1]
                width = right_boundary - left_boundary - 1
            else:
                width = right_boundary

            area = height * width
            maxArea = max(maxArea, area)

        return maxArea