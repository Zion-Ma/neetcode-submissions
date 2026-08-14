class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) return false;
        sort(hand.begin(), hand.end());
        unordered_map<int, int> freq;
        for (int i = 0; i < hand.size(); i++) {
            freq[hand[i]]++;
        }
        for (const int n : hand) {
            if (freq[n] == 0) {continue;}
            for (int i = n + 1; i < n + groupSize; i++) {
                if (freq[i] == 0) {
                    return false;
                }
                freq[i]--;
            } 
            freq[n]--;
        }
        for (const auto& [key, value] : freq) {
            if (value != 0) {return false;}
        }
        return true;
    }
};
