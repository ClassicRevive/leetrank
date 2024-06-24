class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # count character frequencies in s
        # for the first 9 most frequent, add to keypress dictionary with value 1
        # for second 9 most frequent, add to keypress dictionary with value 2
        # for remaining, add to keypress dictionary with value 3
        # calculate keypresses
        from collections import defaultdict

        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1
        
        # get key presses for each character
        uc = 0
        key_presses = 0
        for char, freq in sorted(char_counts.items(), key=lambda x: -x[1]):
            if uc < 9:
                key_presses += freq
            elif uc < 18:
                key_presses += freq*2
            else:
                key_presses += freq*3

            uc += 1
        
        return key_presses
