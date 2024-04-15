''' Reverse vowels in a string (two pointers approach)'''
def reverseVowels(self, s: str) -> str:
        word = list(s)

        start = 0
        end = len(word)-1
        vowels = set('aeiouAEIOU')
        while start < end:
            while start < end and word[start] not in vowels:  # move left pointer
                start += 1
            while start < end and word[end] not in vowels:  # move right pointer
                end -= 1
            
            # found a match, swap them
            word[start], word[end] = word[end], word[start]

            start += 1
            end -= 1
        
        return "".join(word)
