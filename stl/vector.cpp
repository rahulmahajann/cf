#include<bits/stdc++.h>
#define vi vector<int>
#define pub push_back
#define pb pop_back

using namespace std;

int main(){
    
    vi vtr;

    vtr.pub(10);
    vtr.pub(100);
    vtr.pub(200);

    cout<<vtr[2]<<" "<<endl;
    // cout<<vtr.at(2)<<" "<<endl;

    for(int i=0 ; i<vtr.size() ; i++){
        cout<<vtr[i]<<" ";
    }

    cout<<endl;

    // cout<<vtr.size()<<endl;
    // cout<<vtr.capacity()<<endl;

// popback --> from the end of the vector 
// erase() --> removes the particular value from the vector

    vtr.erase(vtr.begin());

    for(int i=0 ; i<vtr.size() ; i++){
        cout<<vtr[i]<<" ";
    }
    
    cout<<"main answer! :) -->"<<endl;

    vi newv;
    for(int i=0; i<31; i++){
        newv.pub(i);
        cout<<newv.size()<<" "<<newv.capacity()<<endl;
    }

    return 0;
}