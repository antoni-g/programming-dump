import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Integer[] init = new Integer[nums.length];
        Arrays.fill(init, null);
        recurse(0,init,nums,ret);
        return ret;
    }
    
    void recurse(int index, Integer[] curr, int[] nums, List<List<Integer>> ret) {
        // make list if done
        if (index == nums.length) {
            ArrayList<Integer> ne = new ArrayList<Integer>();
            for (int i : curr) {
                ne.add(i);
            }
            ret.add(ne);
        }
        else {
            for (int i = 0; i < nums.length; i++) {
                if (!myContains(curr,nums[i])) {
                    Integer[] copy = new Integer[nums.length]; 
                    System.arraycopy(curr, 0, copy, 0, nums.length);
                    copy[index] = nums[i];
                    recurse(index+1, copy, nums, ret);
                }  
            }
        }
    }
    
    public static boolean myContains(final Integer[] array, final int v) {
        boolean result = false;
        for (int i = 0; i < array.length; i++) {
            if(array[i] != null){
                if (array[i] == v) {
                    result = true;
                    break;
                }
            }
        }
        return result;
    }
}
public class permutations {
    public static void main(String[] args) {
        int[] check = {0,1};
        Solution out = new Solution();
        List<List<Integer>> re = out.permute(check);
        for (List<Integer> el : re) {
            for (Integer i : el) {
                System.out.print(i + " ");
            } 
            System.out.println("\n");
        }
    }
}