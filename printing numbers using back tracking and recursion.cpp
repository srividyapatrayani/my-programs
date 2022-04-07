/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/



#include<bits/stdc++.h>//printing 1 to n
using namespace std;
void print(int x){
	if(x==0)return;
	cout<<x;
	print(x-1);//recursion call
}
int main(){
	int x;
	cin>>x;
	print(x);


}