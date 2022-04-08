---
title: "[알고리즘] 빠진 수 하나 찾기"
date: 2021-10-20 13:15:28 -0400
categories: 알고리즘 구현
---


### 빠진 수 하나 찾기

- 기존 숫자 리스트 s1 에서 숫자 하나가 빠진 숫자 리스트 s2 가 있을 때, 어떤 수가 없는지 찾아내는 문제
- 숫자는 0 ~ 2^30 까지의 숫자 , 리스트의 원소 개수는 1000개 이하



### 문제 해결 방법

- 문제가 간단해서 빨리 풀려면 어떻게 해야하지 싶어서 정렬을 할까 하다가 정렬을 하면 더 오래 걸릴 것 같고
- 하나하나 비교를 하자면, 숫자 하나 찾는데 왜이렇게 비효율적이지란 생각이 들었다.
- 그래서 든 생각! 숫자 하나면 `잃어버린 숫자 = s1 의 모든 원소 합 - s2의 모든 원소의 합`으로 해도 되지 않을까!
- 근데 이렇게 하면 합한 숫자가 너무 커져서 1000 * 2^30 이면 `Int32`의 MaxValue 를 넘어버린다. 
- 그래서 생각한 방법이..! `잃어버린 숫자 = sum( s1의 i번 째 원소 - s2의 i번 째 원소 ) + s1의 N번째 원소` 면은 숫자가 커지지 않고 합하면서 구할 수 있다...!


### 해결 코드

- 해결 코드는 아래와 같다.


```csharp
static void Main(string[] args)
{
    int maxValue = Int32.MaxValue / 2;
    Console.WriteLine(maxValue);
    Console.WriteLine(solution(new int[] { maxValue, maxValue, maxValue, maxValue, maxValue, maxValue, maxValue, maxValue } , new int[] { maxValue, maxValue, maxValue, maxValue, maxValue, maxValue, maxValue}));
}

static int solution(int[] s1 , int[] s2)
{
    int s2Length = s2.Length;
    int result = 0;
    for(int i = 0; i < s2Length; i++)
    {
        result += (s1[i] - s2[i]);
    }

    result += s1[s1.Length - 1];

    return result;
}
```