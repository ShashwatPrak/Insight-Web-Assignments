#include<iostream>
#include <cstdlib>
using namespace std;


void merge(int *A, int *B1, int *B2, int n1, int n2)
{
    int cB1, cB2, cA; cB1 = cB2 = cA = 0;
    while (cB1 < n1 && cB2 < n2)
    {
        if (B1[cB1] < B2[cB2])
            A[cA++] = B1[cB1++];
        else if (B1[cB1] > B2[cB2])
            A[cA++] = B2[cB2++];
        else
        {
            A[cA++] = B1[cB1++];
            A[cA++] = B2[cB2++];
        }
    }
    while(cB1 < n1) A[cA++] = B1[cB1++];
    while(cB2 < n2) A[cA++] = B2[cB2++];
}



void mergesort (int *A, int n)
{
    if (n > 1)
    {
        int B1[n/2], B2[n-n/2];
        for (int i=0;i<n/2;i++)
        {
            B1[i] = A[i];
        }
        for (int i=n/2;i<n;i++)
        {
            B2[i-n/2] = A[i];
        }
        mergesort(B1,n/2); mergesort (B2,n-n/2);
		merge(A,B1,B2,n/2,n-n/2);
    }
}

int sign_change(int* A, int n)
{
    int m = -1;
    for(int i = 0 ; i < n-1 ;i++)
    {
        if(A[i]*A[i+1]<=0)
        {
            m = i ;
            break;
        }
    }
    return m ;
}

int main()
{
    int n;
    cout <<"Enter the number of terms : " ;
    cin >> n;
    int* A = new int(n);
    cout <<"Enter the elements : " ;
    for(int i = 0; i < n; i++)
    {
        cin>>A[i];
    }
    mergesort(A,n);
    int flag = sign_change(A,n);
    if(flag == -1)
    {
        if(A[0]>=0)
        {
            cout<<A[0]<<" , "<<A[1];
        }
        else
        {
            cout<<A[n-2]<<" , "<<A[n-1];
        }
        return 0;
    }
    int k = flag+1;
    int j = flag;
    int sum = A[flag]+A[k];
    int diff = abs( abs(A[flag])-abs(A[k]) );
    j-- ; k++;
    while(k<n && j>=0)
    {
        if(A[j]+A[k]==sum)
        {
            if(abs(abs(A[j])-abs(A[k]))< diff )
            flag = j ;
            k++;
            j--;
        }
        else{
            break;
        }
    }
    cout <<A[flag]<< " , "<<A[flag+1] ;
}
