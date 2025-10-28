// https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public String simplifyPath(String path) {
        String[] dirs = path.split("/");
        Stack<String> shortened = new Stack<>();
        for (String dir : dirs) {
            if (dir.isEmpty() || dir.equals("."))
                continue;
            if (dir.equals("..")) {
                if (!shortened.isEmpty()) shortened.pop();
                continue;
            }
            shortened.push(dir);
        }
        return "/" + String.join("/", shortened);
    }
}