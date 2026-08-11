/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if (intervals.empty()) {return 0;}
        int room = 0;
        int count = 0;
        std::vector<int> start;
        std::vector<int> end;
        int s = 0, e = 0;
        for (int i = 0; i < intervals.size(); i++) {
            start.push_back(intervals[i].start);
            end.push_back(intervals[i].end);
        }
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());
        while (s < (int)start.size()) {
            if (start[s] < end[e]) {
                count++;
                room = std::max(room, count);
                s++;
            } else {
                count--;
                e++;
            }
        }
        return room;
    }
};
