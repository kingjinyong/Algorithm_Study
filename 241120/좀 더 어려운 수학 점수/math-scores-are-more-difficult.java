import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = new int[2];
        int[] b = new int[2];

        a[0] = sc.nextInt();
        a[1] = sc.nextInt();
        b[0] = sc.nextInt();
        b[1] = sc.nextInt();

        if (a[0] > b[0]) {
            System.out.println("A");
        } else if (a[0] < b[0]) {
            System.out.println("B");
        } else {
            if (a[1] > b[1]) {
                System.out.println("A");
            } else if (a[1] < b[1]) {
                System.out.println("B");
            }
        }
    }
}