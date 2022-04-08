---
title: "[알고리즘] 타겟 넘버"
date: 2021-10-22 11:15:28 -0400
categories: 알고리즘 C# DFS
---

### 문제 설명

- n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```sh
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

- 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

### 입출력 예

```sh
numbers             target  return
[1, 1, 1, 1, 1]     3       5
```


### 접근 방식

- DFS 로 끝까지 탐색한다. +1 하고 넘기고 -1 하고 넘기고~
- 끝까지 간다음의 결과값이 target이랑 같다면,,! 결과 변수에 1을 더한다.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace pgm_dev
{
    class Program
    {

        int result = 0;
        int targetNum;
        int[] numbersList;
        int[] operations = new int[2] { -1, 1 };

        static void Main(string[] args)
        {
            Program sol = new Program();
            int[] numbers = new int[] { 1, 1, 1, 1, 1 };
            int target = 3;
            int answer = sol.solution(numbers, target);
            Console.WriteLine( "");
        }

        public int solution(int[] numbers, int target)
        {
            targetNum = target;
            numbersList = numbers;
            DFS(0, 0);
            return result;
        }

        public void DFS(int tmpResult , int cnt)
        {
            if(cnt == numbersList.Length)
            {
                if (tmpResult == targetNum)
                    result++;
                return;
            }
            foreach(int op in operations)
            {
                DFS(tmpResult + numbersList[cnt] * op, cnt + 1);
            }

            
        }
    }
}

```