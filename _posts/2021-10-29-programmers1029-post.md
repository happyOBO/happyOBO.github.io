---
title: "[알고리즘] 최댓값과 최솟값"
date: 2021-10-29 23:15:28 -0400
categories: 알고리즘 구현 C#
classes: wide
---



### 문제 설명

- 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.

- 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

### 제한 조건

- s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.


### 입출력 예


```sh
s	return
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
```

### 접근 방식

- 파싱 하고, 소트하고, 리턴! 끝!


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
            string answer = sol.solution("-1 -2 -3 -4");
            Console.WriteLine();
        }

        public string solution(string s)
        {
            string[] parseNums = s.Split();
            List<int> nums = new List<int>();
            
            foreach (string n in parseNums)
                nums.Add(Int32.Parse(n));

            nums.Sort();

            string answer = nums[0].ToString() + " " + nums[parseNums.Length-1].ToString();

            return answer;
        }
    }
}


```