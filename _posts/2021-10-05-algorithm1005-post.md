---
title: "[알고리즘] 조세퍼스 문제"
date: 2021-10-05 11:22:28 -0400
categories: 알고리즘 구현 C++
classes: wide
---

### 문제 설명

- 정보 왕국의 이웃 나라 외동딸 공주가 숲속의 괴물에게 잡혀갔습니다.
- 정보 왕국에는 왕자가 N명이 있는데 서로 공주를 구하러 가겠다고 합니다. 정보왕국의 왕은 다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기로 했습니다.
- 왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다. 그리고 1번 왕자부터 N 번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다. 
- 그리고 1번 왕자부터 시 계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다. 한 왕자가 K(특정숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다. 
- 그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다. 이렇게 해서 마지막까지 남은 왕자가 공주를 구하러 갈 수 있다.
- 예를 들어 총 8명의 왕자가 있고, 3을 외친 왕자가 제외된다고 하자. 처음에는 3번 왕자가 3 을 외쳐 제외된다. 이어 6, 1, 5, 2, 8, 4번 왕자가 차례대로 제외되고 마지막까지 남게 된 7 번 왕자에게 공주를 구하러갑니다.
- N과 K가 주어질 때 공주를 구하러 갈 왕자의 번호를 출력하는 프로그램을 작성하시오.

### 구현 방식 - 1

- 연결리스트 및 이터레이터를 사용해서 풀 수 있다.

```cpp

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

void solution(int N, int K){
    list<int> orders;
    for (int i = 1; i <= N; i++)
    {
        orders.push_back(i);
    }
    int count = K -1;
    list<int>::iterator it = orders.begin();
    while (orders.size() > 1)
    {
        if (count <= 0)
        {
            orders.erase(it++);
            count = K;
        }
        else
            it++;

        if (it == orders.end())
            it = orders.begin();
        count--;
    }

    cout << *orders.begin();
}

```


### 동일 유형( 멀티 태스킹)

- 현수의 컴퓨터는 멀티태스킹이 가능하다. 처리해야 할 작업이 N개 들어오면 현수의 컴퓨터는 작업을 1부터 N까지의 번호를 부여하고 처리를 다음과 같이 한다.
    1. 컴퓨터는 1번 작업부터 순서대로 1초씩 작업을 한다. 즉 각 작업을 1초만 작업하고 다음 작업을 하는 식이다.
    2. 마지막 번호의 작업을 1초 했으면 다시 1번 작업으로 가서 다시 1초씩 후속 처리를 한다. 3) 처리가 끝난 작업은 작업 스케쥴에서 사라지고 새로운 작업은 들어오지 않는다.
- 그런데 현수의 컴퓨터가 일을 시작한 지 K초 후에 정전이 되어 컴퓨터가 일시적으로 멈추었 다. 전기가 들어오고 나서 현수의 컴퓨터가 몇 번 작업부터 다시 시작해야 하는지 알아내는 프로그램을 작성하세요.

### 구현방식 -2

- 아래와 같이 포인터 인덱스 변수를 이용해서 바로 벡터 자료형으로 접근할 수 있다.


```cpp

void solution(int K, int N, vector<int>& schedules){

    int pointer = 0;
    int  count = 0;

    while (true)
    {
        pointer++;
        if (pointer > N) pointer = 1;
        if (schedules[pointer] == 0)
            continue;
        else
        {
            schedules[pointer]--;
            count++;
        }
        if (K == count)
            break;
    }

    while (true)
    {
        pointer++;
        if (pointer > N) pointer = 1;
        if (schedules[pointer] > 0)
            break;
    }
    cout << pointer;

}


// 연결 리스트 사용


int solution(vector<int> food_times, long long k){
    int N = food_times.size();
    int count = 0;

    list<pair<int, int>> food_orders;
    for (int i = 0; i < N; i++)
    {
        food_orders.push_back(make_pair(i + 1, food_times[i]));  
    }

    list<pair<int, int>>::iterator it = food_orders.begin();


    while (true)
    {
        if (count == k)
        {
            break;
        }
        else
        {
            (*it).second--;
            if ((*it).second <= 0)
                food_orders.erase(it++);
            else
                it++;
            count++;
            if (it == food_orders.end())
                it = food_orders.begin();
        }
    }
    return (*it).first;

}
```