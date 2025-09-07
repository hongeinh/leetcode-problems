// https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> exists = new HashSet<>();

        int left = 0, right = 0;
        int n = s.length();
        int max = Integer.MIN_VALUE;

        while (right < n) {
            char c = s.charAt(right);
            if (!exists.contains(c)) {
                exists.add(c);
                right++;
                max = Math.max(max, right - left);
                continue;
            }
            // System.out.println("Before" + left + "->" + right);
            while (left < right && exists.contains(c)) {
                char toRemove = s.charAt(left);
                exists.remove(toRemove);
                left++;
            }
            // System.out.println("After" + left + "->" + right);
            exists.add(c);
            right++;
            
        }
        return !Objects.equals(max, Integer.MIN_VALUE) ? max : 0;
    }
}