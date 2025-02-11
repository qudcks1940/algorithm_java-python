import java.util.*;

class Main{
    public String solution(String str){
        String answer="";
        // HashSet<Character> set = new HashSet<>();
        // for(char x : str.toCharArray()){
        //     if(set.contains(x)){
        //         continue;
        //     }
        //     else{
        //         set.add(x);
        //         answer+=x;
        //     }
        // }
        for(int i=0; i<str.length(); i++){
          if(str.indexOf(str.charAt(i))==i){
            answer+=str.charAt(i);
          }
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