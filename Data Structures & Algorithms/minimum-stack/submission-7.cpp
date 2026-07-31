class MinStack {
    vector<int> regular_stack;
    vector<int> min_stack;
public:
    MinStack() {}
    
    void push(int val) {
        if (min_stack.empty()) {
            min_stack.emplace_back(val);
        } else {
            min_stack.emplace_back(std::min(min_stack.back(), val));
        }
        regular_stack.emplace_back(val);
    }
    
    void pop() {
        min_stack.pop_back();
        regular_stack.pop_back();
    }
    
    int top() {
        return regular_stack.back();
    }
    
    int getMin() {
        return min_stack.back();
    }
};
