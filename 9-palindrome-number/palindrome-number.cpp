class Solution {
public:
    bool isPalindrome(int x) {
        long long sum = 0;
        int temp = x;
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