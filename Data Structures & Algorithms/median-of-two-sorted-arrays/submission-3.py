class Solution:
    def median(self, arr):
        l = len(arr)
        if l%2 == 0:
            return (arr[l//2-1] + arr[l//2])/2
        else:
            return arr[l//2]


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return self.median(nums2)
        if not nums2:
            return self.median(nums1)
            
        
        l1, r1 = 0, len(nums1)-1
        l2, r2 = 0, len(nums2)-1

        
        while l1<r1 and l2<r2:
            print(nums1[l1], nums1[r1])
            print(nums2[l2], nums2[r2])
            print("\n")

            if nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1

            if nums1[r1] < nums2[r2]:
                r2 -= 1
            else:
                r1 -= 1

        final = sorted(nums1[l1:r1+1] + nums2[l2:r2+1])
        return self.median(final)


