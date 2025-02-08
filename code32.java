import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("num1: ");
        int num1 = sc.nextInt();
        System.out.print("num2: ");
        int num2 = sc.nextInt();
        hcf(num1,num2);
        lcm(num1,num2);
    }
    static void hcf(int num1, int num2){
        int hcf = 1;          // initializing hcf as 1 , worst case its 1
        int min = Math.min(num1, num2); // factor will always be lesser than smaller number
        for (int i = min; i >=1; i--) {     
            if (num1 % i == 0 && num2 % i == 0) { // looking for greatest factor decrementing the smaller number
                hcf = i;
                break;
            }
        }
        System.out.println("HCF: "+hcf);
    }
    static void lcm(int num1,int num2){
         int max = Math.max(num1, num2);  // multiple greater than larger number
        int lcm = max;
        while (true) { 
            if (lcm % num1 == 0 && lcm % num2 == 0) { // first multiple is the least
                break;
            }
            lcm += max;  // tables of max element
        }
        System.out.println("LCM: "+lcm);
    }
}