---
title: "[알고리즘] 행렬의덧셈"
date: 2021-11-01 19:15:28 -0400
categories: 알고리즘 구현 C#
classes: wide
---


### 문제 설명

- 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

### 제한 조건

- 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.


### 입출력 예

```sh
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
```

### 작동 방식

- 그냥 더하면 된다. ~~커밋 채워야해서 1단계 문제를 푼건 안비밀..~~

```csharp
public class Solution {
    public int[,] solution(int[,] arr1, int[,] arr2)
    {
        int[,] answer = new int[arr1.GetLength(0), arr1.GetLength(1)];
        for(int y = 0; y < arr1.GetLength(0); y++)
        {
            for(int x = 0; x < arr1.GetLength(1); x++)
            {
                answer[y, x] = arr1[y, x] + arr2[y, x];
            }
        }
        return answer;
    }
}
```