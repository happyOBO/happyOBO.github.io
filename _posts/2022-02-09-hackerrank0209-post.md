---
title: "[알고리즘] KnightL on a Chessboard"
date: 2022-02-09 22:30:28 -0400
categories: 알고리즘 BFS C++
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/48.png){: .align-center}

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/49.png){: .align-center}

### 문제 요지

- `KnightL(i,j)` 는 한번의 이동을 다음과 같이 계산했을 때 를 의미한다.
    - horizontal 방향으로 `+i` or `-i`, vertical 방향으로 `+j` or `-j` 로 이동
    - horizontal 방향으로 `+j` or `-j`, vertical 방향으로 `+i` or `-i` 로 이동
- (0,0) 시작점에서 `KnightL(i,j)` 로 움직여서 (n-1,n-1) 까지 도착할 수 있는 최단거리를 구해서 출력
- ~~문제 보다는 해석이 어렵다,,,~~

### 구현 방식

- `i`,`j` 에 따른 알맞은 방향 벡터 추가
- bfs 로 최단거리 탐색


### 코드

- 최종 코드는 아래와 같다.

```cpp
struct Position
{
    Position(int posy, int posx) : y(posy), x(posx) { }
    int y;
    int x;
};

vector<vector<int>> knightlOnAChessboard(int n) 
{

    vector<vector<int>> result = vector<vector<int>>(n - 1, vector<int>(n -1));
    for (int y = 1; y < n; y++)
    {
        for (int x = 1; x < n; x++)
        {
            vector<Position> directions = { Position(y,x),
                                             Position(x,y),
                                             Position(-y,-x),
                                             Position(-x,-y),
                                             Position(-y,x),
                                             Position( x,-y),
                                             Position(y,-x),
                                             Position(-x,y) };
            result[y - 1][x - 1] = bfs(n, directions);

        }
    }

    return result;
}

int bfs(int n, vector<Position>& directions)
{
    bool visited[25][25] = {};
    vector<vector<int>> graph = vector<vector<int>>(n, vector<int>(n,-1));
    queue<Position> q;
    q.push(Position(0, 0));
    visited[0][0] = true;
    graph[0][0] = 0;

    while (!q.empty())
    {
        Position currPos = q.front();
        q.pop();
        for (Position& dir : directions)
        {
            Position nextPos = { currPos.y + dir.y , currPos.x + dir.x };

            if (nextPos.y == n - 1 && nextPos.x == n - 1)
                return graph[currPos.y][currPos.x] + 1;

            if (canGo(n, nextPos) && !visited[nextPos.y][nextPos.x])
            {
                graph[nextPos.y][nextPos.x] = graph[currPos.y][currPos.x] + 1;
                visited[nextPos.y][nextPos.x] = true;
                q.push(nextPos);

            }
        }

    }

    return graph[n - 1][n - 1];
}

bool canGo(int n, Position nextPos)
{
    if (nextPos.x < 0 || n <= nextPos.x)
        return false;
    if (nextPos.y < 0 || n <= nextPos.y)
        return false;
    return true;

}
```