---
title: "[알고리즘] 결정 알고리즘"
date: 2022-01-08 17:22:28 -0400
categories: 알고리즘 이분탐색 C++
---

## 결정알고리즘

- 답인지 아닌지, 참인지 거짓인지로 결정될 수 있는문제, 빠른 연산을 위해 이분탐색을 주로 사용한다. 
- 키워드로는 보통 최솟값, 최댓값을 구하라고한다.

## 예시 문제 (뮤직 비디오)

- 지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다. DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지 되어야 한다. 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다. 즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야
한다.
- 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기로 하였다. 이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.

### 입력설명

- 첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다. 다음 줄에는 조영필이 라이브에서 부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다. 부른 곡의 길이는 10,000분을 넘지 않는다고 가정하자.

```
9 3
1 2 3 4 5 6 7 8 9
```

### 출력설명

- 첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.

```
17
```

### 구현 방식

- 위의 같은 예시로 생각하면, 총 용량이 45 이다. 3개의 DVD로 한다면 안전빵으로 간다면 최대 용량을 45로 해서 [45, 0, 0 ] 이 가능할 것이고, 하나의 DVD 용량은 45 / 3 = 15 보다는 작지는 못할 것이다.
- 그러면 이분탐색을 이용해서 15 ~ 45 까지 하나씩 늘려가면서 해당 용량에서 가능한지 아닌지를 판별하면 될것이다.
- 만약에 가능하다면..! right 값을 mid 값으로 바꾸고, 불가능하다면 left 값을 mid 로 바꾸면서 더이상 쪼개지지 않는 구간이 생길 것이다.

```cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;


void solution(int N, int M, vector<int> inputs);
bool canPutIn(int size, int bucketNumber, vector<int>& inputs);

void solution(int N, int M, vector<int> inputs){
    // numeric 에 있는 메소드로 해당 범위까지의 합을 구한다.
    int inputsSum = std::accumulate(inputs.begin(), inputs.end(), 0);
    int minSize = inputsSum / M; // left
    int maxSize = inputsSum; // right
    int midSize = (minSize + maxSize) / 2;

    while (minSize < maxSize)
    {
        if (canPutIn(midSize, M, inputs))
        {
            maxSize = midSize;
            midSize = (minSize + maxSize) / 2;
        }
        else
        {
            minSize = midSize + 1;
            midSize = (minSize + maxSize) / 2;
        }
    }

    cout << midSize;
}


bool canPutIn(int size, int bucketNumber , vector<int>& inputs)
{
    int bucket = size;
    bucketNumber--;
    for (vector<int>::iterator it = inputs.begin(); it != inputs.end() ; it++)
    {
        if (size < (*it))
            return false;
        if (bucket - (*it) < 0)
        {
            if (bucketNumber > 0)
            {
                bucketNumber--;
                bucket = size;
            }
            else
                return false;
        }
        bucket -= (*it);
        
    }

    return true;
}

```

