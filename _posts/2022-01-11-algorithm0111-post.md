---
title: "[알고리즘] 송아지 찾기"
date: 2022-01-11 16:19:28 -0400
categories: 알고리즘 BFS C++
classes: wide
---

## 문제 내용

- 현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 현수의 위치와 송아 지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
- 현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성 하세요.


### 입력설명

- 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000 까지이다.


```
5 14
```

### 출력설명

- 점프의 최소횟수를 구한다.

```
3
```

### 구현 방식

- 이전까지 BFS로 이동 가능 노드/위치를 큐에 추가해줬던 것처럼
- 현재 탐색 중인 위치에서 `+1` , `-1` ,`+5` 한 위치를 큐에 추가한 후에 원하는 목적지에 도착할 때까지 탐색한다.


```cpp

void solution(int start, int end) {

    queue<int> q;
    visited = vector<int>(10001, -1);
    vector<int> jumps = vector<int>{ 1, -1, 5 };
    
    q.push(start);
    visited[start] = 0;
    
    while (!q.empty())
    {
        int currIdx = q.front();
        q.pop();

        if (currIdx == end) break;

        for (auto it = jumps.begin(); it != jumps.end(); it++)
        {
            int nextIdx = currIdx + *it;
            if (nextIdx < 0 || 10000 < nextIdx) continue;
            if (visited[nextIdx] < 0)
            {
                q.push(nextIdx);
                visited[nextIdx] = visited[currIdx] + 1;
            }

        }

    }
    cout << visited[end];
}
```


