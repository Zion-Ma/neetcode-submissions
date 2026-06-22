class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            idx = len(self.tweetMap[followee]) - 1
            if idx >= 0:
                count, Id = self.tweetMap[followee][idx]
                minHeap.append((count, Id, followee, idx - 1))
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, Id, followee, idx = heapq.heappop(minHeap)
            res.append(Id)
            if idx >= 0:
                count, Id = self.tweetMap[followee][idx]
                heapq.heappush(minHeap, (count, Id, followee, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
