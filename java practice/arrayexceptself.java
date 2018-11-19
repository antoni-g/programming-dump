class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] out = new int[nums.length];
        out[nums.length-1] = nums[nums.length-1];
        for (int i = nums.length-2; i >= 1; i--) {
            out[i] = nums[i]*out[i+1];
        }        
        int left = 1;
        for (int i = 0; i < nums.length-1; i++) {
            out[i] = left*out[i+1];
            System.out.println(left);
            left*= nums[i];
        }
        out[nums.length-1] = left;
        return out;
    }
    
}

public class arrayexceptself {
    public static void main(String[] args) {
        int[] check = {1,2,3,4};
        Solution out = new Solution();
        int[] re = out.productExceptSelf(check);
        for (int el : re) {
            System.out.print(el + " ");
        }
        System.out.println();
    }
}