---
title: "[알고리즘] 게임 맵 최단 거리"
date: 2021-11-11 22:31:28 -0400
categories: 알고리즘 BFS C#
classes: wide
---



### 문제 설명

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

### 제한사항

- maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
- n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
- maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
- 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.



### 입출력 예

```sh
입출력 예
maps															answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1
```

### 접근 방식

- BFS 를 이용해서, 큐에 쌓아놓고 하나씩 pop 하면서
- 조건에 맞는 (방문하지 않고, 벽이 아닌 경우) 상하좌우 노드 탐색
- 해당 노드 인덱스에 부모노드를 기준 노드로 지정

```csharp

using System;
using System.Collections.Generic;
using System.Linq;

namespace Programmers
{
    public class Pos
    {
        public int X;
        public int Y;
        public Pos(int y, int x)
        {
            X = x;
            Y = y;
        }
    }
    class Program
    {

        static void Main(string[] args)
        {
            Program sol = new Program();
            int[,] maps = new int[,] { { 1, 0, 1, 1, 1 }, { 1, 0, 1, 0, 1 }, { 1, 0, 1, 1, 1 }, { 1, 1, 1, 0, 1 }, { 0, 0, 0, 0, 1 } };
            int answer = sol.solution(maps);
            Console.WriteLine();
        }
        int[,] maps;


        public int solution(int[,] maps)
        {
            this.maps = maps;
            Pos StartPos = new Pos(0, 0);
            Pos dstPos = new Pos(maps.GetLength(0) -1, maps.GetLength(1) -1);
            List<Pos> path = bfs(StartPos, dstPos);

            return path == null ? -1 : path.Count;
        }

        public List<Pos> bfs(Pos StartPos , Pos DestPos)
        {
            int[] deltaY = new int[] { -1, 0, 1, 0 };
            int[] deltaX = new int[] { 0, -1, 0, 1 };
            int MapHeight = maps.GetLength(0);
            int MapWidth = maps.GetLength(1);
            bool[,] visited = new bool[MapHeight, MapWidth];
            Pos[,] parent = new Pos[MapHeight, MapWidth];

            Queue<Pos> q = new Queue<Pos>();
            visited[StartPos.Y, StartPos.X] = true;
            parent[StartPos.Y, StartPos.X] = StartPos;
            q.Enqueue(StartPos);

            while(q.Count > 0)
            {
                Pos pos = q.Dequeue();
                int nowY = pos.Y;
                int nowX = pos.X;
                for(int i = 0; i < 4; i++)
                {
                    int nextX = nowX + deltaX[i];
                    int nextY = nowY + deltaY[i];
                    Console.WriteLine();
                    if (nextY < 0 || MapHeight - 1 < nextY || nextX < 0 || MapWidth - 1 < nextX)
                        continue;
                    if (maps[nextY, nextX] == 0)
                        continue;
                    if (visited[nextY, nextX])
                        continue;
                    Pos nextPos = new Pos(nextY, nextX);

                    visited[nextY, nextX] = true;
                    parent[nextY, nextX] = pos;
                    q.Enqueue(nextPos);
                }


            }

            List<Pos> path = CalcPathFromParent(parent, DestPos);
            return path;
        }

        public List<Pos> CalcPathFromParent(Pos[,] parent, Pos destPos)
        {
            int y = destPos.Y;
            int x = destPos.X;

            List<Pos> path = new List<Pos>();

            while(parent[y, x] != null && !(parent[y,x].Y == y && parent[y,x].X == x))
            {
                path.Add(new Pos(y, x));
                Pos pos = parent[y, x];
                y = pos.Y;
                x = pos.X;
            }
            path.Add(new Pos(y,x));
            if (parent[y, x] == null)
                return null;

            return path;
        }

    }
}

```