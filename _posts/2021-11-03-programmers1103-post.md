---
title: "[알고리즘] 최솟값 만들기"
date: 2021-11-03 19:15:28 -0400
categories: 알고리즘 구현 C#
---

### 문제 설명

- 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
- 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다.
- 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

- 예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

    - A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
    - A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
    - A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
    - 즉, 이 경우가 최소가 되므로 29를 return 합니다.

- 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

### 제한사항

- 배열 A, B의 크기 : 1,000 이하의 자연수
- 배열 A, B의 원소의 크기 : 1,000 이하의 자연수

### 입출력 예

```sh
A	B	answer
[1, 4, 2]	[5, 4, 4]	29
[1,2]	[3,4]	10
```

### 접근 방식

- 원래 맨처음에는 백트래킹을 이용해서 최소값을 구하려고 했다. 하지만, 시간초과 발생.
- 그래서 두번째로는 정렬한 배열 x 거꾸로 정렬한 배열 의 합으로 풀었다.

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
            int[] A = new int[] { 1, 2 };
            int[] B = new int[] { 3, 4 };
            int answer = sol.solution(A,B);
            Console.WriteLine();
        }
        bool[] visitedA;
        bool[] visitedB;
        int maxCount;
        int resultSum = int.MaxValue;

        public int solution(int[] A, int[] B)
        {
            visitedA = new bool[A.Length];
            visitedB = new bool[B.Length];
            for (int i = 0; i < A.Length; i++)
            {
                visitedB[i] = false;
                visitedA[i] = false;
            }
            maxCount = A.Length; // A와 B 배열의 길이가 같음
            backtrk(0, 0, ref A, ref B);
            return resultSum;
        }


        public void backtrk(int currentSum, int count, ref int[] A, ref int[] B)
        {
            if (count == maxCount)
            {
                resultSum = Math.Min(resultSum, currentSum);
            }
            else
            {
                for(int i = 0; i < maxCount; i++)
                {
                    if(!visitedA[i])
                    {
                        for(int j = 0; j < maxCount; j++)
                        {
                            if(!visitedB[j])
                            {
                                visitedA[i] = true;
                                visitedB[j] = true;
                                backtrk(currentSum + A[i] * B[j], count + 1, ref A, ref B);
                                visitedA[i] = false;
                                visitedB[j] = false;
                            }
                        }

                    }
                }
            }
        }
    }
}

```



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
            int[] A = new int[] { 1, 4, 2 };
            int[] B = new int[] { 5,4, 4 };
            int answer = sol.solution(A,B);
            Console.WriteLine();
        }


        public int solution(int[] A, int[] B)
        {
            int answer = 0;
            List<int> listA = A.ToList<int>();
            List<int> listB = B.ToList<int>();
            listA.Sort();
            listB.Sort();
            listB.Reverse();

            for(int i =0; i < A.Length; i++)
            {

                answer += listA[i] * listB[i];

            }
            return answer;
        }




    }
}
```