---
title: "[알고리즘] 마구간 정하기"
date: 2022-01-09 11:19:28 -0400
categories: 알고리즘 이분탐색 C++
classes: wide
---

## 결정알고리즘


- N개의 마구간이 1차원 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가 지며, 마구간간에 좌표가 중복되는 일은 없습니다.
- 현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
- C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

### 입력설명

- 첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다. 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

```
5 3
1 2 8 4 9
```

### 출력설명

- 첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.

```
3
```

### 구현 방식

- 이분 탐색으로 적절한 최소거리의 최대값을 찾아낸다.
- 초기 min 값 : 1
- 초기 max 값 : 정렬시 첫번째와 마지막 값과의 차이
- 정렬해놓은 배열에서 0 번째부터 말을 배치해서(0번째부터 배치해야 최적의 결과가 나옴) 격차가 현재 탐색하고 있는 예상 최소 간격 이상일 때, 그 자리에 다시 말을 배치해서 C개의 말을 모두 배치할 수 있는지 판단

```cpp

void solution(int K, int N, vector<int> inputs){

    sort(inputs.begin(), inputs.end());
    long long maxDistance = *(inputs.end() - 1) - *inputs.begin();
    long long minDistance = 1;
    long long midDistance = (maxDistance + minDistance) / 2;
    while (minDistance <= maxDistance)
    {
        if (canPlaced(midDistance, N, inputs))
            minDistance = midDistance + 1;

        else
            maxDistance = midDistance - 1;
        midDistance = (maxDistance + minDistance) / 2;
    }

    cout << midDistance;
}

bool canPlaced(int dist, int count ,vector<int>& inputs)
{
    int currPos = *inputs.begin();
    count--;
    for (vector<int>::iterator it = inputs.begin(); it != inputs.end(); it++)
    {
        if (count <= 0)
            return true;
        else
        {
            if (*it - currPos >= dist)
            {
                count--;
                currPos = *it;
            }
        }
    }
    if (count <= 0)
        return true;
    else
        return false;
}

```

