#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,x;
        cin>>n>>x;
        int a[n];
        int s = 0;
        for (int i = 0; i < n; ++i){
            cin>>a[i];
            s += a[i];
        }
        int ns = s/x, ps = s%x;
        if (ps == 0)
            cout<<ns<<endl;
        else{
            int mn = a[0];
            for( int i = 0; i < n; ++i ){
                if (a[i]<mn)
                    mn = a[i];
            }
            if (mn <= ps)
                cout<<-1<<endl;
            else
                cout<<ns<<endl;
       
        }
    }
    return 0;
} 
