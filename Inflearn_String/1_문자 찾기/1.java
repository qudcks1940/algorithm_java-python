import java.util.*;

class Main{
    // main은 static 메소드
    // solution은 instance, non static 메소드로 했다.
    // static에서 인스턴스 메서드 호출하려면 객체 생성해야함.
    public int solution(String str, char t){
        int answer=0;
        str=str.toUpperCase();
        t=Character.toUpperCase(t);
        for(char x:str.toCharArray()){
            if(x==t) answer++;
        }
        //메모리 효율이 중요한 경우: charAt() 사용 (공간복잡도가 더 낮음).
        //가독성과 편의성 중시: toCharArray() 사용 (문자 배열을 다루기가 더 직관적).
//        for(int i=0; i<str.length(); i++){
//            if(str.charAt(i)==t)
//                answer++;
//        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        //문자열 입력
        char c=sc.next().charAt(0);
        //문자 하나 입력
        System.out.println(T.solution(str,c));
    }
}