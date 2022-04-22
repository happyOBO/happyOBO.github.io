---
title: "[알고리즘] 두개 뽑아서 더하기"
date: 2021-10-01 9:15:28 -0400
categories: 알고리즘 C#
classes: wide
---

### 문제 설명

- 정수 배열 numbers가 주어집니다.
- numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- numbers의 길이는 2 이상 100 이하입니다.
- numbers의 모든 수는 0 이상 100 이하입니다.

### 입출력 예

```sh
numbers		result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
```

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
            int[] numbers = new int[] { 2, 1, 3, 4, 1 };
            int[] answer = sol.solution(numbers);
            Console.WriteLine();
        }

        public int[] solution(int[] numbers)
        {
            List<int> answer = new List<int>();
            for(int i = 0; i < numbers.Length; i++)
            {
                for(int j = i + 1; j < numbers.Length; j++)
                {
                    if (!answer.Contains(numbers[i] + numbers[j]))
                        answer.Add(numbers[i] + numbers[j]);
                }
            }
            answer.Sort();
            return answer.ToArray();
        }
    }
}

```