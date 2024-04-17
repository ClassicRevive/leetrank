class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # count vowels in first k
        vowels='aeiou'

        count = 0
        curr = s[:k]
        for i in range(k):
            if s[i] in vowels:
                count += 1
        highest = count

        start = 0
        end = k
        while end < len(s):
            if s[start] in vowels:  # only consider characters coming in and out
                count -= 1
            if s[end] in vowels:
                count += 1
            if count > highest:
                highest = count
                
            start += 1
            end += 1

        return highest
        