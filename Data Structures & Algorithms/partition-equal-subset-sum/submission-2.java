class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0, len = nums.length;
        for(int i = 0; i < len; ++i){
            sum += nums[i];
        }
        if(sum % 2 == 1) return false;
        int capacity = sum / 2;
        int dp[][] = new int[len][capacity + 1];
        for(int i = 1; i <= capacity; ++ i){
            if(nums[0] == i) dp[0][i] = 1;
            else dp[0][i] = 0;
        }
        for(int i = 1; i < len; ++ i){
            for(int j = 1; j <= capacity; ++ j){
                int isTrue = j - nums[i] > 0 ? dp[i - 1][j - nums[i]] : 0;
                dp[i][j] = Math.max(dp[i - 1][j], isTrue);
            }
        }
        return dp[len - 1][capacity] == 1;
    }
}
