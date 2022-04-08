---
title: "[알고리즘] 예산"
date: 2021-12-16 21:11:28 -0400
categories: 알고리즘 정렬 C# Linq
---


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/03.png){: .align-center}


### 구현 방식

- 이번에는 람다식을 이용해서 풀어보았다. `Count(Func<int,bool>)` 을 이용했더니 `for`문을 쓰지 않아도 되어서 코드가 깔끔해졌다.
- 앞으로 자주 써야겠다.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] d, int budget)
    {
        List<int> dl = new List<int>();
        dl.AddRange(d);
        dl.Sort();
        int result = 0;
        int answer = dl.Count(
            x =>
            {
                if (result + x <= budget)
                {
                    result += x;
                    return true;
                }
                else
                    return false;
            }
            );
        return answer;
    }
}
```