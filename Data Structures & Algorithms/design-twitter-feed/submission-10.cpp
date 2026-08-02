class Twitter {
public:
    unordered_map<int, unordered_set<int>> followee_map;
    unordered_map<int, vector<pair<int, int>>> post_map;
    int post_time;
    Twitter() {
        post_time = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        post_map[userId].push_back({post_time, tweetId});
        post_time++;
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> result = {};
        priority_queue<pair<int, int>> heap;
        int count = 10;
        for (const auto& [t, tweetId] : post_map[userId]) {
            heap.push({t, tweetId});
        }
        for (const int followeeId : followee_map[userId]) {
            for (const auto& [t, tweetId] : post_map[followeeId]) {
                heap.push({t, tweetId});
            }
        }
        while (!heap.empty() and count > 0) {
            result.push_back(heap.top().second);
            heap.pop();
            count--;
        }
        return result;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }
        followee_map[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followee_map[followerId].find(followeeId) == followee_map[followerId].end()) {return;}
        followee_map[followerId].erase(followeeId);
    }
};
