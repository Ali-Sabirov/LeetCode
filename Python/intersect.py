class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums11 = nums1.copy()
        nums21 = nums2.copy()
        nums3 = []
        if len(nums11) < len(nums21):
            for i in range(len(nums11)):
                x = nums11[i]
                if nums21.count(x) > 0:
                    nums3.append(x)
                    nums21.remove(x)
        else:
            for i in range(len(nums21)):
                x = x = nums21[i]
                if nums11.count(x) > 0:
                    nums3.append(x)
                    nums11.remove(x)
        return nums3