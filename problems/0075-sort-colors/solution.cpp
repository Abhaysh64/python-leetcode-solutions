class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero = 0, one = 0, two = size(nums) - 1;

    while (one <= two)
    {
        if (nums[one] == 0)
        {
            swap(nums[zero], nums[one]);
            zero++;
            one++;
        }
        else if (nums[one] == 1)
        {
            one++;
        }
        else
        {
            swap(nums[one], nums[two]);
            two--;
        }
    }
    }
};