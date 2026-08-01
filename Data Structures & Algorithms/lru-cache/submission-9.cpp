class Node {
public:
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr){}
};
class LRUCache {
public:
    int cap;
    unordered_map<int, Node*> record;
    Node* head = new Node(0, 0);
    Node* tail = new Node(0, 0);
    LRUCache(int capacity) {
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (record.find(key) == record.end()) {return -1;}
        Node* node = record[key];
        remove(node);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (record.find(key) != record.end()) {
            record[key]->val = value;
            remove(record[key]);
            insert(record[key]);
            return;
        }
        Node* new_node = new Node(key, value);
        insert(new_node);
        record[key] = new_node;
        if ((int)record.size() > cap) {
            Node* lru = head->next;
            remove(lru);
            record.erase(lru->key);
            delete lru;
        }
    }

    void remove(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    void insert(Node* node) {
        Node* prev = tail->prev;
        prev->next = node;
        node->prev = prev;
        tail->prev = node;
        node->next = tail;
    }
};
