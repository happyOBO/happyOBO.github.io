---
title: "[알고리즘] 가장 어떤 부분 수열 (bk_17216...)"
date: 2020-08-13 08:00:28 -0400
categories: 알고리즘 C++ 동적계획법 백트랙킹
---

### 문제

수열 A가 주어졌을 때, 그 수열의 감소 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {1, 100, 2, 50, 60, 8, 7, 3, 6, 5} 인 경우에 합이 가장 큰 감소 부분 수열은 A' = {100, 60, 8, 7, 6, 5} 이고, 합은 186이다.

### 입력
첫째 줄에 수열 A의 크기 N(1 ≤ N ≤ 1000)이 주어진다.둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다.(1 ≤ Ai ≤ 1,000)

### 출력
첫째 줄에 수열 A의 합이 가장 큰 감소 부분 수열의 합을 출력한다.

### 예제 입력 1 

```
10
1 100 2 50 60 8 7 3 6 5
```

### 예제 출력 1 

```
186
```

### 생각한 알고리즘

- 백트랙킹을 이용하여 다확인해보자!
- 현재 ``flag`` 지점을 탐색중이며 ``flag+1`` 부터 ``N-1``번째 배열 중 쌓고있는 부분수열의 가장 마지막 부분보다 작으면 넣고 함수 호출!
- **문제점** : 너무 느리다. 중복적인 부분이 많다.

```cpp
// 백트래킹
#include <iostream>
#include <vector>
using namespace std;

long int mx = 0;
int N;
int arr[1100] ={0,};
void back(int flag, vector<int> order)
{

    if(flag >= N)
    {
        long int sum = 0;
        for(int i = 0; i<order.size();i++)
        {
            sum += order[i];
        }
        if(mx < sum) mx = sum;
    }
   for(int i = flag; i<N;i++)
   {
       if(order.size() == 0)
        {
            order.push_back(arr[i]);
            back(i+1,order);
            order.pop_back();
        }
       else if(order.back() > arr[i])
       {
           order.push_back(arr[i]);
           back(i+1,order);
           order.pop_back();
       }
   }
}

int main(void)
{
    cin>>N;
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }
    vector<int> v;
    back(0,v);
    cout<<mx;

}
```

### 생각한 알고리즘 -2

- 동적 계획법을 사용하자
- ``d[i] = max(d[i], arr[i] + d[0~i-1])``
- Top-down ver

```cpp

#include <iostream>
#include <vector>

using namespace std;

long int mx = 0;
int N;
int arr[1100] ={0,};
int d[1100] ={0, };

// d[n] = max(d[n], A[n]+d[j(0부터 n까지)])


void dp(int n)
{
    for(int i=0;i<n;i++)
    {
        if(arr[i] > arr[n])
        {
            d[n] = max(d[n], arr[n] + d[i]);
            // cout<<d[n]<<endl;   
        }
        

    }
    if(n < N)
    {
        if(mx < d[n]) mx = d[n];
        dp(n+1);
    }
    
}

int main(void)
{
    cin>>N;
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
        d[i] = arr[i];
    }
    dp(0);
    cout<<mx;
}
```
### 생각한 알고리즘 -3

```cpp
#include <iostream>
#include <vector>

using namespace std;


int main(void)
{

    int N;
    int arr[1100] ={0,};
    int d[1100] ={0, };
    int mx = 0;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
        d[i] = arr[i];
    }
    for(int j = 0; j<=N;j++)
    {
        for(int i=0;i<j;i++)
        {
            if(arr[i] > arr[j])
            {
                d[j] = max(d[j], arr[j] + d[i]);
                // cout<<d[n]<<endl;   
            }

        }
        if(d[j] > mx) mx = d[j];
    }
    cout<<mx;
}
```