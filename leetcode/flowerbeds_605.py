''' Can we plant n fowers given constraints in Q605? '''
def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # check how many flowers can be planted
        size = len(flowerbed)
        count = 0

        if n == 0:
            return True
        elif len(flowerbed) == 1:
            return flowerbed[0] == 0
        else:
            i = 0
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                i += 1  # can't plant in the next plot
            i += 1

            while i < size-1:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == flowerbed[i+1] == 0:
                        count += 1
                        i += 1
                    
                    if count >= n:  # terminate early if possible
                        return True
                i += 1
            # last plot is an edge case            
            if i == size-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    count += 1
            
            return count >= n