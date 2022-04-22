---
title: "[알고리즘] 소수 만들기"
date: 2021-12-17 21:11:28 -0400
categories: 알고리즘 DFS C#
classes: wide
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/04.png){: .align-center}


```csharp
using System;

class Solution
{
    int count = 0;
    int[] nums;
    public int solution(int[] nums)
    {
        this.nums = nums;

        dfs(0, 0, 0);

        return this.count;
    }

    public void dfs(int count , int sum, int currIdx)
    {
        if (count == 3)
        {
            if(IsPrime(sum))
                this.count++;
        }
        else
        {
            for (int i = currIdx; i < nums.Length; i++)
                dfs(count + 1, sum + nums[i], i + 1);

        }
    }

    public static bool IsPrime(int number)
    {
        if (number <= 1) return false;
        if (number == 2) return true;
        if (number % 2 == 0) return false;

        var boundary = (int)Math.Floor(Math.Sqrt(number));

        for (int i = 3; i <= boundary; i += 2)
            if (number % i == 0)
                return false;

        return true;
    }
}
```