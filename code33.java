public class Main {
    public static int hillWeight(int N, int W, int D) {
        int tot = 0; // total weight
        int x = W; // initial weight in each row
        for (int i = 0; i < N; i++) {
            for (int s = 0; s < N - i - 1; s++) {  // whitespace logic
                System.out.print("  ");
            }
            for (int j = 0; j <= i; j++) { // hill logic
                tot += x; // add weight to toal iterating the row
                System.out.print(x + " ");
            }
            System.out.println(); 
            x += D; // increment weight by D
        }
        return tot;
    }
    public static void main(String[] args) {
        int tot = hillWeight(5, 10, 2);
        System.out.println("Total Weight: " + tot);
    }
}
