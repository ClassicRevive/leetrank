'''
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a 
particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about 
potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, determine the number of times 
the client will receive a notification over all days.

'''


# essentially it's insertion sort with binary search modification.
def activityNotifications(expenditure, d):
    # Write your code here
    # binary search for item
    def find(lst, query, size):
        low, high = 0, size-1

        while low < high:
            mid = (low + high) // 2

            print(low, high)
            if lst[mid] < query:
                low = mid + 1
            elif lst[mid] > query:
                high = mid
            else:
                return mid


        print(low, high)
        low = min(low, high)
        
        # linear search if low has exceeded high without finding.
        # edge case for when we append to the top of list
        while low < size and lst[low] < query:
            low += 1
        return low

    notices = 0
    # checks if d is odd while finding index of median
    mid, mod = divmod(d, 2)
    sample = sorted(expenditure[:d])
    for start in range(d, len(expenditure)):
        curr = expenditure[start]

        # threshold setting dependent on whether window is even or odd
        if mod:
            threshold = sample[mid] * 2
        else:
            threshold = sample[mid] + sample[mid-1]

        if curr >= threshold:
            notices += 1

        # updating the list to search
        sample.pop(find(sample, expenditure[start-d], d))
        sample.insert(find(sample, curr, d-1), curr)

    return notices




def find(lst, query, size):
        low, high = 0, size-1

        while low < high:
            mid = (low + high) // 2

            print(low, high)
            if lst[mid] < query:
                low = mid + 1
            elif lst[mid] > query:
                high = mid
            else:
                return mid


        print(low, high)
        low = min(low, high)
        
        # linear search if low has exceeded high without finding.
        while low < size and lst[low] < query:
            low += 1
        return low



def main():
    print(find([1, 2, 3, 4], 4, 4))

    #print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))


if __name__ == '__main__':
    main()