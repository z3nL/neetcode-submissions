class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = self.followees[userId] | {userId}
        next_tweet = []
        for c in candidates:
            if c not in self.tweets:
                continue
            time, tweetId = self.tweets[c][-1]
            index = len(self.tweets[c])-1
            heapq.heappush(next_tweet, (time, tweetId, c, index))
        res = []
        while next_tweet and len(res)<10:
            time, tweetId, c, index = heapq.heappop(next_tweet)
            res.append(tweetId)
            if index > 0:
                time, tweetId = self.tweets[c][index-1]
                heapq.heappush(next_tweet, (time, tweetId, c, index-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
