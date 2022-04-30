#include<bits/stdc++.h>
using namespace std;
struct node{
	int data;
	struct node*link;

};
int main(){
	node *head=new node();
	head->data=1;
	head->link=NULL;
	node *current=new node();
	current->data=2;
	current->link=NULL;
	current->link=NULL;
	head->link=current;
	node *temp=head;
	while(temp){
		cout<<temp->data<<" ";
		temp=temp->link;
	}

}

