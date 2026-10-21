class Twitter:

    def __init__(self):
        self.followMap = defaultdict(list)
        self.userPosts = defaultdict(list)
        self.userFeed = defaultdict(list)
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        #build priority queue
        posts = self.userPosts[userId]
        for followee in self.followMap[userId]:
            posts = posts + self.userPosts[followee]
        heapq.heapify_max(posts)
        if len(posts) < 10:
            retPosts = heapq.nlargest(len(posts), posts)
        retPosts = heapq.nlargest(10, posts)
        return [x[1] for x in retPosts]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)  


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
