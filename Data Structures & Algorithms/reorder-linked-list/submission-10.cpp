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
    void reorderList(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast and fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* first = head;
        ListNode* second = slow->next;
        slow->next = nullptr;
        second = reverse(second);
        while (first and second) {
            ListNode* first_next = first->next;
            ListNode* second_next = second->next;
            first->next = second;
            second->next = first_next;
            first = first_next;
            second = second_next;
        } 
        // curr->next = first ? first : second;
    }
    ListNode* reverse(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = nullptr;
        while (curr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};
