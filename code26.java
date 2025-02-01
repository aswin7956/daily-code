import java.util.Scanner;

public class SimpleCalculatorDoWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num1, num2;
        char operator;
        boolean loop;  // initialized default value false unlike previous program
        do {          // executes once always
            System.out.println("Num1 : ");
            num1 = scanner.nextInt();         //   get operands
            System.out.println("Num2 : ");
            num2 = scanner.nextInt();
            System.out.println("operator : ");  // get operaor
            operator = scanner.next().charAt(0);
            switch (operator) {         // switch case for operatoions
                case '+':
                    System.out.println(num1 + num2);
                    break;
                case '-':
                    System.out.println(num1 - num2);
                    break;
                case '*':
                    System.out.println(num1 * num2);
                    break;
                case '/':
                    if (num2 != 0) {      // handling error thrown
                        System.out.println(num1 / num2);
                    } else {
                        System.out.println("division by zero");
                    }
                    break;
                default:                             // default to handle other inputs
                    System.out.println("Invalid operator.");
                    break;
            }
            System.out.println("Continue ? yes : no ");
            String res = scanner.next();      // prompt user to ask for continuation
            if (res.equalsIgnoreCase("no")) {
                loop = false;
            }
    }
}
