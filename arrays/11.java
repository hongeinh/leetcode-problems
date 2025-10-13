// https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;

        int maxArea = 0;
        while (left < right) {
            int cur = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, cur);
            if (height[left] >= height[right]) right--;
            else left++;
        }
        return maxArea;
    }
}