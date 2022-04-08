---
title: "[알고리즘] 네트워크"
date: 2021-12-20 20:51:28 -0400
categories: 알고리즘 그래프 C# BFS Linq
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/06.png){: .align-center}

### 구현 방식

- 그래프 구조로 변환
- BFS 로 탐색후 방문 한 노드 개수가 증가하면, 카운트 1 증가

```csharp
using System;
using System.Collections.Generic;
using System.Linq;


class Vertex
{
    public Vertex(int idx)
    {
        this.idx = idx;
    }
    public int idx;
    public List<Vertex> edges = new List<Vertex>();
}

class Program
{


    static void Main(string[] args)
    {
        Program sol = new Program();
        int answer = sol.solution(3, new int[,] { { 1, 1, 0}, { 1,1,0}, { 0,0,1}});

        Console.WriteLine();
    }

    bool[] visited;
    List<Vertex> graph;
    (int maxDist, int Count) result = (int.MinValue, 0);

    public int solution(int n, int[,] computers)
    {
        SetGraph(out graph, n, computers);
        int currIdx = 0;
        int answer = 0;
        visited = new bool[n];
        int count = visited.Count(x => x);

        while (count < n)
        {
            bfs(currIdx);
            int bfsCount = visited.Count(x => x);
            if (count < bfsCount)
            {
                count = bfsCount;
                answer++;
            }
            currIdx++;

        }
        return answer;
    }

    public void SetGraph(out List<Vertex> graph, int n, int[,] computers)
    {
        graph = new List<Vertex>();
        for(int i = 0; i < n; i++)
        {
            graph.Add(new Vertex(i));
        }

        for(int i = 0; i < computers.GetLength(0); i++)
        {
            for(int j = i + 1; j < computers.GetLength(1); j++)
            {
                if(computers[i,j] == 1)
                {
                    graph[i].edges.Add(graph[j]);
                    graph[j].edges.Add(graph[i]);

                }
            }
        }
    }

    public void bfs(int now)
    {
        visited[now] = true;
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(now);
        while(queue.Count != 0)
        {
            int currIdx = queue.Dequeue();
            foreach(Vertex next in graph[currIdx].edges)
            {
                if(!visited[next.idx])
                {
                    queue.Enqueue(next.idx);
                    visited[next.idx] = true;

                }
            }
        }

    }



}

```