#include <bits/stdc++.h>
using namespace std;
vector<char> v;
int alpa[26];
int main(){
    string s;
    cin >> s;

    for (char c : s){
        v.push_back(c);
    }

    for (char c : v){
        int i = (int) c - 97;
        alpa[i] += 1;
    }

    for (int i = 0; i < 26; i++){
        cout << alpa[i] << " ";
    }
    return 0;
}
// 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
// 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0                                   