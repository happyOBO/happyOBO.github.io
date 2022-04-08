---
title: "[알고리즘] ATM (boj_11399)"
date: 2020-08-10 00:05:28 -0400
categories: 그리디
---

### 그리디란?
- 가장 최선의 방법 루트로 탐색하는것
- 동적 계획법보다 효율이 좋지만, 빼먹는게 많다.

### 문제
인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다. 예를 들어, 총 5명이 있고, P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자. [1, 2, 3, 4, 5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다. 2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다. 3번 사람은 1번, 2번 사람이 돈을 뽑을 때까지 기다려야 하기 때문에, 총 3+1+4 = 8분이 필요하게 된다. 4번 사람은 3+1+4+3 = 11분, 5번 사람은 3+1+4+3+2 = 13분이 걸리게 된다. 이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.
줄을 [2, 5, 1, 4, 3] 순서로 줄을 서면, 2번 사람은 1분만에, 5번 사람은 1+2 = 3분, 1번 사람은 1+2+3 = 6분, 4번 사람은 1+2+3+3 = 9분, 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다. 각 사람이 돈을 인출하는데 필요한 시간의 합은 1+3+6+9+13 = 32분이다. 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

### 입출력 예제
```bash
# input
5
3 1 4 3 2
# output
32
```
### 생각한 알고리즘

- 받은 배열 정렬
- result는 i는 1 ~ N까지의 값에 대해서 1 ~i 값을 계속 더해서 N까지 진행시킨것의 누적 합이다.

```cpp
#include <iostream>

using namespace std;

void quick_sort(int *data, int start, int end){
    if(start >= end){
        // 원소가 1개인 경우
        return; 
    }
    
    int pivot = start;
    int i = pivot + 1; // 왼쪽 출발 지점 
    int j = end; // 오른쪽 출발 지점
    int temp;
    
    while(i <= j){
        // 포인터가 엇갈릴때까지 반복
        while(i <= end && data[i] <= data[pivot]){
            i++;
        }
        while(j > start && data[j] >= data[pivot]){
            j--;
        }
        
        if(i > j){
            // 엇갈림
            temp = data[j];
            data[j] = data[pivot];
            data[pivot] = temp;
        }else{
            // i번째와 j번째를 스왑
            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
        }
    } 
    
    // 분할 계산
    quick_sort(data, start, j - 1);
    quick_sort(data, j +1, end );
}


int acc_sum(int *data,int n)
{
    int acc = 0;
    for(int i = 0; i< n;i++)
    {
        for(int j = 0; j<=i;j++)
        {
            acc +=data[j];
        }
    }
    return acc;
}


int main(void)
{
    int N;
    int p[1010] = {0,};
    cin>>N;
    for(int i = 0;i<N;i++)
    {
        cin>>p[i];
    }
    
    quick_sort(p,0,N-1);
    int result = acc_sum(p,N);

    cout<<result;
}
```