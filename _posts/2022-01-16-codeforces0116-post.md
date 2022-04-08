---
title: "[알고리즘] Not Shading"
date: 2022-01-16 01:30:28 -0400
categories: 알고리즘 구현 C++
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/23.png){: .align-center}

### 입력

```
9
3 5 1 4
WBWWW
BBBWB
WWBBB
4 3 2 1
BWW
BBW
WBB
WWB
2 3 2 2
WWW
WWW
2 2 1 1
WW
WB
5 9 5 9
WWWWWWWWW
WBWBWBBBW
WBBBWWBWW
WBWBWBBBW
WWWWWWWWW
1 1 1 1
B
1 1 1 1
W
1 2 1 1
WB
2 1 1 1
W
B

```

### 출력

```
1
0
-1
2
2
0
-1
1
1

```

### 구현 방식

- `-1` : 블랙이 하나라도 없는 경우
- `0` : (r,c) 에 있는 cell 이 블랙인 경우
- `1` : r 또는 c 행 렬 쪽에 블랙이 하나라도 있는 경우
- `2` : 블랙이 하나라도 있는 경우
- ~~영어로 풀려고 하니까,, 문제 이해 속도가 너무 느리다... 영어 공부좀 할걸~~

```cpp

#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <limits.h>

using namespace std;

void solution(int n, int m, int r, int c);

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        int n, m, r, c;
        cin >> n >> m >> r >> c;
        solution(n, m , r , c);
    }
}

void solution(int n, int m , int r , int c)
{
    int result = INT_MAX;
    for (int row = 1; row <= n; row++)
    {
        for (int column = 1; column <= m; column++)
        {
            char cell;
            cin >> cell;
            if (cell == 'B')
            {
                if (row == r && column == c)
                    result = min(0,result);
                else if (row == r || column == c)
                    result = min(1,result);
                else
                    result = min(2,result);
            }

        }
    }
    if (result == INT_MAX)
        cout << -1 << endl;
    else
        cout << result << endl;

}
```