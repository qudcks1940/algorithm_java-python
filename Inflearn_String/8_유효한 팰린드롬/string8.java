import java.util.*;

class Main{
  public String solution(String str){
    // String answer="NO";

    // String[] s = str.split(" ");
    // String sen="";
    // for(String x : s){
    //     for(char c : x.toCharArray()){
    //         if(Character.isAlphabetic(c)){
    //             sen+=c;
    //         }
    //     }
    // }

    // String tmp=new StringBuilder(sen).reverse().toString();
    // if(sen.equalsIgnoreCase(tmp)){
    //     answer="YES";
    // }
    // return answer;

    // GPT 코드
    int left = 0, right = str.length() - 1;
    
    while (left < right) {
      char leftChar = str.charAt(left);
      char rightChar = str.charAt(right);
      
      // 알파벳이 아닌 문자는 건너뛰기
      if (!Character.isLetter(leftChar)) {
        left++;
      } else if (!Character.isLetter(rightChar)) {
        right--;
      } else {
        // 대소문자 구분없이 비교
        if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
          return "NO";
        }
        left++;
        right--;
      }
    }
    
    return "YES";
  }

  public static void main(String[] args){
    Main T = new Main();
    Scanner sc = new Scanner(System.in);

    String str = sc.nextLine();

    System.out.println(T.solution(str));

  }
}