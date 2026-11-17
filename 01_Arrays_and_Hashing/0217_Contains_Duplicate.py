'''
Solution_1: Use a set to track seen numbers.
Time complexity: O(n)
Space complexity: O(n)

Solution_2: Use a set to track seen numbers, but check the length of the set against the length of the list.
Time complexity: O(n)
Space complexity: O(n)

Solution_3: Sort the list and check for adjacent duplicates.
Time complexity: O(n log n) 
    - sorting: O(n log n)
    - for loop: O(n)
Space complexity: O(1) since sorting in place
'''

class Solution:
    # First method
    def containsDuplicate_m1(self, nums: list[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else: 
                num_set.add(num)

        return False
    

    # modify run time
    def containsDuplicate_m2(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
    
    # modify memory
    def containsDuplicate_m3(self, nums: list[int]) -> bool:
        nums.sort()

        prev = nums[0]
        curr = 0

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr == prev:
                return True
            prev = curr
        
        return False
    
if __name__ == "__main__":
    sol = Solution()

    # Example 1 (預期結果: True)
    nums1 = [1, 2, 3, 1]
    print(sol.containsDuplicate_m1(nums1))
    print(sol.containsDuplicate_m2(nums1))
    print(sol.containsDuplicate_m3(nums1))

    # Example 2 (預期結果: False)
    nums2 = [1, 2, 3, 4]
    print(sol.containsDuplicate_m1(nums2))
    print(sol.containsDuplicate_m2(nums2))
    print(sol.containsDuplicate_m3(nums2))

    # Example 3 (預期結果: True)
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(sol.containsDuplicate_m1(nums3))
    print(sol.containsDuplicate_m2(nums3))
    print(sol.containsDuplicate_m3(nums3))
