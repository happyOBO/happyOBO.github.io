---
title: "[알고리즘] RGB (bk_1149)"
date: 2020-08-06 13:41:28 -0400
categories: 동적계획법
---


### 문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
- 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.


### 예제 입출력

```bash
# input
3
26 40 83
49 60 57
13 89 99

# output

96
```


### 생각한 알고리즘
- dp[i][0] : 1 ~ i-1 까지 최소 비용으로 집을 칠하고 i를 빨강색으로 칠했을 때의 비용
- dp[i][1] : 1 ~ i-1 까지 최소 비용으로 집을 칠하고 i를 그린색으로 칠했을 때의 비용
- dp[i][2] : 1 ~ i-1 까지 최소 비용으로 집을 칠하고 i를 파랑색으로 칠했을 때의 비용
- dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + i 집을 빨강으로 칠한 비용

```bash
# 2
# 1 2 3
# 3 1 2

dp[0][0] = 1
dp[0][1] = 2
dp[0][2] = 3

dp[1][0] = min(dp[0][1],dp[0][2]) + 3 # 2 + 3
dp[1][1] = min(dp[0][0],dp[0][2]) + 1 # 1 + 1
dp[1][2] = min(dp[0][0],dp[0][1]) + 2 # 1 + 2

# 따라서 최소 비용은 2 이다.

```

### 코드 (재귀 top-down 사용)
```cpp

#include <iostream>
#include <vector>
#include <utility> // pair

using namespace std;

int arr[1200][5] ={0, };
long int cost[1200][5] ={0, };
int N;


void rgb(int n)
{
    cost[n][0] = min(cost[n-1][1],cost[n-1][2]) + arr[n][0];
    cost[n][1] = min(cost[n-1][0],cost[n-1][2]) + arr[n][1];
    cost[n][2] = min(cost[n-1][0],cost[n-1][1]) + arr[n][2];
    if(n < N-1)
    {
        rgb(n+1);
    }
}


int main(void)
{
    
    cin>>N;
    for(int i = 0; i< N; i++)
    {
        cin>>arr[i][0]>>arr[i][1]>>arr[i][2];
    }
    cost[0][0] = arr[0][0];
    cost[0][1] = arr[0][1];
    cost[0][2] = arr[0][2];
    rgb(1);
    long int mid_min = min(cost[N-1][0],cost[N-1][1]);
    cout<<min(mid_min, cost[N-1][2]);

}
```


### 코드 (for문 buttom-up 사용)

```cpp

#include <iostream>
#include <vector>
#include <utility> // pair

using namespace std;

int main(void)
{
    int arr[1200][5] ={0, };
    long int cost[1200][5] ={0, };
    int N;
    cin>>N;
    for(int i = 0; i< N; i++)
    {
        cin>>arr[i][0]>>arr[i][1]>>arr[i][2];
    }
    cost[0][0] = arr[0][0];
    cost[0][1] = arr[0][1];
    cost[0][2] = arr[0][2];
    for(int i = 1;i<N;i++)
    {
        cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + arr[i][0];
        cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + arr[i][1];
        cost[i][2] = min(cost[i-1][0],cost[i-1][1]) + arr[i][2];
    }

    long int mid_min = min(cost[N-1][0],cost[N-1][1]);
    cout<<min(mid_min, cost[N-1][2]);

}

```