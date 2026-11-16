class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            result = ""

            for i in range(0, len(s), k):
                group = s[i:i + k]

                digit_sum = sum(int(ch) for ch in group)

                result += str(digit_sum)

            s = result

        return s