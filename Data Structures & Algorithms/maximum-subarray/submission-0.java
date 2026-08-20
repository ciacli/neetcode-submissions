class Solution {
    public int findMaxMidSection(int nums[], int lb, int ub, int mid){
        int leftMax = nums[mid - 1];
        int rightMax = nums[mid];
        int sum = 0;
        for(int i = mid - 1; i >= lb; -- i){
            sum += nums[i];
            if(sum > leftMax) leftMax = sum;
        }
        sum = 0;
        for(int i = mid; i < ub; ++ i){
            sum += nums[i];
            if(sum > rightMax) rightMax = sum;
        }
        return leftMax + rightMax;
    }
    public int dei(int[] nums, int lb, int ub){
        if(lb == ub - 1) return nums[lb];
        else{
            int mid = (lb + ub) / 2;
            int midSection = findMaxMidSection(nums, lb, ub, mid);
            int left = dei(nums, lb, mid);
            int right = dei(nums, mid, ub);
            int max = midSection;
            if(max < left) max = left;
            if(max < right) max = right;
            return max;
        }
    }
    public int maxSubArray(int[] nums) {
        return dei(nums, 0, nums.length);
    }
}
