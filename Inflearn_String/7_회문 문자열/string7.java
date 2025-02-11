import java.util.*;

class Main{
    public String solution(String str){
//        String answer="YES";
//        str=str.toUpperCase();
//        int len=str.length();
//        for(int i=0; i<len/2; i++){
//            if(str.charAt(i)!=str.charAt(len-i-1)){
//                return "NO";
//            }
//        }
        String answer="NO";
        String tmp=new StringBuilder(str).reverse().toString();
        if(str.equalsIgnoreCase(tmp)){
           answer="YES";
        }
        return answer;
    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        System.out.println(T.solution(str));
    }
}