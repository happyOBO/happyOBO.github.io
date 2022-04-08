---
title: "[알고리즘] 에리 - 카드 (boj_15728)"
date: 2020-08-11 15:05:28 -0400
categories: 완전탐색
---
### 에리 - 카드

### 문제
- 2468년 개최된 해왕성 올림픽, ‘에리 - 카드’는 드디어 올림픽 정식 종목으로 채택된다. ‘에리 - 카드’는 N 장의 ‘공유 숫자카드’와 N 장의 ‘팀 숫자카드’를 받고 시작한다. 상대 팀은 우리 팀의 ‘팀 숫자카드’ K 장을 견제할 수 있는데, 견제된 카드는 낼 수 없게 된다. 모든 견제가 마친 후 우리 팀은 ‘공유 숫자카드’에서 한 장, ‘팀 숫자카드’ 중 한 장씩을 골라 내게 되는데, 두 카드의 곱이 우리 팀의 점수가 되며 이후 같은 방식으로 상대 팀도 진행하여 상대 팀의 점수보다 높을 경우 이기게 된다.

- 상대팀은 항상 최선의 방법으로 N장의 우리 팀의 ‘팀 숫자카드’ 중 K장을 견제한다고 했을 때, 우리 팀이 얻을 수 있는 최대 점수를 출력하는 프로그램을 작성하시오.

### 입출력 예제
```bash
# input
5 2
-1 2 3 4 5
-1 0 2 3 4

# output
10
```

### 생각한 알고리즘
- 원래 처음에는 받은 카드를 정렬하여, 그리디 알고리즘으로 풀었으나,
- 음수 * 음수는 최댓값이 될수 있기 때문에 완전 탐색으로 진행한다.

```cpp

for(K+1 개수만큼 진행)
{
    for(N 개수 만큼 진행)
    {
        for(현재 남아있는 팀카드의 개수만큼 진행)
        {
            맥스값, 맥스값을 만드는 팀카드의 인덱스 찾기
        }
    }
    K개수만큼 맥스값을 만드는 팀카드 삭제
    K+1번째 돌 때의 맥스값은 우리가 원하는 맥스값
}
```
- 코드는 다음과 같다.

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
    int N,K;
    vector<int> share_cards;
    vector<int> team_cards;
    cin>>N>>K;
    for(int i = 0; i<N;i++)
    {
        int card;
        cin>>card;
        share_cards.push_back(card);
    } 
    for(int i = 0; i<N;i++)
    {
        int card;
        cin>>card;
        team_cards.push_back(card);
    } 

    long int max= -100000000;
    int max_team_card_index= 0;
    for(int k = 0; k < K+1; k++)
    {
        max= -100000000;
        for(int i = 0; i< N; i++)
        {
            for(int j = 0; j<N-k;j++)
            {
                
                if(max < share_cards[i] * team_cards[j])
                {
                    max = share_cards[i] * team_cards[j];
                    max_team_card_index = j;
                }
            }
        }
        if(k < K)
            team_cards.erase(team_cards.begin() + max_team_card_index);
        
    }

    cout<<max;

}

```