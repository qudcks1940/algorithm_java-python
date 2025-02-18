import java.util.*;

class Main{
    public int solution(String str){
        int answer;
//        내가 푼 코드
//        String tmp="";
//        for(char x:str.toCharArray()){
//            if(!Character.isAlphabetic(x)){
//                tmp+=x;
//            }
//        }
//
//        answer=Integer.parseInt(tmp);

//        GPT 코드
        StringBuilder sb=new StringBuilder();
        for(char c:str.toCharArray()){
            if(Character.isDigit(c)){
                sb.append(c);
            }
        }
        answer=Integer.parseInt(sb.toString());

        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner sc= new Scanner(System.in);
        String str=sc.next();

        System.out.println(T.solution(str));
    }
}