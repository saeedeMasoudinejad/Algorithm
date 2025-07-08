from math import inf


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        ############################### solution 1  #################################
        # index_1 = 0
        # index_2 = 0
        # while len(nums2) != 0:
        #     while index_1 < m:
        #         if nums2[index_2] < nums1[index_1]:
        #             temps = nums1[index_1]
        #             nums1[index_1] = nums2[index_2]
        #             nums2[index_2] = temps
        #             index_2 = index_2 + 1 if n > 1 and n + 1 < len(nums2) else index_2
        #             index_1 = 0
        #         else:
        #             index_1 = index_1 + 1
        #     nums1[m] = nums2[index_2]
        #     nums2.remove(nums2[index_2])
        #     index_2 = 0
        #     index_1 = 0
        #     m = m + 1
        # print(nums1)

        ################################# solution 2 ############################
        nums1[m:] = nums2
        nums1.sort()
        print(nums1)

        ################################# solution 3 ############################
        index_1 = m - 1
        index_2 = n - 1
        index_total = m + n - 1
        if nums1[index_1] > nums2[index_2]:
            nums1[index_total] = nums1[index_1]
            nums1[index_1] = nums2[index_2]
            index_total -= 1
            index_2 -= index_2
        else:
            nums1[index_total] = nums2[index_2]
            index_total -= 1

    def remove_element(self, nums: list[int], val: int) -> int:
        k = 0
        for index, value in enumerate(nums):
            if value == val:
                nums[index] = float(inf)
            else:
                k += 1
        nums.sort()
        return k

    def remove_duplicate_from_sorted_array(self, nums: list[int]) -> int:
        # first solution but should increase the runtime
        k: int = 1
        temp: int = nums[0]
        for i, value in enumerate(nums[1:]):
            if temp == value:
                nums[i] = float(inf)
            else:
                temp = value
                k += 1
        nums.sort()
        return k

    def remove_duplicate_from_sorted_array_2(self, nums: list[int]) -> int:
        # solution 1
        # pivot: int = nums[0]
        # index: int = 1
        # twice_num: int = 1
        # repeat_num: int = 1
        # while index < len(nums):
        #     while nums[index] == pivot:
        #         repeat_num += 1
        #         if repeat_num > 2:
        #             nums[index] = float(inf)
        #         else:
        #             twice_num += 1
        #         if index < len(nums) - 1:
        #             index += 1
        #         else:
        #             nums.sort()
        #             return twice_num
        #     pivot = nums[index]
        #     repeat_num = 0

        # solution 2
        # pivot = nums[0]
        # repeat_limit = 1
        # twice_nums: int = 1
        # for i, value in enumerate(nums[1:]):
        #     if value == pivot:
        #         repeat_limit += 1
        #         if repeat_limit > 2:
        #             nums[i] = float(inf)
        #         else:
        #             twice_nums += 1
        #     else:
        #         pivot = value
        #         twice_nums += 1
        #         repeat_limit = 1
        # nums.sort()
        # print(nums)
        # return twice_nums
        # solution3
        if len(nums) <= 2:
            return len(nums)

        slow = 2  # Position to place next valid element

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        print(nums)
        return slow

    def majorityElement(self, nums: list[int]) -> int:
        # majority: int = int(len(nums) / 2)
        # repeat_nme: dict[int, int] = {}
        # for i in nums:
        #     if i in repeat_nme:
        #         repeat_nme[i] += 1
        #     else:
        #         repeat_nme[i] = 1
        # for j in repeat_nme:
        #     if repeat_nme[j] > majority:
        #         return j

        nums.sort()
        majority = int(len(nums) / 2)
        return nums[majority]

    def rotate(self, nums: list[int], k: int) -> None:
        # l = len(nums)
        # if k > l:
        #     k = k - l
        # for i in range(k):
        #     for i in range(len(nums)):
        #         temp = nums[i]
        #         nums[i] = nums[0]
        #         nums[0] = temp
        # return nums
        l = len(nums)
        if k > l:
            k = k - l
        nums[:] = nums[l-k:] + nums[0:l-k]
        return nums