'''
Solution: 
    1. Store nums into a dictionary with their frequency.
    2. Sort the dictionary by frequency in descending order.
    3. Return the first k elements from the sorted list.

Time complexity: O(n log n), since the time complexity of sorted() is O(n log n).

Space complexity: O(n)
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        sorted_nums = sorted(counts, key=lambda x: counts[x], reverse=True)

        output = []

        for i in range(k):
            output.append(sorted_nums[i])

        return output

        
if __name__ == "__main__":
    sol = Solution()

    # Example 1 (預期結果: [1, 2])
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(sol.topKFrequent(nums1, k1))

    # Example 2 (預期結果: [1])
    nums2 = [1]
    k2 = 1
    print(sol.topKFrequent(nums2, k2))

    # Example 3 (預期結果: [1, 2])
    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k3 = 2
    print(sol.topKFrequent(nums3, k3))