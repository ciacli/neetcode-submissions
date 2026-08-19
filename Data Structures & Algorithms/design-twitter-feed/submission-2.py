class Twitter:

    def __init__(self):
        self.followees = {}
        self.posts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.setdefault(userId, [])
        self.posts[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        l = self.followees.get(userId, {userId})
        h = []
        counts = {}
        for followee in l:
            if not followee in self.posts:
                continue
            #print(followee)
            thisPosts = self.posts[followee]
            postslen = len(thisPosts)
            counts.setdefault(followee, postslen - 1)
            if counts[followee] < 0:
                continue
            latest = thisPosts[counts[followee]]
            counts[followee] -= 1
            t = (*latest, followee)
            heapq.heappush(h, t)
        ans = []
        for _ in range(10):
            if not h:
                break
            latest = heapq.heappop(h)
            tweetId = latest[1]

            ans.append(tweetId)
            followee = latest[2]
            #print(followee)
            thisPosts = self.posts[followee]

            postslen = len(thisPosts)

            if counts[followee] < 0:
                continue

            latest = thisPosts[counts[followee]]
            counts[followee] -= 1
            t = (*latest, followee)
            heapq.heappush(h, t)
            
        return ans
            




    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees.setdefault(followerId, {followerId})
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followees:
            return

        self.followees[followerId].discard(followeeId)
        if not self.followees[followerId]:
            del self.followees[followerId]
