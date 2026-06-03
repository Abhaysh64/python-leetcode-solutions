class Solution {
public:

    int binarySearch(vector<int>&nums ,int left, int right, int target) {

        // If target value not found return -1.
        if(left > right)
            return -1;

        // We will use index of the array to find the value.
        int mid = (left+right)/2;


        // Target value found
        if(nums[mid] == target)
            return mid;

        // Divide the array into sub-arrays and proceed to that su-array according to target value. 
        // As the array is sorted, if the target value is more than mid value of current sub-array 
        // that means the given target value might be present in the sub-array with index greater than mid. 
        if(target > nums[mid])
            return binarySearch(nums, mid+1, right, target);
        else
            return binarySearch(nums, left, mid-1, target);
    }

    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
};