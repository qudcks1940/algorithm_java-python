import java.util.*;

class Main{
    public String solution(String s){
        StringBuilder answer=new StringBuilder();

        int count=1;
        for(int i=1;i<s.length();i++){
            if(s.charAt(i)==s.charAt(i-1)){
                count++;

            }
            else{
                answer.append(s.charAt(i-1));
                if(count!=1){
                    answer.append(count);
                }
                count=1;
            }
        }
        answer.append(s.charAt(s.length()-1));
        if(count!=1){
            answer.append(count);
        }

        return answer.toString();
    }

    public static void main(String[] args){
        Main T =new Main();
        Scanner sc=new Scanner(System.in);

        String s = sc.next();

        System.out.println(T.solution(s));
    }
}