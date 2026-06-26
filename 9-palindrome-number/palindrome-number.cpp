class Solution {
public:
    bool isPalindrome(long long x) {
        long long sum = 0;
        long long temp = x;
        while (x>0) {
            sum = sum * 10 + (x % 10);
            x /= 10;
        }
        if (temp == sum){
            return true;
        }
        else
            return false;
    }
};