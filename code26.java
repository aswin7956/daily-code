import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("This is a simple Calculator");
        int num1, num2;
        char operator;
        boolean loop = false;     // to store user choice initially tofalse
        do {                      // runs atleast once 
            System.out.println("Num1 : ");
            num1 = scanner.nextInt();         //   get operands
            System.out.println("Num2 : ");
            num2 = scanner.nextInt();
            System.out.println("operator : ");  // get operaor
            operator = scanner.next().charAt(0);
            switch (operator) {            // loop until user prompts to stop program execution
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
                    if (num2 != 0) {             // division by zero causes error
                        System.out.println(num1 / num2);
                    } else {
                        System.out.println("division by zero");
                    }
                    break;
                default:
                    System.out.println("invalid operator");
                    break;
            }
            System.out.println("Continue ? yes : no "); // prompt user to ask for continuation
            String res = scanner.next();  
            if (res.equalsIgnoreCase("yes")) {
                loop = true;
            }    
            if (res.equalsIgnoreCase("no")) {
                loop = false;
            }
        }while (loop);
    }
}
