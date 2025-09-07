// https://leetcode.com/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, String current, int open, int close, int max) {
        // if the string is complete
        if (current.length() == max * 2) {
            result.add(current);
            return;
        }

        // add "(" if we still have open brackets left
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }

        // add ")" if valid (only if close < open)
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
        }
    }
}