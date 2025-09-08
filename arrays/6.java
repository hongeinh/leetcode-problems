// https://leetcode.com/problems/zigzag-conversion/description/
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 0) return "";
        if (numRows == 1) return s;
        if (numRows > s.length()) return s;


        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            rows.add(new StringBuilder());
        }

        int direction = 1; // down
        int curRow = 0;
        for (char c: s.toCharArray()) {
            rows.get(curRow).append(c);
            curRow += direction;
            if (curRow == numRows - 1) direction = -1;
            else if (curRow == 0) direction = 1;
        }

        return rows.stream().map(StringBuilder::toString).collect(Collectors.joining(""));
    }
}