---
title: "[알고리즘] 가장 먼 노드"
date: 2021-12-18 21:51:28 -0400
categories: 알고리즘 그래프 C# BFS
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/05.png){: .align-center}

### 구현 방식

- 그래프 구조로 변환
- bfs 를 이용해서 0번째 노드와의 거리를 `dist`에 담고, 
- `dist`를 최대값으로 가지는 노드를 튜플로 카운트 한다.


```csharp
class Vertex
{
    public Vertex(int idx)
    {
        this.idx = idx;
    }
    public int idx;
    public int dist = -1;
    public List<Vertex> edges = new List<Vertex>();
}

class Program
{


    static void Main(string[] args)
    {
        Program sol = new Program();
        int answer = sol.solution(6, new int[,] { { 3, 6}, { 4, 3 }, { 3, 2 }, { 1, 3 }, { 1, 2 }, { 2, 4 } , { 5, 2} });

        Console.WriteLine();
    }

    bool[] visited;
    List<Vertex> graph;
    (int maxDist, int Count) result = (int.MinValue, 0);

    public int solution(int n, int[,] edge)
    {

        SetGraph(out graph, n, edge);
        visited = new bool[graph.Count];
        bfs(0);
        return result.Count;
    }

    public void SetGraph(out List<Vertex> graph, int n, int[,] edge)
    {
        graph = new List<Vertex>();
        for(int i = 0; i < n; i++)
        {
            graph.Add(new Vertex(i));
        }

        for(int i = 0; i < edge.GetLength(0); i++)
        {
            graph[edge[i, 0] - 1].edges.Add(graph[edge[i, 1] - 1]);
            graph[edge[i, 1] - 1].edges.Add(graph[edge[i, 0] - 1]);
        }
    }

    public void bfs(int now)
    {
        visited[now] = true;
        Queue<int> queue = new Queue<int>();
        graph[now].dist = 0;
        queue.Enqueue(now);
        while(queue.Count != 0)
        {
            int currIdx = queue.Dequeue();
            foreach(Vertex next in graph[currIdx].edges)
            {
                if(!visited[next.idx])
                {
                    next.dist = graph[currIdx].dist + 1;
                    queue.Enqueue(next.idx);
                    visited[next.idx] = true;
                    if (result.maxDist < next.dist)
                        result = (next.dist, 1);
                    else if (result.maxDist == next.dist)
                        result.Count++;
                }
            }
        }

    }


}
```