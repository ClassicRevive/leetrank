''' Suboptimal linear search solution '''
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        results = [] 
        for left, right in queries:
            substr = s[left:right+1]

            # linear search for plates between candles
            total = 0
            curr_sum = 0
            in_seq =  False
            for j in range(len(substr)):
                if substr[j] == "|":
                    in_seq = True
                    total += curr_sum
                    curr_sum = 0
        
                elif in_seq and substr[j] == "*":
                    curr_sum += 1
            
            results.append(total)
        
        return results
                


''' Optimisation: binary search and prefix sum '''
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == "|"]
        result = []

        for left, right in queries:
            # binary search for leftmost candle
            
            leftmost = bisect.bisect_left(candles, left)  # first digit >= left
            rightmost = bisect.bisect(candles, right)-1  # first digit <= right

            # now calculate number of plates in that range and add
            if leftmost < rightmost:  # at least 2 plates in query range
                ans = (candles[rightmost] - candles[leftmost]) - (rightmost-leftmost)
                result.append(ans)
            else:
                result.append(0)
        
        return result

        