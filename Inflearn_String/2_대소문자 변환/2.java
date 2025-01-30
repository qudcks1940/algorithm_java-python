import java.util.Scanner;

class change {
    public String solution(String str) {
        String answer = "";
//        for(char x:str.toCharArray()){
//            if(Character.isLowerCase(x)){
//                answer+=Character.toUpperCase(x);
//            }
//            else{
//                answer+=Character.toLowerCase(x);
//            }
//        }

        for(char x:str.toCharArray()){
            if(97<=x && x<=122){
                answer+=(char)(x-32);
            }
            else{
                answer+=(char)(x+32);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        change T = new change();
        Scanner sc = new Scanner(System.in);
        String str=sc.next();
        System.out.print(T.solution(str));
    }

}
