---
title: "[알고리즘] 나머지가 1이 되는 수 찾기"
date: 2021-06-23 19:15:28 -0400
categories: 알고리즘 구현 C#
classes: wide
---


### 문제 설명

- 자연수 n이 매개변수로 주어집니다.
- n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

### 제한사항

- 3 ≤ n ≤ 1,000,000


### 입출력 예

```sh
n	result
10	3
12	11
```


```csharp
using System;

public class Solution {
    public int solution(int n)
    {
        for(int i = 1; i < n; i++)
        {
            if (n % i == 1)
                return i;
        }
        return -1;
    }
}
```