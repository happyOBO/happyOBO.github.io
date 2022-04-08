---
title: "[알고리즘] 숫자 문자열과 영단어"
date: 2021-11-02 19:15:28 -0400
categories: 알고리즘 구현 C#
---

### 문제 설명

- 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

- 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

```sh
1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
```

- 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

- 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

```sh
숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine
```


### 제한사항
- 1 ≤ s의 길이 ≤ 50
- s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
- return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

### 입출력 예

```sh
s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123
```

### 접근 방식

- 딕셔너리 이용


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
            int answer = sol.solution("100");
            Console.WriteLine();
        }
        public int solution(string s)
        {
            Dictionary<string, int> num_dict = new Dictionary<string, int>();
            num_dict.Add("zero", 0);
            num_dict.Add("one", 1);
            num_dict.Add("two", 2);
            num_dict.Add("three", 3);
            num_dict.Add("four", 4);
            num_dict.Add("five", 5);
            num_dict.Add("six", 6);
            num_dict.Add("seven", 7);
            num_dict.Add("eight", 8);
            num_dict.Add("nine", 9);

            string str_answer = "";
            string num_english = "";
            foreach (char c in s)
            {
                if(48 <= c && c < 59)
                {
                    str_answer += c;
                }
                else
                {
                    num_english += c;
                }
                if ( num_english.Length > 0 && num_dict.ContainsKey(num_english))
                {
                    str_answer += num_dict[num_english];
                    num_english = "";
                }
            }
            int answer = int.Parse(str_answer);
            return answer;
        }
    }
}

```