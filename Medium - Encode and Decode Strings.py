# Design an algorithm to encode a list of strings to a string. The encoded string is then sent 
# over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Example1:
    # Input: ["lint","code","love","you"]
    # Output: ["lint","code","love","you"]
    # Explanation:
    # One possible encode method is: "lint:;code:;love:;you"

# Example2:
    # Input: ["we", "say", ":", "yes"]
    # Output: ["we", "say", ":", "yes"]
    # Explanation:
    # One possible encode method is: "we:;say:;:::;yes"

# Topic: Arrays
# Use the length of each string along with delimiter to identify individual strings

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
class Solution:
    def encode(self, strs):
        return "".join((str(len(string)) + ";" + string for string in strs))

    def decode(self, str):
        pointer = 0
        result = []
        numStr = []
        string = []

        while pointer < len(str):
            if str[pointer] != ";":
                numStr.append(str[pointer])
                pointer += 1
            else:
                string.clear()

                pointer += 1

                num = int("".join(numStr))

                while num > 0:
                    string.append(str[pointer])
                    num -= 1
                    pointer += 1

                result.append("".join(string))

                numStr.clear()

        return result

sol = Solution()
enc = sol.encode(["::,#", "\"\"", "\\", "ajksgb", "+"])
print(sol.decode(enc))