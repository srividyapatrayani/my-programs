/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/



#include<bits/stdc++.h>//printing 1 to n
using namespace std;
void print(int x,int n){
	if(x>n)return;
	cout<<x;
	print(x+1,n);//recursion call
}
int main(){
	int n;
	cin>>n;
	print(1,n);


}

//printing n to 1
if(x<n)return;
cout<<x;
print(x+1,n);
print(n,1)