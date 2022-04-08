---
title: "[자율주행] Python3 에서 heap 응용 문제"
date: 2020-12-04 16:41:28 -0400
categories: ROS
---


## heap 응용문제 ; 배상 비용최소화 사본

### **문제 설명**

- OO 조선소에서는 태풍으로 인한 작업지연으로 수주한 선박들을 기한 내에 완성하지 못할 것이 예상됩니다. 기한 내에 완성하지 못하면 손해 배상을 해야 하므로 남은 일의 작업량을 숫자로 매기고 배상비용을 최소화하는 방법을 찾으려고 합니다.
배상 비용은 각 선박의 완성까지 남은 일의 작업량을 제곱하여 모두 더한 값이 됩니다.

- 조선소에서는 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리할 수 있습니다. 조선소에서 작업할 수 있는 N 시간과 각 일에 대한 작업량이 담긴 배열(works)이 있을 때 배상 비용을 최소화한 결과를 반환하는 함수를 만들어 주세요. 예를 들어, N=4일 때, 선박별로 남은 일의 작업량이 works = [4, 3, 3]이라면 배상 비용을 최소화하기 위해 일을 한 결과는 [2, 2, 2]가 되고 배상 비용은 22 + 22 + 22 = 12가 되어 12를 반환해 줍니다.

- 제한사항
    - 일할 수 있는 시간 N : 1,000,000 이하의 자연수
    - 배열 works의 크기 : 1,000 이하의 자연수
    - 각 일에 대한 작업량 : 1,000 이하의 자연수

- **입출력 예**

```s
N	works	result
4	[4,3,3]	12
2	[3,3,3]	17
```

### 문제 풀이

- Max heap 을 이용하여 가장 top에 있는것에 1을 빼고 재정렬한다.
- 처음에는 Max heap 을 사용해서 문제를 풀려고 했지만, Python3 라이브러리에는 기본적으로 Min heap 만을 제공하고 있다.
- 그래서, ``works`` 리스트의 원소들을 ``음수``로 변경한다. 그러면 Min heap으로 Max heap과 같은 효과를 볼수 있다.

```py
import heapq
def solution(no, works):
    result = 0
    negative_works = []
    for w in works:
        negative_works.append(-w) # 음수로 변환
    heapq.heapify(negative_works) # Min heap 생성
    while(no > 0):
        ship = heapq.heappop(negative_works) # 제일 작은 음수 ( 가장 큰수) 를 pop
        if(ship < 0):
            heapq.heappush(negative_works, ship+1)
            no -= 1
        else:
            break # 만약, 0 이라면, 모든 수가 0이 되었으므로 더이상의 일을 그만한다.
    
    for nw in negative_works:
        result += (nw)**2
    return result
```