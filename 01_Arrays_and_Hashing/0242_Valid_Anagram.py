'''
Solution: 
    - Use two dictionaries to count the occurrences of each character in both strings, and then compare the two dictionaries.

Time complexity: O(n)
    - O(1) + O(n) + O(n) + O(1) = O(n)
    - len() + for loop + for loop + dict comparison

Space complexity: O(1)
    - 因為兩個 dict 的大小最多是 26 個英文字母。

Note:
    - dict1 可以直接和 dict2 比較所有的 key-value pair，不管 pair 的順序。
    - 可以加上一個判斷式判斷長度是否相同，以加快實際執行速度。
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for character in s:
            if character in count_s:
                count_s[character] += 1
            else:
                count_s[character] = 1


        for character in t:
            if character  in count_t:
                count_t[character] += 1
            else:
                count_t[character] = 1

        return count_s == count_t
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # Output: True
    print(solution.isAnagram("rat", "car"))          # Output: False