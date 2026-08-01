class Node {
public:
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v) {
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
        tail->prev = node;
        node->next = tail;
    }
public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {return -1;}
        Node* node = cache[key];
        remove(node);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            cache[key]->val = value;
            remove(cache[key]);
            insert(cache[key]);
            return;
        }
        Node* new_node = new Node(key, value);
        cache[key] = new_node;
        insert(new_node);
        if ((int)cache.size() > cap) {
            Node* lru = head->next;
            remove(lru);
            cache.erase(lru->key);
        }
    }
};
