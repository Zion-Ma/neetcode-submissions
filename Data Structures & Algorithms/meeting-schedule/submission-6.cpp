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
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(
            intervals.begin(), intervals.end(), [](const Interval& x, const Interval& y){
                return x.start < y.start;
            }
        );
        int prev_end = intervals[0].end;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i].start < prev_end) {
                return false;
            }
            prev_end = intervals[i].end;
        }
        return true;
    }
};
