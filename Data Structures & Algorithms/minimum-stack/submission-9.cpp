class MinStack {
    stack<int> regular_stack;
    stack<int> min_stack;
public:
    MinStack() {}
    
    void push(int val) {
        regular_stack.push(val);
        val = std::min(val, min_stack.empty() ? val : min_stack.top());
        min_stack.push(val);
    }
    
    void pop() {
        min_stack.pop();
        regular_stack.pop();
    }
    
    int top() {
        return regular_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};
