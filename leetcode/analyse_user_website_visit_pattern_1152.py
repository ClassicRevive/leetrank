class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict
        
        utw = []
        site_by_user = defaultdict(list)
        user_triplets = defaultdict(set)
        triplet_scores = defaultdict(int)
        max_score = 0

        # create username, timestamp, website tuples and sort them on timestamp
        for row in sorted(zip(username, website, timestamp), key = lambda x: x[2]):
            utw.append(row)

        # get traffic by user in order of visits
        for user, website, timestamp in utw:
            site_by_user[user].append(website)
        
        
        # create all triplets for each user
        for user, sites in site_by_user.items():
            
            # create all unique in-order 3-tuples
            user_visited = set(
                (sites[i], sites[j], sites[k])
                for i in range(len(sites))
                for j in range(i + 1, len(sites))
                for k in range(j + 1, len(sites)))
            
            # keep updating the occurrences of triplets and keeping track of the max while counting occurrences
            # for each user
            for t in user_visited:
                triplet_scores[t] += 1
                max_score = max(triplet_scores[t], max_score)
        
        candidates = [t for t in triplet_scores.keys() if triplet_scores[t] == max_score]
        return min(candidates)
