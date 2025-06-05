class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        int n = nums.size();
        set<vector<int>> v;
        for(int i = 0 ; i < n ; i++)
        {
            int j = i+1, k = n-1;
            while(j < k)
            {
                int total = nums[i] + nums[j] + nums[k];
                if(total == 0 && i != j && i != k && j != k)
                {
                    v.insert({nums[i], nums[j], nums[k]});
                    // v.push_back(nums[i]);
                    // v.push_back(nums[j]);
                    // v.push_back(nums[k]);
                    j++;
                    k--;
                }
                else if(total < 0) j++;
                else if(total > 0) k--;
            }
        }
        for(auto i : v)
            ans.push_back(i);
        return ans;
    }
};