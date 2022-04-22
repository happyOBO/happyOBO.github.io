---
title: "[알고리즘] 입국심사"
date: 2022-01-09 22:22:28 -0400
categories: 알고리즘 이분탐색 C++
classes: wide
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/17.png){: .align-center}

### 구현 방식

- 결정 문제로 이분탐색으로 풀자.. --> **탐색 시간에 N명 이상을 심사할 수 있는가!**
- 초기 최소 시간 (`left`) : `min(times) x (사람수 n  / 심사관 수)`
- 초기 최대 시간 (`right`) : `max(times) x max ( 1, (사람수 n / 심사관 수))` (사람수가 심사관 수보다 작으면 이게 0 이 되어버려서 1 이상 값으로 해아함)
- 특정 시간에 심사 받을수 있는 최대 인원수 : `SUM ( [특정시간] / times[i] )`
- 이분 탐색을 하면,, 딱 `midTotalTime` 값이 이상적인 최소 최대 값이 나오진 않는다. 만약 `while (minTotalTime <= maxTotalTime)` 를 빠져나오기 직전에 만약 `canJudgeN(midTotalTime, n, times)` 값이 `false` 로 나오면, `midTotalTime` 값이 조건을 만족치 못하는 값으로 나온다.
- 그러므로 `canJudgeN(midTotalTime, n, times)` 을 만족할때 `answer` 값을 찾아주는 식으로한다.

```cpp
#include <string>
#include <vector>
#include <limits.h>

using namespace std;


long long solution(int n, vector<int> times);
bool canJudgeN(long long targetTimes, int n, vector<int>& times);


long long solution(int n, vector<int> times) {
    int minTime = INT_MAX;
    int maxTime = INT_MIN;
    long long answer = LONG_MAX;
    for (auto it = times.begin(); it != times.end(); it++)
    {
        minTime = min(minTime, (*it));
        maxTime = max(maxTime, (*it));
    }

    long long minTotalTime = static_cast<long long>(minTime) * static_cast<long long>(n / times.size());
    long long maxTotalTime = static_cast<long long>(maxTime) * max(static_cast<int>(n / times.size()), 1);
    long long midTotalTime = (minTotalTime + maxTotalTime) / 2;

    while (minTotalTime <= maxTotalTime)
    {
        if (canJudgeN(midTotalTime, n, times))
        {
            maxTotalTime = midTotalTime - 1;
            answer = min(answer, midTotalTime);
        }
        else
            minTotalTime = midTotalTime + 1;
        midTotalTime = (minTotalTime + maxTotalTime) / 2;

    }
    return answer;
}

bool canJudgeN(long long targetTimes, int n, vector<int>& times)
{
    long long count = 0;
    for (auto it = times.begin(); it != times.end(); it++)
        count += (targetTimes / static_cast<long long>(*it));
    return n <= count;
}
```