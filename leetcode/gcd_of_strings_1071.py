def gcdOfStrings(str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        # if the lengths are not divisible, then return empty string
        
        def valid_gcd(k):
            # check if prefix of length k is gcd string
            if l1 % k or l2 % k:
                return False
            
            base = str1[:k]
            n1, n2= l1//k, l2//k

            return str1 == base*n1 and str2 == base*n2
        
        for i in range(min(l1, l2), 0, -1):
            if valid_gcd(i):
                return str1[:i]

        return ""

if __name__ == "__main__":
    ans = gcdOfStrings("ABAB", "ABABABAB")
    print(ans)