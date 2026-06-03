class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> cnt;
        int n = nums.size();
        for(int i = 0; i <n;i++){
            cnt[nums[i]]++;
        }
        for(auto i: cnt){
            if(i.second > (n/2)) return i.first;
        }
        return -1;
    }
};