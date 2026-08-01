class Node {
public:
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k = 0, int v = 0) {
        key = k;
        val = v;
        prev = nullptr;
        next = nullptr;
    }
};

class LRUCache {
private:
    int cap;
    unordered_map<int, Node*> cache;
    Node* head;
    Node* tail;
    
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
        node->next = tail;
        tail->prev = node;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {return -1;}
        Node* target = cache[key];
        remove(target);
        insert(target);
        return target->val;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            cache[key]->val = value;
            remove(cache[key]);
            insert(cache[key]);
            return;
        }
        Node* new_node = new Node(key, value);
        insert(new_node);
        cache[key] = new_node;
        if ((int)cache.size() > cap) {
            Node* lru = head->next;
            remove(lru);
            cache.erase(lru->key);
        }
    }
};
