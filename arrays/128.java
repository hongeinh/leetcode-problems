// https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length < 2) return nums.length;
        
        Set<Integer> uniques = new HashSet<>();
        for (int num: nums) {
            uniques.add(num);
        }
        
        int longest = 1; 

        for (int num: uniques) {
            // ignore if current num is not start of the sequence
            if (uniques.contains(num - 1)) continue;
            int len = 1;
            int cur = num;
            while (uniques.contains(cur + 1)) {
                len++;
                cur++;
            }
            longest = Math.max(longest, len);
        }
        return longest;

        
    }
}


// class Solution {
//     public int longestConsecutive(int[] nums) {
//         if (nums.length < 2) return nums.length;
//         PriorityQueue<Integer> minHeap = new PriorityQueue<>();

//         for (int num: nums) {
//             minHeap.add(num);
//         }

//         int longest = 1;
//         int len = 1;
//         int prev = minHeap.poll();

//         while (!minHeap.isEmpty()) {
//             int cur = minHeap.poll();
//             if (cur == prev) {
//                 continue;
//             } else if (cur == prev + 1) {
//                 len++;
//                 longest = Math.max(longest, len);
//             } else {
//                 len = 1;
//             }
//             prev = cur;

//         }
//         return longest;

        
//     }
// }