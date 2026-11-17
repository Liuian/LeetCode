'''
Solution_1: 正乘一次，反乘一次，存在兩個 array。取這個位置的前一個位置，後一個位置的值，相乘。
Solution_2: 加快 runtime。正乘一次，存到output array。反乘一次，直接把答案乘上output array 對應的格子並且存回同一個位置。

Time complexity for solution_2: O(n)

Space complexity for solution_2: O(1)
    - 因為 output array 不算進去，因為是要 return 的東西。

Note:
    - Division operation 就是除法運算。
    - 定義 array 長度： arr = [1] * len(nums)
    - for loop 反著走

'''
class Solution:
    def productExceptSelf_1(self, nums: list[int]) -> list[int]:
        
        arr_1 = [1] * len(nums)
        arr_2 = [1] * len(nums)
        tmp_1 = 1
        tmp_2 = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            tmp_1 = tmp_1 * nums[i]
            tmp_2 = tmp_2 * nums[len(nums) - 1 - i]

            arr_1[i] = tmp_1
            arr_2[len(nums) - 1 - i] = tmp_2

        output[0] = arr_2[1]
        output[len(nums) - 1] = arr_1[len(nums) - 1 - 1]

        for i in range(1, len(nums) - 1):
            output[i] = arr_1[i - 1] * arr_2[i + 1]

        return output

    # 1, 2, 3, 4
    # _, 1, 2, 6
    # 24, 12, 4, _
    def productExceptSelf_2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        tmp = 1

        for i in range(n - 1):
            output[i + 1] = output[i] * nums[i]
        
        for i in range(n - 2, -1, -1):
            tmp = tmp * nums[i + 1]
            output[i] = output[i] * tmp

        return output
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf_2(nums))
    nums = [-1, 1, 0, -3, 3]
    print(Solution().productExceptSelf_2(nums))