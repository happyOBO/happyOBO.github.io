---
title: "[알고리즘] 별 찍기 - 19 (boj_10944)"
date: 2020-08-23 10:15:28 -0400
categories: 재귀 알고리즘
classes: wide
---

### 별 찍기 - 19 

## 문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

### 입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

### 출력
첫째 줄부터 차례대로 별을 출력한다.

```bash
# 예제 입력 1 
1
# 예제 출력 1 
*
# 예제 입력 2 
2
# 예제 출력 2 
*****
*   *
* * *
*   *
*****
# 예제 입력 3 
3
# 예제 출력 3 
*********
*       *
* ***** *
* *   * *
* * * * *
* *   * *
* ***** *
*       *
*********
# 예제 입력 4 
4
# 예제 출력 4 
*************
*           *
* ********* *
* *       * *
* * ***** * *
* * *   * * *
* * * * * * *
* * *   * * *
* * ***** * *
* *       * *
* ********* *
*           *
*************
```


### 생각한 알고리즘

- 길이 및 재귀 시작 좌표 규칙은 다음과 같다.

```bash
# 최대 변 길이 (입력 N 이 들어 왔을 때)
N : 1 -> 1
N : 2 -> 5
N : 3 -> 9
N : 4 -> 13
# 4*(n-1) + 1


# 시작좌표 (입력이 3이 들어 왔을 때)
3 : 0.0
2 : 2,2
1 : 4,4
# 2(N-n), 2(N-n)

```
- i번째에 해당하는 테두리가 ``*`` 인 직사각형을 그려내고
- i-1 번째 함수를 호출한다.


### 답안 코드

```cpp
#include <iostream>

using namespace std;
char arr[450][450];
int N;
void recur(int leng)
{
    int st = 2*(N-leng); 

    for(int i = st; i < st + 4 * (leng-1) +1 ; i++)
    {
        for(int j = st; j < st + 4 * (leng-1) +1 ; j++)
        {
            if(i == st || i ==  st + 4 * (leng-1))
            {
                arr[i][j] = '*';
            }
            else if(j == st || j == st + 4*(leng-1))
            {
                arr[i][j] = '*';
            }

        }
    }
    if(1 < leng)
        recur(leng-1);
}

int main(void)
{

    cin>>N;
    for(int i = 0; i < 4 * (N-1) +1 ; i++)
    {
        for(int j = 0; j < 4 * (N-1) +1 ; j++)
        {
            arr[i][j] = ' ';
        }
    }
    recur(N);
    for(int i = 0; i < 4 * (N-1) +1 ; i++)
    {
        for(int j = 0; j < 4 * (N-1) +1 ; j++)
        {
            printf("%c",arr[i][j]);
        }
        printf("\n");
    }
    
}


```