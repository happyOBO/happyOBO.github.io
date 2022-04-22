---
title: "[알고리즘] 플로이드 와샬 알고리즘"
date: 2022-01-14 10:19:28 -0400
categories: 알고리즘 플로이드와샬 C++
classes: wide
---

### 플로이드 와샬 알고리즘

- 모든 정점에서 모든 정점으로 가는 최단 거리를 구하는 알고리즘
- 지금까지 했던 다익스트라, BFS 알고리즘은 한 정점에서 다른 정점으로 가는 최단 거리를 구하는 알고리즘이었다.
- `i` -> `j` 까지 현재까지 탐색한 것중 최단거리를 담고 있는 2차원 배열`dist` 이 있다고 할때
- `dist[i][j]` 는 먼저 인접한 노드의 가중치로 초기화 해주고
- `k`를 탐색할 때, `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`  로 바꿔준다.
- 이렇게 하면 `i` -> `1 ... k` 까지 중에서 `i` ~ `j` 거리를 최소로 하는 노드 경로 -> `j` 가 된다
- 만약에 예시로 `dist[3][8]`을 탐색 중일 때, `1` 부터 경유지에 적합한지 판단한다고 하자.
    1. `dist[3][8] = min(dist[3][8], dist[3][1] + dist[1][8])`
    2. `dist[3][8] = min(dist[3][8], dist[3][2] + dist[2][8])`
        - 이때 이것은 `3 -> 1 -> 8` , `3 -> 1 -> 2 -> 8` , `3 -> 2 -> 8` , `3 -> 2 -> 1 -> 8` 에서 탐색을 마쳐서 최소 거리 값을 가지고 있는 것중에 하나일 것이다. 
        - `3 -> 1 -> 8` 이 최소 였으면 1 번 과정에서 거친 값이 그대로 적용이 되고 있는 것일거고
        - `3 -> 2 -> 1 -> 8` 이 최소 였다는 건 `dist[3][2]` 를 구했을 당시에 `dist[3][2] = dist[3][1] + dist[1][2]`로 구해졌을 것이다.
    3. 이와 같은 식으로 순서가 복작거리는 순열 상황 또한 다 탐색이 가능하다.

### 기본 예제

- N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 때 모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값을 구하는 프로그램을 작성하세요.


### 입력 설명

- 첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고, M줄에 걸쳐 도로정보와 비용(20 이하의 자연수)이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이면 `1 2 13`으로 주어진다. 

```
5 8
1 2 6
1 3 3
3 2 2
2 4 1
2 5 13
3 4 5
4 2 3
4 5 7

```

### 출력 설명

- 모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력한다. 자기자신으로 가는 비용은 0입니다. i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 `M`으로 출력합니다.

```
0 5 3 6 13 
M 0 M 1 8 
M 2 0 3 10
M 3 M 0 7
M M M M 0
```

```cpp

#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <limits.h>


using namespace std;

void solution(int N, vector<vector<int>>& graph);
void FloydWarshall(int N, vector<vector<int>>& graph);

int main()
{
    int N, M;
    cin >> N >> M;
    vector<vector<int>> graph = vector<vector<int>>(N + 1, vector<int>(N + 1, INT_MAX));

    for (int i = 0; i < M; i++)
    {
        int from , to , w;
        cin >> from >> to >> w;
        graph[from][to] = w;
    }
    for(int i = 1; i <= N; i++)
        graph[i][i] = 0;

    solution(N, graph);
}

void solution(int N, vector<vector<int>>& graph)
{
    FloydWarshall(N, graph);
    for (int from = 1; from <= N; from++)
    {
        for (int to = 1; to <= N; to++)
        {
            if (graph[from][to] == INT_MAX)
                cout << "M ";
            else
                cout << graph[from][to] << " ";
        }
        cout << endl;
    }

}


void FloydWarshall(int N, vector<vector<int>>& graph)
{
    for (int stopover = 1; stopover <= N; stopover++)
        for(int from = 1; from <= N; from++)
            for(int to = 1; to <= N; to++)
            {
                if (stopover == from || stopover == to)
                    continue;
                if (graph[from][stopover] == INT_MAX || graph[stopover][to] == INT_MAX)
                    continue;
                graph[from][to] = min(graph[from][to], graph[from][stopover] + graph[stopover][to]);
            }
}
```

