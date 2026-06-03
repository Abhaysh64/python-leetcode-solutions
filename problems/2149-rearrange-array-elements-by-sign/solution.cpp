class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> pos;
	    vector<int> neg;
        vector<int> ans;
	    for(int i=0; i<nums.size(); i++){
	       if(nums[i]<0) neg.push_back(nums[i]);
	       else pos.push_back(nums[i]);
	   }
       int i=0;
	   int j=0, k=0;
	   while(i<nums.size()){
	       if(j<pos.size()){
	           ans.push_back(pos[j]);
	           i++;
	           j++;
	       } 
	       if(k<neg.size()){
	           ans.push_back(neg[k]);
	           i++;
	           k++;
	       }
	   }
       return ans;

    }
};