/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {return nullptr;}
        while (lists.size() > 1) {
            vector<ListNode*> merged;
            for (int i = 0; i < lists.size(); i += 2) {
                ListNode* next_node = i + 1 < lists.size() ? lists[i + 1] : nullptr;
                ListNode* new_node = merge(lists[i], next_node);
                merged.push_back(new_node);
            }
            lists = merged;
        } 
        return lists[0];
    }
    ListNode* merge(ListNode* node1, ListNode* node2) {
        if (!node1) {return node2;}
        if (!node2) {return node1;}
        ListNode dummy;
        ListNode* curr = &dummy;
        while (node1 and node2) {
            if (node1->val < node2->val) {
                curr->next = node1;
                node1 = node1->next;
            } else {
                curr->next = node2;
                node2 = node2->next;
            }
            curr = curr->next;
        }
        curr->next = node1 ? node1 : node2;
        return dummy.next;
    }
};
