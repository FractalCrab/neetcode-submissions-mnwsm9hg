class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
          unordered_map<int, int> hash;

          for (int idx = 0; idx < nums.size(); ++idx){
               int complement = target - nums[idx];
               if (hash.find(complement) != hash.end())
                  return {hash[complement], idx};
                hash[nums[idx]] = idx;
        }
        return {};
        
    }


};
