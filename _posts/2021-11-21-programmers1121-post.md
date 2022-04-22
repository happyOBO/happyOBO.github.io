---
title: "[알고리즘] 모음 사전"
date: 2021-11-21 12:31:28 -0400
categories: 알고리즘 DFS C#
classes: wide
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/01.png){: .align-center}


### 접근 방식

- DFS 면 A , AA ... 이런식으로 가장 먼저 것 부터 쑥쑥 확인할 수 있다.
- BFS 먄 A , B , C .. 이런 식 이겠지


```csharp

using System;
using System.Collections.Generic;


namespace Programmers
{
    class Program
    {


        static void Main(string[] args)
        {
            Program sol = new Program();
            int answer = sol.solution("AAAAE");
            Console.WriteLine();
        }
        public int count = 0;
        public int targetCount;
        List<char> vowels = new List<char>() { 'A', 'E', 'I', 'O', 'U' };

        public int solution(string word)
        {
            dfs("", ref word);
            return targetCount;
        }


        public void dfs(string currWord , ref string targetWord)
        {
            if (currWord.Equals(targetWord))
            {
                targetCount = count;
                return;
            }
            if (currWord.Length == 5)
                return;

            foreach(char c in vowels)
            {
                count++;
                string word = currWord + c;
                dfs(word, ref targetWord);

            }

        }
    }
}
```