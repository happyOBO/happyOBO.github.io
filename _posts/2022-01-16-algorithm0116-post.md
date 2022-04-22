---
title: "[알고리즘] 벨만-포드 알고리즘"
date: 2022-01-16 14:30:28 -0400
categories: 알고리즘 벨만포드 C++
classes: wide
---


### 벨만-포드 알고리즘

- i 개 이하의 간선을 거쳤을 때 나오는 최단거리를 간선이 0개에서 V - 1 개까지 일때까지로 구한다.
- i 개 이하의 간선을 거쳤을 때 목적지 to 로 가는 최단거리는 아래 중 최소값을 나타낸다.
    - i - 1 개 이하의 거쳤을 때 목적지 to 로 가는 최단거리
    - from -> to 로 가는 간선이라면, [i - 1 개 이하의 거쳤을 때 목적지 from 로 가는 최단거리] + [from -> to 로 가는 간선 가중치]
- 만약에 간선이 V - 1 개 보다 많이 거쳤을 때 최소값이 나온다면, 그거는 동일 노드를 여러번 거치면 더 최소값이 나온다는 것이므로, 음의 사이클이 존재한다는 의미


```
dist[to] = min(dist[to], dist[from] + w);
```


### 기본 예제

- N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 때 한 도시에서 다른 도시로 이동하는데 쓰이는 비용의 최소값을 구하는 프로그램을 작성하세요.


### 입력 설명

- 첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고, M줄에 걸쳐 도로정보와 비용이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이면 “1 2 13”으로 주어진다. 그 다음 마지막 줄에 출발도시와 도착도시가 주어진다. 

```
5 7
1 2 5
1 3 4
2 3 -3
2 5 13
3 4 5
4 2 3
4 5 7
1 5

```

### 출력 설명

- 출발도시에서 도착도시까지 가는데 걸리는 최소비용을 출력한다. 음의 사이클이 존재할 경우 -1를 출력한다.

```
14
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
class Edge;
void solution(int V, int startPos, int destPos, vector<Edge> edges);
vector<int> BellmanFord(int V, int startPos, vector<Edge> edges);

class Edge
{
public:
    Edge(int f, int t, int w)
    {
        from = f;
        to = t;
        weight = w;
    }

public:
    int from;
    int to;
    int weight;
};

int main()
{
    int V,E, startPos, destPos;
    cin >> V >> E;
    vector<Edge> edges = vector<Edge>();
    for (int i = 1; i <= E; i++)
    {
        int from, to, w;
        cin >> from >> to >> w;
        edges.push_back(Edge(from, to, w));
    }
    cin >> startPos >> destPos;

    solution( V,  startPos, destPos, edges);
}

void solution(int V, int startPos, int destPos, vector<Edge> edges)
{
    vector<int> dist = BellmanFord(V, startPos, edges);
    // 음의 사이클 존재 여부 확인
    for (auto it = edges.begin(); it != edges.end(); it++)
    {
        int from = (*it).from;
        int to = (*it).to;
        int w = (*it).weight;
        if (dist[to] > dist[from] + w)
        {
            cout << -1 << endl;
            return;
        }
    }

    cout << dist[destPos] << endl;

}

vector<int> BellmanFord(int V, int startPos, vector<Edge> edges)
{
    vector<int> dist = vector<int>(V + 1, INT_MAX);
    dist[startPos] = 0;
    for (int edgeCount = 1; edgeCount < V; edgeCount++)
    {
        for (auto it = edges.begin(); it != edges.end(); it++)
        {
            int from = (*it).from;
            int to = (*it).to;
            int w = (*it).weight;
            dist[to] = min(dist[to], dist[from] + w);
        }
    }

    return dist;
}


```

### 유사문제 (타임 머신)


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/26.png){: .align-center}


### 구현 방식

- 위의 코드는 음의 사이클이 하나라도 있으면 `-1` 을 출력하는 방식이었는데
- 이번에는 **해당 시작 노드에서부터의 경로 중에 음의 사이클이 없어야한다.**
- 예를 들어서 1 번 노드는 간선 이 없고, 2, 3 번 노드가 음의 사이클을 가지는 간선이 있는경우
- 이런 경우에는 한번더 탐색해서 감소하는 구간이 있는지 판별해서 음의 사이클을 체크하는 구간에서
- 1 ~ V -1 개까지 간선 개수를 탐색했을때, 접근되지 못했던 노드의 간선이면 `continue` 로 넘어가준다.


```cpp

#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <limits.h>

using namespace std;
class Edge;
void solution(int V, int startPos, vector<Edge> edges);
vector<long long> BellmanFord(int V, int startPos, vector<Edge> edges);

class Edge
{
public:
    Edge(int f, int t, int w)
    {
        from = f;
        to = t;
        weight = w;
    }

public:
    int from;
    int to;
    int weight;
};

int main()
{
    int V,E, startPos, destPos;
    cin >> V >> E;
    vector<Edge> edges = vector<Edge>();
    for (int i = 1; i <= E; i++)
    {
        int from, to, w;
        cin >> from >> to >> w;
        edges.push_back(Edge(from, to, w));
    }

    solution( V,  1, edges);
}

void solution(int V, int startPos, vector<Edge> edges)
{
    vector<long long> dist = BellmanFord(V, startPos, edges);

    for (auto it = edges.begin(); it != edges.end(); it++)
    {
        int from = (*it).from;
        int to = (*it).to;
        long long w = static_cast<long long>((*it).weight);
        if (dist[to] == LLONG_MAX || dist[from] == LLONG_MAX)
            continue;

        if (dist[to] > dist[from] + w)
        {
            cout << -1 << endl;
            return;
        }
    }

    for (int v = 1; v <= V; v++)
    {
        if (startPos == v)
            continue;
        if (dist[v] == LLONG_MAX)
            cout << -1 << endl;
        else
            cout << dist[v] << endl;

    }

}

vector<long long> BellmanFord(int V, int startPos, vector<Edge> edges)
{
    vector<long long> dist = vector<long long>(V + 1, LLONG_MAX);
    dist[startPos] = 0;
    for (int edgeCount = 1; edgeCount < V; edgeCount++)
    {
        for (auto it = edges.begin(); it != edges.end(); it++)
        {
            int from = (*it).from;
            int to = (*it).to;
            int w = (*it).weight;
            if (dist[from] == LLONG_MAX)
                continue;
            dist[to] = min(dist[to], dist[from] + w);
        }
    }

    return dist;
}

```