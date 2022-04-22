---
title: "[알고리즘] 행렬의 곱셈"
date: 2021-10-28 18:15:28 -0400
categories: 알고리즘 구현 C#
classes: wide
---


### 문제 설명

- 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

### 제한 조건

- 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
- 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
- 곱할 수 있는 배열만 주어집니다.


### 입출력 예

```sh
arr1	                            arr2	                            return
[[1, 4], [3, 2], [4, 1]]	        [[3, 3], [3, 3]]	                [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
```


### 접근 방식

- 행렬 곱셈에서 결과 행렬의 원소는 아래와 같이 계산된다.

```s
resultMatrix[i,j] = SUM(preMatrix[i,k] * postMatrix[k,j]) (k는 0 ~preMatrix/postMatrix의 열.행 개수, )
```


```csharp
using System;

namespace Programmers
{
    class Program
    {

        static void Main(string[] args)
        {
            Program sol = new Program();
            int[,] arr1 = new int[,] { { 2, 3, 2 }, { 4, 2, 4 }, { 3, 1, 4 } };
            int[,] arr2 = new int[,] { { 5, 4, 3 }, { 2, 4, 1 }, { 3, 1, 1 } };
            int[,] answer = sol.solution(arr1, arr2);
            Console.WriteLine();
        }

        public int[,] solution(int[,] arr1, int[,] arr2)
        {
            int[,] answer = new int[arr1.GetLength(0), arr2.GetLength(1)];


            for (int row = 0; row < answer.GetLength(0); row++)
            {
                for (int col = 0; col < answer.GetLength(1); col++)
                {
                    answer[row, col] = 0;
                }
            }

            int matCalcTimes = arr1.GetLength(1);

            for (int row = 0; row < answer.GetLength(0); row++)
            {
                for (int col = 0; col < answer.GetLength(1); col++)
                {
                    // 행렬 원소 계산
                    for (int i = 0; i < matCalcTimes; i++)
                    {
                        answer[row, col] += arr1[row, i] * arr2[i, col];
                    }
                }
            }
            return answer;
        }
    }
}

```