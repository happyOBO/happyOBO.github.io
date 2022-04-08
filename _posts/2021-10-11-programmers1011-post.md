---
title: "[알고리즘] 내적"
date: 2021-10-11 22:31:28 -0400
categories: 알고리즘 C#
---



### 코드


```csharp
using System;

public class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for(int i = 0; i < a.Length; i++)
        {
            answer += (a[i] * b[i]);
        }

        return answer;
    }
}
```