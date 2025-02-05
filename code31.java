import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter P ");
        double principal = sc.nextDouble();
        System.out.print("Enter T in years ");
        double time = sc.nextDouble();
        System.out.print("Enter R ");
        double rate = sc.nextDouble();        // getting all user input as double as values can be very ihigh or floating points
        double simpleInterest = (principal * time * rate) / 100; // formula ptr/100 where t is in years
        System.out.println("SI " + simpleInterest);
        double amount = simpleInterest+principal; // Amount = simple interest + principal
        System.out.println("Total Amount " + amount);
    }
}

