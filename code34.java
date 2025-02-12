public class Main {
    public static String lcs(String s1, String s2) {
        String LCS = ""; // emoty string to store final res
        for (int i = 0; i < s1.length(); i++) { // iterate over first str
            for (int j = i + 1; j <= s1.length(); j++) { // iterate i+1 to end
                String substr = s1.substring(i, j); // get all possible substrings
                //System.out.println(substr);// 
                if (s2.contains(substr) && substr.length() > LCS.length()) { // if substr found and is greater than current max length
                    //System.out.println(substr);
                    LCS = substr; // update
                }
            }
        }
        return LCS;
    }

    public static void main(String[] args) {
        String s1 = "abcdef";
        String s2 = "zabcdf";
        String result = lcs(s1, s2);
        System.out.println("Longest Common Substring: " + result);
    }
}
