class MinStack {
    vector<int> regular_stack;
    vector<int> min_stack;
public:
    MinStack() {}
    
    void push(int val) {
        regular_stack.emplace_back(val);
        val = std::min(val, min_stack.empty() ? val : min_stack.back());
        min_stack.emplace_back(val);
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
