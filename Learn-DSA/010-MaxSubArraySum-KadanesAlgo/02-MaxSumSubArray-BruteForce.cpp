#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    vector <int> vec = {1,-3,6,7,8,-10};
    int n = vec.size();
    int maxSum = INT_MIN;
    for(int st=0; st<n; st++){
        int currSum = 0;
        for(int end=st; end<n; end++) {
            currSum+=vec[end];
            if(currSum > maxSum) {
                maxSum = currSum;
            }
        } 
    }
    cout << maxSum << endl;
}