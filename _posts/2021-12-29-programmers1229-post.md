---
title: "[알고리즘] 예상 대진표"
date: 2021-12-29 16:22:28 -0400
categories: 알고리즘 이분탐색 C#
---


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/12.png){: .align-center}

### 구현 방식

- 요거는 이분 탐색으로 쪼갰을 때 양쪽에 있으면 개수 계산하는 방식으로
- `n` 의 수를 받았을 때 2의 몇제곱인지 확인하기
- 숫자 a, b 가 쪼갠 양쪽에 위치하면 리턴
- 한쪽으로 치우쳐져 있으면 치우친쪽으로 다시 쪼개기



```csharp
enum Position
{
    BothLeft = -1, // 왼쪽에 치우친 경우
    Bisection = 0, // 양쪽에 잘 분배된 경우
    BothRight = 1, // 오른쪽에 치우친 경우
}

public int solution(int n, int a, int b)
{
    int answer = calcFactor(n);
    int num1 = Math.Min(a, b);
    int num2 = Math.Max(a, b);

    int mid = n / 2;
    (int start, int end) prev = (1, mid);
    (int start, int end) post = (mid + 1, n);
    while(true)
    {
        Position pos = calcPosition(prev, post, num1, num2);
        switch(pos)
        {
            case Position.BothLeft:
                {
                    mid = (prev.start + prev.end) / 2;
                    post = (mid + 1, prev.end);
                    prev = (prev.start, mid);

                    answer--;
                    break;
                }
            case Position.Bisection:
                {
                    return answer;
                }
            case Position.BothRight:
                {
                    mid = (post.start + post.end) / 2;
                    prev = (post.start, mid);
                    post = (mid + 1, post.end);
                    answer--;
                    break;
                }
        }

    }
    return answer;
}

public int calcFactor(int n)
{
    int count = 0;
    while( n > 1)
    {
        n /= 2;
        count++;
    }

    return count;
}

public Position calcPosition((int start, int end) prev , (int start, int end) post , int a , int b)
{
    if (a <= prev.end && b <= prev.end)
        return Position.BothLeft;
    else if (a <= prev.end && post.start <= b)
        return Position.Bisection;
    else
        return Position.BothRight;

}
```