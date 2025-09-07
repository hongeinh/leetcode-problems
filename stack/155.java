// https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150
class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> prevMins;
    private Integer prevMin;

    public MinStack() {
        stack = new Stack<>();
        prevMins = new Stack<>();
        prevMin = Integer.MAX_VALUE;
        
    }
    
    public void push(int val) {
        stack.push(val);
        prevMin = Math.min(prevMin, val);
        prevMins.push(prevMin);
    }
    
    public void pop() {
        if (stack.isEmpty()) return;
        stack.pop();
        prevMins.pop();
        prevMin = prevMins.isEmpty() ? Integer.MAX_VALUE : prevMins.peek();
    }
    
    public int top() {
        if (stack.isEmpty()) return Integer.MIN_VALUE;
        return stack.peek();
    }
    
    public int getMin() {
        if (prevMins.isEmpty()) return Integer.MIN_VALUE;
        return prevMins.peek();
    }
}
