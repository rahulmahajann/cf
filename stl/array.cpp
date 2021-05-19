#include<bits/stdc++.h>
using namespace std;

int main(){
    
    array<int,5> arraym;

    arraym={1,2,3,4,5};

    cout<<arraym.at(3)<<" "<<"--> element at 3rd index"<<endl;
    cout<<arraym[2]<<" "<<"--> element at 2nd index"<<endl;
    cout<<arraym.front()<<" "<<"--> element at first position"<<endl;
    cout<<arraym.back()<<" "<<"--> element at last position"<<endl;
    cout<<arraym.data()<<" "<<"--> pointer of the array"<<endl;

    array<char,10> arrayn;
    arrayn.fill('a');
    // cout<<arrayn[1];

    for(int i=0 ; i<arrayn.size() ; i++){
        cout<<arrayn[i]<<" ";
    }

    return 0;
}