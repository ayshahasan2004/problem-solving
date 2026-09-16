import java.util.ArrayList;
import java.util.List;

    ///////Design an algorithm to encode a list of strings to a string.
    ///////The encoded string is then sent over the network and is decoded back to
    ///////the original list of strings.
import java.util.Arrays;
import java.util.List;

public class EncodeandDecodeStrings {

    public static void main(String[] args) {

        EncodeandDecodeStrings outer = new EncodeandDecodeStrings();
        Solution solution = outer.new Solution();

        List<String> strs = Arrays.asList("hello", "world", "java");
        String encoded = solution.encode(strs);
        System.out.println("Encoded: " + encoded);

        List<String> decoded = solution.decode(encoded);
        System.out.println("Decoded: " + decoded);
    }

    public class Solution {

        public String encode(List<String> strs) {
            if (strs.isEmpty()) return "";

            StringBuilder res = new StringBuilder();
            List<Integer> sizes = new java.util.ArrayList<>();

            for (String str : strs) {
                sizes.add(str.length());
            }

            for (int size : sizes) {
                res.append(size).append(',');
            }

            res.append('#');

            for (String str : strs) {
                res.append(str);
            }

            return res.toString();
        }

        public List<String> decode(String str) {
            if (str.length() == 0) {
                return new java.util.ArrayList<>();
            }

            List<String> res = new java.util.ArrayList<>();
            List<Integer> sizes = new java.util.ArrayList<>();

            int i = 0;

            while (str.charAt(i) != '#') {
                StringBuilder cur = new StringBuilder();

                while (str.charAt(i) != ',') {
                    cur.append(str.charAt(i));
                    i++;
                }

                sizes.add(Integer.parseInt(cur.toString()));
                i++;
            }

            i++;

            for (int sz : sizes) {
                res.add(str.substring(i, i + sz));
                i += sz;
            }

            return res;
        }
    }
}