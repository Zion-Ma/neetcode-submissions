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
    unordered_map<Node*, Node*> node_map;
    Node* copyRandomList(Node* head) {
        Node* curr = head;
        while (curr) {
            Node* new_node = new Node(curr->val);
            node_map[curr] = new_node;
            curr = curr->next;
        }
        for (Node* old_node = head; old_node; old_node = old_node->next) {
            node_map[old_node]->next = node_map[old_node->next];
            node_map[old_node]->random = node_map[old_node->random];
        }
        return node_map[head];
    }
};
