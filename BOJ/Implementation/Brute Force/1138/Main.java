import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("test");
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (cnt == arr[i] && answer[j] == 0) {
                    answer[j] = i + 1;
                    break;
                } else if (answer[j] == 0) {
                    cnt++;
                }
            }
        }
        for (int i = 0; i < n; i++)
            System.out.println(answer[i] + " ");
    }
}