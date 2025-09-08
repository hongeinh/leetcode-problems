// https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public String intToRoman(int num) {
        Map<Integer, String> conversions = converter();

        int base = 1;
        List<String> result = new ArrayList<>();
        while (num > 0) {
            int remainder = num % 10;
            // System.out.println("num=" + num + " base=" + base + " remainder=" + remainder);

            int required = remainder * base;
            if (conversions.containsKey(required)) {
                result.add(conversions.get(required));
            } else if (remainder == 4) {
                result.add(conversions.get(base) + conversions.get(base * 5));
            } else if (remainder == 9) {
                result.add(conversions.get(base) + conversions.get(base * 10));
            } else if (remainder < 4) {
                String value = "";
                for (int i = 1; i <= remainder; i++) {
                    value += conversions.get(base);
                }
                result.add(value);
            } else {
                String value = conversions.get(base * 5);
                for (int i = 6; i <= remainder; i++) {
                    value += conversions.get(base);
                }
                result.add(value);
            }
            num = (num - remainder) / 10;
            base *= 10;
        }        
        Collections.reverse(result);
        return String.join("", result);
    }


    private Map<Integer, String> converter() {
        Map<Integer, String> conversions = new HashMap<>();
        conversions.put(1, "I");
        conversions.put(5, "V");
        conversions.put(10, "X");
        conversions.put(50, "L");
        conversions.put(100, "C");
        conversions.put(500, "D");
        conversions.put(1000, "M");
        return conversions;
    }
}