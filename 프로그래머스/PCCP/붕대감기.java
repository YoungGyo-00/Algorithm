
// 붕대 감기
import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = -1;
        int count = 0;
        int index = 0;
        int t = 0;
        int max_health = health;

        while (index < attacks.length) {
            t++;
            // 1. health가 0보다 작으면 break
            if (health <= 0) {
                break;
            }

            // 2. 시간이랑 attacks[index][0] 이랑 같으면 health 감소
            if (t == attacks[index][0]) {
                health -= attacks[index][1];
                index++;
                count = 0;
                continue;
            }

            // 3. health 회복
            health += bandage[1];
            count++;
            if (count == bandage[0]) {
                health += bandage[2];
                count = 0;
            }

            if (health > max_health) {
                health = max_health;
            }
        }

        if (health > 0) {
            answer = health;
        }

        return answer;
    }
}