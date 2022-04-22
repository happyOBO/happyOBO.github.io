---
title: "[알고리즘] Journey to the Moon"
date: 2022-02-08 14:30:28 -0400
categories: 알고리즘 BFS 시간복잡도 C++
classes: wide
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/40.png){: .align-center}

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/41.png){: .align-center}

### 문제 요지

- `astronaut`의 ID 가 페어로 들어오는데, 같은 페어 내에 있는 `astronaut` 같은 그룹에 속한다.
    - 예로 (1,2) ,( 2, 3) 페어 가 들어오면 {1, 2, 3} 은 같은 그룹에 속한다.
- 이때, `astronaut`을 다른 그룹에서 하나씩 뽑아서 만들 수 있는 페어의 수를 구한다.
- 입력으로 `astronaut` 의 수 `N` (ID 는 `0` ~ `N -1`) , `astronaut` 의 ID 값이 페어로 들어오는 개수 `P` `astronaut` 의 ID 값 페어 가 순차적으로 입력받는다.

### 구현 방식

- 먼저 그래프를 생성한 후에 DFS 를 통해 그룹마다의 사이즈를 기록한 벡터 `groups`를 채워나간다.
    - ex : (0, 1, 2) , (3,4) 로 2 그룹이 존재한다면 `groups` 는 `{3,2}` 이다.
- 개수를 구하기 위해
- `groups` 을 조합으로 2개 택한다음에 해당 두 원소의 곱을 합한 값을 누적 시킨다.
- 위의 결과처럼 하면 코드를 작성하면 아래와 같다.

```cpp
long long combination(int n, vector<int>& groups)
{
    long long result = 0;
    for(int i = 0; i < groups.size(); i++)
    {
        for(int j = i + 1; j < groups.size(); j++)
        {
            result += groups[i] * groups[j];
        }
    }
    return result;
}
```

-  이렇게 되면 $O(N^2)$ 이 되어버려서 `n = 10^5` 이므로 1초를 넘어버리게 되어 시간초과가 발생한다.
-  `현재 탐색중인 그룹의 크기 X 지금까지 탐색 하지 않은 그룹들의 총 크기` 를 합한 값은 동일한 결과를 낼수 있다.
   -  예로,  `groups` 가 `{2, 2, 1, 1, 1}` 이라면 `2 * 5 + 2 * 3 + 1 * 2 + 1 * 1 + 1 * 0 = 19` 이다.

```cpp
long long combination(int n, vector<int>& groups)
{
    long long result = 0;
    for(auto& cnt : groups)
    {
        n -= cnt;
        if(n < 0) break;
        result += static_cast<long long>(n * cnt);
    }
    return result;
}
```

- 이렇게 되면 $O(N)$ 으로 줄일 수 있다..!


### 코드

- 최종 코드는 아래와 같다.

```cpp
#include <bits/stdc++.h>

using namespace std;

void createGraph(vector<vector<int>>& graph, vector<vector<int>>& astronaut);
vector<int> calcGroupsBFS(int n, vector<vector<int>>& graph);
long long combination(int n, vector<int>& groups);

long long journeyToMoon(int n, vector<vector<int>> astronaut) {
    vector<vector<int>> graph = vector<vector<int>>(n);
    createGraph(graph, astronaut);
    auto groups =  calcGroupsBFS(n, graph);
    return combination(n, groups);

}

void createGraph(vector<vector<int>>& graph, vector<vector<int>>& astronaut)
{
    for(auto& ast : astronaut)
    {
        graph[ast[0]].push_back(ast[1]);
        graph[ast[1]].push_back(ast[0]);
    }
}

vector<int> calcGroupsBFS(int n, vector<vector<int>>& graph)
{
    vector<int> groups;
    // bfs
    vector<bool> visited = vector<bool>(n,false);
    queue<int> q;
    for(int start = 0; start < n; start++)
    {
        if(visited[start])
            continue;
        
        q.push(start);
        visited[start] = true;
        int groupSize = 0;
        groupSize++;
        
        while(!q.empty())
        {
            int curr = q.front();
            q.pop();
            for(auto& next : graph[curr])
            {
                if(!visited[next])
                {
                    q.push(next);
                    visited[next] = true;
                    groupSize++;
                }
            }
            
        }
        groups.push_back(groupSize);
        
    }

    return groups;
}

long long combination(int n, vector<int>& groups)
{
    long long result = 0;

    for(auto& cnt : groups)
    {
        n -= cnt;
        if(n < 0) break;
        result += static_cast<long long>(n * cnt);
    }
    
    return result;
}
```