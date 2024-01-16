public class Solution {
    public int SmallestEvenMultiple(int n) {
        return n % 2 == 1 ? n * 2 : n;
    }
}