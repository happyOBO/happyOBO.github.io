---
title: "[알고리즘] 올바른 괄호"
date: 2021-11-06 19:15:28 -0400
categories: 알고리즘 스택 C#
classes: wide
---


### 문제 설명

- 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

- "()()" 또는 "(())()" 는 올바른 괄호입니다.
- ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
- '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

### 제한사항

- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.


### 입출력 예

```sh
s	        answer
"()()"	    true
"(())()"	true
")()("	    false
"(()("	    false
```

### 구현 방식

- 시작 괄호면 push, 끝 괄호면 pop
- pop 할게 없다면 false 모든 동작이 끝났는데, 시작괄호가 스택에 남아있다면 false
- 그외에는 true 리턴


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
            bool answer = sol.solution("(())()");
            Console.WriteLine();
        }

        public bool solution(string s)
        {
            Stack<char> stck = new Stack<char>();

            foreach(char c in s)
            {
                if(c.Equals('('))
                {
                    stck.Push('(');
                }
                else
                {
                    if (stck.Count == 0)
                        return false;
                    else
                    {
                        stck.Pop();
                    }
                }

            }
            if (stck.Count > 0)
                return false;
            return true;
        }

    }
}


```


