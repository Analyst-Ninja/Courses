#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    vector <int> vec = {1,-3,6,7,8,-10};
    int n = vec.size();
    int currSum = 0, maxSum = INT_MIN;

    for (int i=0; i<n; i++) {
        currSum+=vec[i];
        maxSum=max(maxSum,currSum);
        if (currSum<0) {
            currSum=0;
        }
    }
    cout << "Max Sum of SubArray " << maxSum << endl;
}