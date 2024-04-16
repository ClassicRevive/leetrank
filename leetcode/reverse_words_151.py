def reverseWords(self, s: str) -> str:
        words = s.strip().split()

        for i in range(len(words)//2):
            words[i], words[-i-1] = words[-i-1], words[i]
        
        return " ".join(words)