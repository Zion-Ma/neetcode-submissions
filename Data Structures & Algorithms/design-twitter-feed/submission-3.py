class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        ans = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            idx = len(self.tweetMap[followeeId]) - 1
            if idx >= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                feed.append((count, tweetId, followeeId, idx - 1))
        heapq.heapify(feed)
        while feed and len(ans) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(feed)
            ans.append(tweetId)
            if idx >= 0 :
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(feed, (count, tweetId, followeeId, idx - 1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
