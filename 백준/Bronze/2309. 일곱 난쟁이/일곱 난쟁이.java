import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static boolean found = false;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 9;
        int[] arr = new int[n];

        for (int i= 0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int[] result = new int[7];

        combination(arr, result, 0, 0);
    }

    static void combination(int[] arr, int[] result, int start, int depth){
        if (found) return;

        if (depth == 7){
            // result 합 계산해서 100 나오는거 출력
            if (Arrays.stream(result).sum() == 100){
                found = true;
                Arrays.sort(result);
                for (int i = 0; i < result.length; i++) {
                    System.out.println(result[i]);
                }
            }
            return;
        }
        for (int i = start; i < arr.length; i++){
            result[depth] = arr[i];
            combination(arr, result, i + 1, depth + 1);
        }
    }


}