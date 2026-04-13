using big_int = long long int;
class Solution {
public:
    big_int helper(int n, unordered_map< int, big_int>& cache) {
        if (n <= 2) return n;

        auto it = cache.find(n);
        if (it != cache.end()) return it->second;
        big_int a = helper(n - 1, cache);
        big_int b = helper(n - 2, cache);
        big_int ans = a + b;
        cache[n] = ans;
        return ans;
    }

    big_int climbStairs(int n) {
        unordered_map<int, big_int> cache;   
        return helper(n, cache);        
    }
};
