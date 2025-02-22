import java.util.*;

class Main {
    public int[] solution(String s) {
        String[] str = s.split(" ");
        String a=str[0];
        char b=str[1].charAt(0);
        int[] answer = new int[a.length()];

        int p = a.length();
        for (int i = 0; i < a.length(); i++) {
            if(a.charAt(i)==b){
                p=0;
                answer[i]=p;
            }
            else{
                p++;
                answer[i]=p;
            }
        }
        p=a.length();
        for(int i=a.length()-1; i>=0; i--){
            if(a.charAt(i)==b){
                p=0;
                answer[i]=p;
            }
            else{
                p++;
                answer[i]=Math.min(answer[i],p);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        for (int x : T.solution(s)) {
            System.out.print(x + " ");
        }
    }
}
