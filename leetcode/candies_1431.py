def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        result = []
        for k in candies:
            result.append(k+extraCandies >= highest)

        return result        