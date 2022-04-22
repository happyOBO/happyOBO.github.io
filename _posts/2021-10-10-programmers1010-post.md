---
title: "[알고리즘] 올바른 괄호"
date: 2021-10-10 19:15:28 -0400
categories: 알고리즘 C#
classes: wide
---


- 쉬운거 그만 풀고,,, 제대로된 문제를 풀자..


```csharp

public string solution(string s)
{
    string answer = "";
    int sLength = s.Length;
    if (sLength % 2 == 0) answer += s[sLength / 2 -1];
    answer += s[sLength / 2];
    return answer;
}
```