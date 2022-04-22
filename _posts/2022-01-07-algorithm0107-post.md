---
title: "[알고리즘] LRU 알고리즘"
date: 2022-01-07 11:22:28 -0400
categories: 알고리즘 정렬 C++
classes: wide
---

## LRU (Least Recently Used)

- 캐시 알고리즘에서 사용된다.
- 캐시에서 작업을 제거할 때 가장 오랫동안 사용하지 않은 것을 제거하겠다
    1. `Cache Miss` : 해야할 작업이 캐시에 없는 상태로 Cache miss가 되고 모든 작업이 뒤로 밀리고 해야할 작업은 캐시의 맨 앞에위치한다. 맨 뒤에 있던건 삭제
    2.  `Cache Hit` : 해야할 작업이 캐시에 있는 상태로 Cache Hit가 되고, 해야할 작업은 캐시의 맨 앞의 위치 되고 해야할 작업의 앞에 있던 작업들은 뒤로 밀리게 된다.
- 여기에서는 삽입 정렬을 사용하게 된다.
    - 현재 탐색하고 있는 숫자에서 지금까지 탐색해놓아서 정렬된 리스트와 비교해서 작으면 한개씩 앞당기고, 커지는 순간 현재 탐색하고 있는 인덱스의 이전 인덱스에 위치시킨다.


### 삽입정렬 알고리즘

```cpp
#include <string>
#include <vector>
#include <iostream>
using namespace std;

void solution(int size, vector<int> inputs) {

    for (int i = 1; i < size; i++)
    {
        int j;
        int tmp = inputs[i];
        for (j = i -1; j >= 0; j--)
        {
            if (inputs[j] > tmp)
            {
                inputs[j + 1] = inputs[j];
            }
            else
                break;
        }
        inputs[j + 1] = tmp;
    }

}

```


### 캐시 알고리즘

- 입력받은 작업들이 담겨있는 배열을 다 처리하고 난 후의 캐시 상태 출력

```cpp

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
using namespace std;


void solution(int S, int N, vector<int> inputs);


int main()
{
    int S, N;
    cin >> S >> N;
    vector<int> inputs = vector<int>(N);
    for (int i = 0; i < N; i++)
    {
        cin >> inputs[i];
    }

    solution(S, N, inputs);

}

void solution(int S, int N, vector<int> inputs) {

    vector<int> cache = vector<int>(S, 0);
    for (int i = 0; i < N; i++)
    {
        int pos = -1;
        for (int j = 0; j < S; j++)
        {
            if (cache[j] == inputs[i])
            {
                pos = j;
            }
        }
        // miss
        if (pos == -1)
        {
            for (int j = S-1; j > 0; j--)
            {
                cache[j] = cache[j - 1];
            }
            cache[0] = inputs[i];
        }
        // hit
        else
        {
            for (int j = pos; j > 0; j--)
            {
                cache[j] = cache[j - 1];
            }
            cache[0] = inputs[i];
        }
    }

    for (int i = 0; i < S; i++)
        cout << cache[i] << " ";

}

```