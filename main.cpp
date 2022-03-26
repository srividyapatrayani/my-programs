/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<bits/stdc++.h>
using namespace std;
int N=1000001;

int primes[1000001];
void Gen_seive(){
	for(int i=0;i<N;i++){

		primes[i]=1;
	}
	for(int i=2;i*i<N;i++){
		if(primes[i]==1){
			for(int j=i*i;j<N;j+=i){
				primes[j]=0;
			}
		}
	}
}
vector<int>Gen_primes(int num){
	vector<int>ds;
	for(int i=2;i<=num;i++){
		if(primes[i]==1)ds.push_back(i);
	}
	return ds;

}
int main()
{
	Gen_seive();
	int t;
	cin>>t;
	while(t--){
		int l,r;
		cin>>l>>r;
		vector<int>dj=Gen_primes(sqrt(r)+1);
		vector<int>dummy(r-l+1,1);
		for(auto it:dj){
			int firstmul=0;
			if((l/it)*it<l){
				firstmul=((l/it)+1)*it;
			}
			else{
				firstmul=(l/it)*it;
				}
			for(int j=max(firstmul,it*it);j<=r;j+=it){
				dummy[j-l]=0;
				}
			}
		for(int i=0;i<r-l+1;i++){
			if(dummy[i]==1){
				cout<<l+i<<" ";
				
			}
		}
	}
}
