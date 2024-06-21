import heapq as hq
# when we want to maintain a maximum or minimum k as we traverse a list, use a heap
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Create tuples of nums1 and nums2 and sort them with respect to nums2
        n = len(nums1)
        pairs = [(nums1[i], nums2[i]) for i in range(n)]
        pairs = sorted(pairs, key = lambda x: -x[1])

        # we initialise a heap with the first k pairs, and take the sum.
        heap = [x[0] for x in pairs[:k]]
        hq.heapify(heap)
        top_k_sum = sum(heap)
        max_score = top_k_sum * pairs[k-1][1]

        for i in range(k, len(nums1)):
            # smallest element popped to maintain k highest elements (including nums1[i], so rly k-1 highest)
            min_val = hq.heappop(heap)
            top_k_sum -= min_val
            top_k_sum += pairs[i][0]
            hq.heappush(heap, pairs[i][0])

            curr_score = top_k_sum*pairs[i][1]
            max_score = max(max_score, curr_score)
        
        return max_score
