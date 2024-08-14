import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main {
    public static int check(String[] board, int row, int column, char color) {
        int check = (row + column) % 2;
        int count = 0;

        for (int i = row; i < row + 8; i++) {
            for (int j = column; j < column + 8; j++) {
                if ((i + j) % 2 == check && color != board[i].charAt(j)) {
                    count++;
                }
                if ((i + j) % 2 != check && color == board[i].charAt(j)) {
                    count++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] board = new String[n];

        for (int i = 0; i < n; i++) {
            board[i] = br.readLine();
        }

        int min = Integer.MAX_VALUE;

        for (int i = 0; i < n - 7; i++) {
            for (int j = 0; j < m - 7; j++) {
                int count_w = check(board, i, j, 'W');
                int count_b = check(board, i, j, 'B');
                min = Math.min(min, Math.min(count_w, count_b));
            }
        }

        System.out.println(min);
    }
}