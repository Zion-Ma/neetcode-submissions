/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> random_map;
        Node* curr = head;
        while (curr) {
            random_map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        for (Node* curr = head; curr; curr = curr->next) {
            random_map[curr]->next = random_map[curr->next];
            random_map[curr]->random = random_map[curr->random];
        }
        return random_map[head];
    }
};
