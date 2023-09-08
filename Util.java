//Binary Search

class Util {
    public static boolean binarySearch(int[] arr, int e) {
        int low = 0;
        int high = arr.length - 1;
        int mid = 0;
        boolean flag = false;
        while (low <= high) {
            mid = (int) Math.floor((low + high) / 2.0);
            if (arr[mid] == e){
                flag = true;
                break;
            }
            else if (arr[mid] < e) {
                low = mid + 1;
                continue;
            } else {
                high = mid - 1;
                continue;
            }
        }
        return flag;
    }
}