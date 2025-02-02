import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int n=7;
        int mid=n/2;   // to store half
        for (int i = 0; i <= mid; i++) {   // upper half of diamond
            for (int j = 0; j < mid - i; j++) { // whitespaces 
                System.out.print(" ");
            }
            for (int j = 0; j < (2 * i + 1); j++) { // odd number logic 1 3 5
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = 0; i <= mid; i++) { // lower half
            for (int j = 0; j < i; j++) { // whitespace logic 
                System.out.print(" ");
            }
            for (int j = 0; j < (n - 2 * i); j++) {  // odd number logic in reverse  5 3 1
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
