import java.util.Arrays;
import java.util.Scanner;

class Tester{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputLine = sc.nextLine();
        sc.close();
        String[] inputStringObjects = inputLine.split("#");
        int[] arr = Arrays.stream(inputStringObjects[0].split(",")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(arr);
        int e = Integer.parseInt(inputStringObjects[1]);
        System.out.println(Util.binarySearch(arr, e));
    }
}