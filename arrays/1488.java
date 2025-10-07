// https://leetcode.com/problems/avoid-flood-in-the-city/description/
class Solution {
    public int[] avoidFlood(int[] rains) {
        int n = rains.length;
        int[] ans = new int[n];
        Arrays.fill(ans, 1);
        
        TreeSet<Integer> sunnyDays = new TreeSet<>();
        Map<Integer, Integer> lastRainedOnLake = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (rains[i] == 0) {
                sunnyDays.add(i);
                continue;
            }
            ans[i] = -1;
            if (lastRainedOnLake.containsKey(rains[i])) {
                Integer nearestSunnyDay = sunnyDays.ceiling(lastRainedOnLake.get(rains[i]));
                if (nearestSunnyDay == null) return new int[0];
                ans[nearestSunnyDay] = rains[i];
                sunnyDays.remove(nearestSunnyDay);
            }
            lastRainedOnLake.put(rains[i], i);
        }
        return ans;
    }
}