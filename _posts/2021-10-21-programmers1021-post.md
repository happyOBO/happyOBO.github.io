---
title: "[알고리즘] N과 M"
date: 2021-10-21 13:15:28 -0400
categories: 알고리즘 백트랙킹 C#
---


### N과 M

- 예전에 파이썬으로 풀었는데, 왜 C# 으로 푸니까 시간초과가 났음
- 원인은 `Console.Write` 가 시간을 많이 잡아 먹었기 때문이다.
- `StringBuilder` 클래스로 정답 출력 부분을 수정하니 통과가 되었음



### 백트래킹

- DFS 과 조건문을 이용한 빠르게 끊고 넘어가는 방식
- 조합 관련 알고리즘에 많이 쓰인다.
- 큰 틀은 아래와 같다.


```csharp
static void backtrk(int cnt)
{
    if(cnt == M)
    {
        // 원하는 결과 만들기
        return;
    }

    for(int i = cnt; i < N; i++)
    {
        if(!visited[i])
        {
            // 방문한다.(예시 0번째 idx 방문)
            visited[i] = true;
            // 0 번째 idx 를 방문했으니 이제 cnt +1 하고 다른거 방문해보러 출발!
            backtrk(cnt + 1);
            // 방문을 하지 않고, 다른걸 방문한다.
            visited[i] = false;
        }
    }
}
```


### 해결 코드

- 해결 코드는 아래와 같다. 여기서는 **중복을 포함** 해야했기 때문에 `for`문을 계속 적으로 `0`번째에서 부터 쭉 돌린다.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace pgm_dev
{
    class Program
    {
        static bool[] visited;
        static int[] result;
        static int M, N;
        static StringBuilder stringBuilder = new StringBuilder();

        static void backtrk(int cnt)
        {
            if(cnt == M)
            {
                for (int i = 0; i < M; i++)
                {
                    stringBuilder.Append(result[i] + 1 + " ");

                }
                stringBuilder.Append("\n");

                return;
            }

            for(int i = 0; i < N; i++)
            {
                if(!visited[i])
                {
                    visited[i] = true;
                    result[cnt] = i;
                    backtrk(cnt + 1);
                    visited[i] = false;
                }
            }
        }

        // 이부분은 쓰지 않았다.
        static void print()
        {
            for(int i = 0; i< M; i++)
            {
                
                Action print_line = () =>
                {
                    if (M -1 == i) Console.WriteLine(result[i] +  1); else Console.Write($"{result[i] + 1} ");
                };
                print_line();
                
            }
        }


        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split();

            N = int.Parse(input[0]);
            M = int.Parse(input[1]);

            visited = new bool[N];
            result = new int[M];
            for(int i = 0; i < N; i++)
            {
                visited[i] = false;
            }

            backtrk(0);
            Console.Write(stringBuilder.ToString());

        }



    }
}
```