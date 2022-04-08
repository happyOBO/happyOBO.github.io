---
title: "[알고리즘] 괄호 회전하기"
date: 2021-11-07 9:15:28 -0400
categories: 알고리즘 스택 C#
---

### 문제 설명

- 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

- (), [], {} 는 모두 올바른 괄호 문자열입니다.
- 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
- 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
- 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- s의 길이는 1 이상 1,000 이하입니다.

### 입출력 예

```sh
s			result
"[](){}"	3
"}]()[{"	2
"[)(]"		0
"}}}"		0
```

### 접근 방식

- 시작 괄호면 push, 끝 괄호면 pop
- 아스키 코드 값 이용해서 코드 줄이기
- pop 할게 없다면 false 모든 동작이 끝났는데, 시작괄호가 스택에 남아있다면 false
- 그외에는 true 리턴
- true 개수 세기

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
            int answer = sol.solution("{}()[]");
            Console.WriteLine();
        }

        public int solution(string s)
        {
            int result = 0;
            List<char> listS = s.ToList<char>();
            for (int i = 0; i < s.Length; i++)
            {
                bool isRightBrk = IsRightBracket(listS);
                if (isRightBrk)
                    result++;
                char c = listS[0];
                listS.RemoveAt(0);
                listS.Add(c);

            }
            return result;
        }

        public bool IsRightBracket(List<char> s)
        {
            Stack<char> stck = new Stack<char>();

            foreach (char c in s)
            {
                switch (c)
                {
                    case '(':
                    case '{':
                    case '[':
                        {
                            stck.Push(c);
                        }
                        break;
                    case ')':
                    case '}':
                    case ']':
                        {
                            if (stck.Count == 0) return false;

                            char pop_c = stck.Pop();
                            if (!(pop_c + 1 == c || pop_c + 2 == c))
                                return false;
                        }
                        break;
                }

            }
            if (stck.Count > 0)
                return false;
            return true;
        }

    }
}

```