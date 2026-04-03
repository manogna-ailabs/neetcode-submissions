class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        XOR[3,1,1]
        XOR[3,1], XOR[3,1], XOR[1,1]
        3, 1, 1

        []   :0
        [1]  :[0], [1]
        [1,2]:[0], [[1],[2]], [[1,2]]  #  a [XOR(0)] + b[XOR(0,1)] + c[XOR(0,2)] + [XOR(b,c)]

                XOR[1,2] 
        leaves: [1] [2]


        """
        out = []

        def dfs(idx, val):
            if idx == len(nums):
                return val
            prev = dfs(idx+1, val)
            child = dfs(idx+1, val ^ nums[idx])

            return child + prev
        return dfs(0, 0)