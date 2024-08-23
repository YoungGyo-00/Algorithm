package 프로그래머스.kakao;

public class 신규아이디 {
    class Solution {
        public String solution(String new_id) {
            String answer = "";
            
            // 1. 대문자를 소문자로
            new_id = new_id.toLowerCase();
            
            // 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 제외 제거
            for (int i = 0; i < new_id.length(); i++) {
                char ch = new_id.charAt(i);
                if (Character.isAlphabetic(ch) || Character.isDigit(ch) || ch == '-' || ch == '_' || ch == '.') {
                    answer += ch;
                }
            }
            
            // 3. 마침표(.) 2개 이상이면 하나의 마침표로
            while (answer.indexOf("..") != -1) {
                answer = answer.replace("..", ".");
            }
            
            // 4
            if (!answer.isEmpty() && answer.charAt(0) == '.') {
                answer = answer.substring(1);
            }
            if (!answer.isEmpty() && answer.charAt(answer.length() - 1) == '.') {
                answer = answer.substring(0, answer.length() - 1);
            }
            
            // 5
            if (answer.isEmpty()) {
                answer = "a";
            }
            
            // 6
            if (answer.length() > 15) {
                answer = answer.substring(0, 15);
                if (answer.charAt(answer.length() - 1) == '.') {
                    answer = answer.substring(0, answer.length() - 1);
                }
            }
        
            // 7
            while (answer.length() < 3) {
                answer += answer.charAt(answer.length() - 1);
            }
            return answer;
        }
    }
}
