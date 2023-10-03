'''
Check if a string is valid. A string is valid if all it's characters occur an equal number of times.
Also, if one character occurs a different number of times but we can remove just one instance of it
and the remainning charcters will occur the same number of times.
'''

from collections import Counter

def isValid(s):
    # Write your code here
    fd = {}

    # create character frequency dictionary using Coutner
    fd = dict(Counter(s))
    freqs = list(fd.values())
    
    # if the count of highest frequency is 1, and the minimum frequency is less return YES
    # if the count of highest frequency exceeds 1, but the minimum frequency is 1 less and only 
    
    high_freq = max(freqs)
    low_freq = min(freqs)

    # case 1: all characters occur the same number of times
    if high_freq == low_freq:
        return 'YES'
    # case 2: count of characters with the highest frequency is 1
    # and this is just 1 character more than the lowest frequency
    elif freqs.count(high_freq) == 1 and high_freq - 1 == low_freq:
        return 'YES'
    # case 3: count of characters with the highest frequency is more than 1
    # count of characters with the lowest frequency is 1
    elif freqs.count(high_freq) > 1 and freqs.count(low_freq) == 1:
        return 'YES'
    else:
        return 'NO'