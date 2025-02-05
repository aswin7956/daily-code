import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {      // whitespace logic increases by 1 
                System.out.print(" ");
            }
            for (int j = 0; j < (2 * (n - i) - 1); j++) { // odd number logic for stars
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = n - 2; i >= 0; i--) { // lower half
            for (int j = 0; j < i; j++) {
                System.out.print(" ");  // spaces decrement by 1 each line
            }
            for (int j = 0; j < (2 * (n - i) - 1); j++) { // odd number logic for start
                System.out.print("*");
            }
            System.out.println();
        }
    }
}