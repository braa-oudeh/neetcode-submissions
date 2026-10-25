
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> sett = new HashSet<>();

        for (int i = 0; i < nums.length; i++)
        {
            if (sett.contains(nums[i]))
            {
                return true;
            }

            else
            {
                sett.add(nums[i]);
            }
        }
        return false;
    }
}