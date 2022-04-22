---
title: "[알고리즘] 교집합 (투 포인터 알고리즘)"
date: 2021-10-07 11:22:28 -0400
categories: 알고리즘 정렬 C++
classes: wide
---

### 문제 설명

- 두 집합 A, B가 주어지면 두 집합의 교집합을 출력하는 프로그램을 작성하세요.
- 첫 번째 줄에 집합 A의 크기 N(1<=N<=30,000)이 주어집니다.
- 두 번째 줄에 N개의 원소가 주어집니다. 원소가 중복되어 주어지지 않습니다. 세 번째 줄에 집합 B의 크기 M(1<=M<=30,000)이 주어집니다.
- 네 번째 줄에 M개의 원소가 주어집니다. 원소가 중복되어 주어지지 않습니다. 각 집합의 원소는 int형 변수의 크기를 넘지 않습니다.

### 접근 방식

- 두배열의 크기가 각각 10^4 이상이므로 이중 for문을 사용하면 약 연산량이 1억이 되어 시간초과가 날 수 도 있다.
- 맨처음에 생각했던 방식은 딕셔너리로 첫번째 배열을 파싱 한 후에 두번째 배열을 키값으로 갖으면 교집합에 추가하는 식으로 할려고 했다. 그 이후에 소트
- 두번째 방식(문제의 의도)은 두 배열을 따로 정렬을 한 다음에 각 배열의 이터레이터 변수를 생성해서 비교후에 같으면 교집합에 추가하고, 아니라면, 값이 작은 이터레이터에 1 을 더한다.


```cpp

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


void solution(int N1, vector<int> list1, int N2, vector<int> list2) {

    vector<int> answer;
    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());

    vector<int>::iterator it1 = list1.begin();
    vector<int>::iterator it2 = list2.begin();
    while (it1 != list1.end() && it2 != list2.end())
    {
        if ((*it1) < (*it2))
        {
            it1++;
        }
        else if ((*it1) > (*it2))
        {
            it2++;
        }
        else
        {
            answer.push_back(*it1);
            it1++;
            it2++;
        }
    }


    for (int i = 0; i < answer.size(); i++)
    {
        cout << answer[i] << " ";
    }

}


```