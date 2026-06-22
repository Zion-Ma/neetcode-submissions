class Twitter:

    def __init__(self):
       self.timestamp = 0
       self.tweet_heap = []
       self.followee = defaultdict(set)
       self.tweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweet_heap, (self.timestamp, userId, tweetId))
        self.tweet[userId].append(tweetId)
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        count = 0
        popped = []
        feed = []
        while self.tweet_heap and count < 10:
            timestamp, poster_id, tweetId = heapq.heappop(self.tweet_heap)
            if poster_id in self.followee[userId] or poster_id == userId:
                feed.append(tweetId)
                count += 1
            popped.append((timestamp, poster_id, tweetId))
        for item in popped:
            heapq.heappush(self.tweet_heap, item)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)
        
