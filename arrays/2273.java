// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13
class Solution {
    public List<String> removeAnagrams(String[] words) {
        int n = words.length;
        int [] prev = null;
        List<String> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int[] frequencies = new int[26];
            for (char c: words[i].toCharArray()) {
                frequencies[c - 'a']++;
            }
            if (prev == null || (!Arrays.equals(frequencies, prev))) {
                prev = frequencies;
                res.add(words[i]);
            } 

        }
        return res;

    }
}