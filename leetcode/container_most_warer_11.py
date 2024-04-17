class Solution:
    ''' Very useful two pointers algorithm example '''
    def maxArea_suboptimal(self, height: list[int]) -> int:
        # suboptimal approach. calculate areas for each line O(n^2)
        highest = 0
        for i in range(len(height)):
            for j in range(len(height)):
                curr = abs(i - j) * min(height[i], height[j])
                if curr > highest:
                    highest = curr

        return highest

    def maxArea_optimal(self, height: list[int]) -> int:
        # suboptimal approach. calculate areas for each line O(n^2)
        highest = 0
        for i in range(len(height)):
            for j in range(len(height)):
                curr = abs(i - j) * min(height[i], height[j])
                if curr > highest:
                    highest = curr

        return highest 
 

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    