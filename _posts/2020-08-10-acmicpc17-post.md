---
title: "[알고리즘] 다항함수의 미분 (boj_15725)"
date: 2020-08-10 23:05:28 -0400
categories: C++
classes: wide
---

### 문제
최대 일차 일변수 다항식이 주어졌을 때 그 함수를 미분한 결과를 출력하는 프로그램을 작성하시오.

### 입력
첫째 줄에 최대 일차 일변수 다항식이 주어진다. 항의 개수는 최대 2개이고, 변수는 항상 x로 주어지며, 각 항은 공백 문자로 구분되지 않는다. 주어지는 계수와 상수의 절댓값은 10,000을 넘지 않는 정수이다. 단, 계수의 절댓값이 1인 경우에는 계수를 생략한다. 차수가 같은 항은 한 번만 주어진다.

다항식은 차수가 큰 것부터 작아지는 순서대로 주어진다.

### 예제 및 counter example

```bash
6x-6 # 6
+7x-10 # 7
x-x+x-x # 0
-10x+1+9x # -1
```
### 생각한 알고리즘
1. 입력받은 문자열들의 캐릭터 하나하나를 앞에서부터 탐색한다.
2. 숫자 형태인(48이상 57이하) 캐릭터는 스택에 누적시킨다.
3. 그외의 문자를 마주치면 스택을 비운다.
4. 캐릭터 'x'를 마주치면 순서대로 숫자 캐릭터를 pop하고 알맞게 더한다.

```cpp
#include <iostream>
#include <cstring>
#include <queue>
#include <cmath>

using namespace std;

int main(void)
{
    char arr[30];
    cin>>arr;
    int arr_len = strlen(arr);
    int acc = 0;
    queue<char> que;
    for(int i = 0; i< arr_len;i++)
    {
        if(arr[i] == 'x')
        {
            int is_plus = 1;
            if( !que.empty() &&(que.front() == '-' ||que.front() == '+') )
            {
                if(que.front() == '-')
                    is_plus = -1;
                que.pop();
            }
            if(que.empty())
            {
                acc = acc + is_plus;
            }
            while(!que.empty())
            {
                int add = (que.front() - 48) * pow(10,que.size()-1);
                acc = acc + is_plus * add;
                que.pop();
            }
        }
        else if(!( 48 <= arr[i] && arr[i]<= 57))
        {
            while(!que.empty())
            {
                que.pop();
            }
            
        }
        que.push(arr[i]);
    }
    cout<<acc;
}
```