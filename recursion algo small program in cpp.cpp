/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/



#include<bits/stdc++.h>
using namespace std;
void print(int num){
	if(num==0)return;
	cout<<"Ashok";
	print(num-1);//recursion call
}
int main(){
	int num;
	cin>>num;
	print(num);


}