import java.util.Scanner;
public class Main {
    public static void generatePasswords(int n, int l) {
        for (int d1 = 1; d1 <= n; d1++) {   // 1 to n
            for (int d2 = 1; d2 <= n; d2++) { // 1 to n
                for (char ch1 = 'a'; ch1 < 'a' + l; ch1++) {  // char from a to givel length of char
                    for (char ch2 = 'a'; ch2 < 'a' + l; ch2++) { // char from a to givel length of char
                        for (int d3 = Math.max(d1, d2) + 1; d3 <= n; d3++) { // number greater than mac of n1,n2
                            System.out.print("" + d1 + d2 + ch1 + ch2 + d3 + " ");  //use quotes to convert to string and space to give spaces between consecutive passwords
                        }
                    }
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter n:");
        int n = scanner.nextInt();
        System.out.print("Enter l:");
        int l = scanner.nextInt();
        generatePasswords(n, l);
        scanner.close();
    }
}

//Program 2 factorial using java

/* import java.util.Scanner;
public class Main {
    public static long fact(int n) {
        if (n == 0 || n == 1)   // 0! = 1 also 1! =1 the base case
        return 1;
        return n * fact(n - 1);  // current number fact = fact of previous number
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(fact(num));
        scanner.close();
    }
}
*/
