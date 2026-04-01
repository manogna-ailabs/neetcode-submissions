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
        print(nums1[l1], nums1[r1])
        print(nums2[l2], nums2[r2])
        print("\n") 

        final = sorted(nums1[l1:r1+1] + nums2[l2:r2+1])
        print(final)
        return self.median(final)

        # if len(final) == 2:
        #     return (final[0]+final[1])/2
        # elif len(final) == 3:
        #     return final[1]

        # print(final)



        # mid1 = (l1 + r1) // 2
        # mid2 = (l2 + r2) // 2

        # return (nums1[mid1] + nums2[mid2])/2
