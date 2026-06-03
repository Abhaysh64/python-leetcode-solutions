class Solution {
public:
    bool canJump(vector<int>& nums) {
        int final_pos=nums.size()-1;
        for(int i=nums.size()-2;i>=0;i--)
        {
            if(i+nums[i]>=final_pos)
            {
                final_pos=i;
            }
        }

        return final_pos==0;
    }
};