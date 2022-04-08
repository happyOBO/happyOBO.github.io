---
title: "[알고리즘] 정수삼각형 (bk_1932)"
date: 2020-08-06 13:41:28 -0400
categories: 동적계획법
---

### 문제
```
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
```

위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

### 예제 입출력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

```bash
# input
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
# output
30
```

### 생각한 알고리즘
- d[i][0] = 1 ~ i-1 번째의 최대 값에서 i번째에서 왼쪽으로 간 값
- d[i][1] = 1 ~ i-1 번째의 최대 값에서 i번째에서 오른쪽으로 간 값
- d[i][1] = max(d[i-1][0],d[i-1][1]) + i번째에서 오른쪽으로 간 값

- ```cost[n][i] = max(cost[n-1][i],cost[n-1][i+1]) + triangle[n][i];```
- **주의할 점** :``` max``` 가 필요없는 단일 부분 존재

```bash
# input
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5

# output -> 30
         7
      10   15
    18   16  15
  20  25   20  19
24  30  27   26  24
```
## 코드 (재귀 ,top-down)

```cpp
#include <iostream>
#include <vector>
#include <utility> 
#include <algorithm>

using namespace std;

int triangle[600][600] = {0,};
int N;
long int cost[600][600] = {0,};

void tri(int n)
{
    for(int i = 0; i<= n;i++)
    {
        if(n == i)
        {
            cost[n][i] = cost[n-1][i-1] + triangle[n][i];
        }
        else if(i == 0)
        {
            cost[n][i] = cost[n-1][i] + triangle[n][i];
        }
        else
        {
            cost[n][i] = max(cost[n-1][i-1],cost[n-1][i]) + triangle[n][i];
        }
    }
    if(n<N) tri(n+1);
}

int main(void)
{
    cin>>N;
    for(int i = 0;i<N;i++)
    {
        for(int j = 0; j<=i;j++)
        {
            cin>>triangle[i][j];
        }
    }
    cost[0][0] = triangle[0][0];
    tri(1);
    int max = 0;
    for(int i = 0; i<N;i++)
    {
        if(max < cost[N-1][i]) max = cost[N-1][i];
        
    }
    cout<<max;

}
```

## 코드 (반복문, bottom-up)
```cpp
#include <iostream>
#include <vector>
#include <utility> 
#include <algorithm>

using namespace std;

int main(void)
{
    int triangle[600][600] = {0,};
    int N;
    long int cost[600][600] = {0,};
    cin>>N;
    for(int i = 0;i<N;i++)
    {
        for(int j = 0; j<=i;j++)
        {
            cin>>triangle[i][j];
        }
    }
    cost[0][0] = triangle[0][0];
    for(int j=0; j<N;j++)
    {
        for(int i = 0; i<= j;i++)
        {
            if(j == i)
            {
                cost[j][i] = cost[j-1][i-1] + triangle[j][i];
            }
            else if(i == 0)
            {
                cost[j][i] = cost[j-1][i] + triangle[j][i];
            }
            else
            {
                cost[j][i] = max(cost[j-1][i-1],cost[j-1][i]) + triangle[j][i];
            }
        }
    }


    int max = 0;
    for(int i = 0; i<N;i++)
    {
        if(max < cost[N-1][i]) max = cost[N-1][i];
        
    }
    cout<<max;

}
```