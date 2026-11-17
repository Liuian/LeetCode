'''
Solution: 把 strs: List[str] 合併成 'length'_'string''length'_'string'....

Time complexity: O(n)

Space complexity: O(n)
    - list output: O(n)
    - string output_str: 是最終回傳字串，不計入空間複雜度
'''
class Solution:
    def encode(self, strs: list[str]) -> str:
        output = []
        for str in strs:
            output.append(f"{len(str)}_{str}")
        output_str = "".join(output)

        return output_str        

    def decode(self, s: str) -> list[str]: 
        i = 0
        output = []

        while i < len(s):
            j = i
            
            while s[j] != "_":
                j += 1

            length = int(s[i : j])
            output.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return output

if __name__ == "__main__":
    solution = Solution()
    strs = ["Hello", "World"]
    encoded_str = solution.encode(strs)
    print(encoded_str)  # Output: "5_Hello5_World"
    decoded_strs = solution.decode(encoded_str)
    print(decoded_strs)  # Output: ["Hello", "World"]