import java.util.*;
class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> hs = new HashMap<>();
        for (int num : nums){
            if (!hs.containsKey(num)){
                hs.put(num, 1);
            }
            else {
                hs.put(num, hs.get(num) + 1);
            }
        }
        
        int compareA = nums.length/2;
        int compareB = hs.size();

        return Math.min(compareA, compareB);
        
    }
}
