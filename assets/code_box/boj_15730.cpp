#include <iostream>

using namespace std;

int arr[110][110] = {0,};

int* sub_elem (int N, int M, int add)
{
    int rel_arr[110][110] = {0,};
    for(int i = 0 ; i<N;i++)
    {
        for(int j = 0; j <M; j++)
        {
            rel_arr[i][j] = arr[i][j] + add;
        }
    }
    return *rel_arr;
}

int main(void)
{
    int N, M;
    cin>>N>>M;
    int min = 0;
    int max = 0;
    for(int i =0; i<N;i++)
    {
        for(int j=0; j<M;j++)
        {
            cin>>arr[i][j];
            if(arr[i][j] < min) min = arr[i][j];
            if(max < arr[i][j]) max = arr[i][j];
        }
    }

    for(int i = min; i < max+1; i++)
    {
        int* rel_arr = sub_elem(N,M,i);
        for(int j=1 ; j < N-1; j++)
        {
            for(int k=1; k < M-1; k++)
            {
                if(rel_arr[j][k] == 0)
                {
                    cout<<rel_arr[j][k]<<" ";
                }
            }
            cout<<endl;
        }
    }


}