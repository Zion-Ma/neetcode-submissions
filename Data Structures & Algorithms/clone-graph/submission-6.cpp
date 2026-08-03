/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<int, Node*> graph;
    Node* cloneGraph(Node* node) {
        if (!node) {
            return nullptr;
        }
        graph[node->val] = new Node(node->val);
        buildGraph(node);
        return graph[node->val];
    }
    void buildGraph(Node* node) {
        // cout<<node->val<< '\n';
        for (Node* neighbor : node->neighbors) {
            cout<<"entered the loop"<<'\n';
            if (graph.find(neighbor->val) == graph.end()) {
                graph[neighbor->val] = new Node(neighbor->val);
                buildGraph(neighbor);
            }
            graph[node->val]->neighbors.push_back(graph[neighbor->val]);
        }
    }
};
