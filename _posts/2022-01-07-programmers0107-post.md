---
title: "[알고리즘] 캐시"
date: 2022-01-07 13:22:28 -0400
categories: 알고리즘 정렬 C++
classes: wide
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/14.png){: .align-center}

### 구현 방식

- 캐시에 현재 작업할 도시명이 있는지 판단한 후에 없으면 miss , 있으면 hit 분기문으로 넘어간다.
- 삽입 정렬방식을 이용해서, 한개씩 한개씩 뒤로 미루고 맨앞에 현재 도시명을 적는다.

```cpp
#include <string>
#include <vector>

using namespace std;
bool isSameCity(string a, string b);

int solution(int cacheSize, vector<string> cities) {

    int answer = 0;
    vector<string> cache = vector<string>(cacheSize);
    for (int i = 0; i < cities.size(); i++)
    {
        int pos = -1;
        for (int j = 0; j < cacheSize; j++)
        {
            if (isSameCity(cache[j] , cities[i]))
            {
                pos = j;
                break;
            }
        }
        // miss
        if (pos == -1)
        {
            answer += 5;

            for (int j = cacheSize - 1; j > 0; j--)
            {
                cache[j] = cache[j - 1];
            }
            if(cacheSize > 0)
                cache[0] = cities[i];
        }
        else
        {
            answer += 1;

            for (int j = pos; j > 0; j--)
            {
                cache[j] = cache[j - 1];
            }
            if (cacheSize > 0)
                cache[0] = cities[i];
        }
    }
    return answer;
}



bool isSameCity(string a, string b)
{

    if (a == b)
        return true;
    else if (a.size() != b.size())
        return false;
    else
    {
        for (int i = 0; i < a.size(); i++)
        {
            if (a[i] != b[i] && abs(a[i] - b[i]) != 32 )
                return false;
        }
    }

    return true;
}
```