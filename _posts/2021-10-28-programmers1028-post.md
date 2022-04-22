---
title: "[알고리즘] 피보나치 수"
date: 2021-10-28 14:15:28 -0400
categories: 알고리즘 동적계획법 C#
classes: wide
---



### 문제 설명

- 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

- 예를들어

```sh
F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
```
- 와 같이 이어집니다.

- 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

### 제한 사항

- n은 2 이상 100,000 이하인 자연수입니다.

### 입출력 예

```sh
n	return
3	2
5	5
```



### 접근 방식

- 예전에 다이나믹 프로그래밍 및 재귀 방식으로 백준 문제를 동일하게 풀었는데, 이번에는 프로그래머스에서 반복문 형태로 풀어보았다.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace Programmers
{
    class Program
    {

        static void Main(string[] args)
        {
            Program sol = new Program();
            int answer = sol.solution(3);
            Console.WriteLine();
        }

        int[] fibbo;
        public int solution(int n)
        {
            fibbo = new int[n + 1];
            fibbo[0] = 0;
            fibbo[1] = 1;

            for(int i = 0; i < n+1;i++)
            {
                if (i <= 1)
                    fibbo[i] = i;
                else
                    fibbo[i] = (fibbo[i - 1] + fibbo[i - 2]) % 1234567;
            }

            return fibbo[n];
        }


    }
}

```