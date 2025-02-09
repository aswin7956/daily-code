public class Main {
    public static int hillWeight(int N, int W, int D) {
        int tot = 0;
        int x = W;
        for (int i = 0; i < N; i++) {
            for (int s = 0; s < N - i - 1; s++) {
                System.out.print("  ");
            }
            for (int j = 0; j <= i; j++) {
                tot += x;
                System.out.print(x + " ");
            }
            System.out.println(); 
            x += D;
        }
        return tot;
    }
    public static void main(String[] args) {
        int tot = hillWeight(5, 10, 2);
        System.out.println("Total Weight: " + tot);
    }
}
