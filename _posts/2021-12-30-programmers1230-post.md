---
title: "[알고리즘] 문자열 내 마음대로 정렬하기"
date: 2021-12-30 20:22:28 -0400
categories: 알고리즘 정렬 C#
---


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/13.png){: .align-center}

### 구현 방식

- 코드는 간단하지만, `Comparision` 메소드 및 람다식을 사용해 풀어서 기록해둔다.
- 정렬 메소드중 오버로드 된것중에 하나로는 `List<T>.Sort(Comparision<T>)` 가 있다.
- `Comparision<T>` 는 `delegate` 로 정의된 대리자로, `delegate int Comparison<in T>(T x, T y);` 로 
- `Comparison`에는 `x` 와 `y`를 받아서 `x`가 `y` 보다 작으면 0보다 작은 정수를, `x` 와 `y`가 같으면 0을, `x`가 `y` 보다 크면 1 을 리턴해야하는 함수를 할당해야한다.
- 이걸 쓰면 크고 작음의 기준을 커스텀하게 작성할 수 있어서 편리하다.


```csharp
public string[] solution(string[] strings, int n)
{
    List<string> stringList = new List<string>();
    stringList.AddRange(strings);

    stringList.Sort((x, y) =>
    {
        if (x[n] < y[n])
            return -1;
        else if (x[n] > y[n])
            return 1;
        else
        {
            int camparer = x.CompareTo(y);
            if (camparer < 0)
                return -1;
            else if (camparer == 0)
                return 0;
            else
                return 1;
        }
    }
    );

    return stringList.ToArray();
}
```