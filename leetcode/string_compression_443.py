def compress(chars: list[str]) -> int:
        # consecutive linear searches for first new character
        # we edit the array, but we don't care about deleting elements for this solution
        # just record the compression at the earliest index possible
        i = 0
        res = 0  # so we don't need to compute len at the end
        while i < len(chars):   
            count = 1
            while i + count < len(chars) and chars[i] == chars[i+count]:
                count += 1
            chars[res] = chars[i]
            res += 1

            if count > 1:
                str_repr = str(count)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += count
                        
        return res
        