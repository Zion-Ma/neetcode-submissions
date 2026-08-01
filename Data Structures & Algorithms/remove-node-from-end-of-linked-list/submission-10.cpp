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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* curr = dummy;
        ListNode* fast = head;
        while (n > 0) {
            fast = fast->next;
            n--;
        }
        while (fast) {
            fast = fast->next;
            curr = curr->next;
        }
        ListNode* target = curr->next;
        std::cout<<curr->val;
        curr->next = target ? target->next : nullptr;
        delete target;
        target = nullptr;
        return dummy->next;
    }
};
