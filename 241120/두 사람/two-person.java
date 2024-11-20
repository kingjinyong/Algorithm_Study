import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] a = new String[2];
        String[] b = new String[2];

        a[0] = sc.next();
        a[1] = sc.next();
        b[0] = sc.next();
        b[1] = sc.next();
        if ((Integer.parseInt(a[0]) >= 19) && (a[1].equals("M")) || (Integer.parseInt(b[0]) >= 19) && (b[1].equals(
                "M"))) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}