#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,e;
    cin>>n>>e;

    vector<int> adj[n+1];

    for(int i=0;i<e;i++){
        int u,v;
        cin>>u>>v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // cout<<adj;
    // for(int j=0; j<adj.size(); j++){
    //     cout << adj.at(j);
    // }
    cout << adj[0];
    // cout<<2;

    return 0;
}

// 5 7
// 1 2
// 1 5
// 1 3
// 3 5
// 2 3
// 2 4
// 3 4