/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<bits/stdc++.h>
using namespace std;
int main ()
{
  int n;
  cin >> n;
  vector < int >ds;
  for (int i = 0; i < n; i++)
    {
      int x;
      cin >> x;
      ds.push_back (x);

    }

  for (int i = 0; i < ds.size (); i++)
    {
      cout << ds[i] << " ";
    }

}
