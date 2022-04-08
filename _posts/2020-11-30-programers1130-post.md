---
title: "[자율주행] 알고리즘 자료구조 기초"
date: 2020-11-30 19:41:28 -0400
categories: ROS
---

### 알아두면 좋은 ``Python3`` 내장 함수

```py
>> a = [1,14,19,21,5,3]

>> a.insert(2,77)
a = [1,14,77,19,21,5,3]

>> a.index(19)
3

>> a.remove(21)
a = [1,14,77,19,5,3]

>> a.append(404)
a = [1,14,77,19,5,3,404]

>> a.pop()
a = [1,14,77,19,5,3]

## 정렬

>> newlist = sorted(a)
a = [1,14,77,19,5,3]
newlist = [1, 3, 5, 14, 19, 77]

>> a.sort()
a = [1, 3, 5, 14, 19, 77]

>> revlist = sorted(a,reverse = True)
revlist = [77, 19, 14, 5, 3, 1]

>> strlist = ['my', 'name', 'is', 'obo']
>> strlist = sorted(strlist, key=lambda s: len(s))
strlist = ['my', 'is', 'obo', 'name']


>> strlist = sorted(strlist, key=lambda s: len(s) , reverse = True)
strlist =['name', 'obo', 'my', 'is']

>> L = [ {'name' : 'pencil', 'score' : 99}, {'name' : 'book', 'score' : 70}]
>> L.sort(key = lambda x : x['name'])
L = [{'name': 'book', 'score': 70}, {'name': 'pencil', 'score': 99}]
```

### 이분 탐색

- 정렬된 리스트에서 상수 x 의 인덱스를 알아내려고한다. 이때 탐색하는 부분리스트의 중간값이 x 보다 작으면/크면 중간 값 이전/이후 부분 배열을 버리는 것(탐색하지 않는것)을 이용한다.

- 코드는 다음과 같다.

```py
def solution(L, x):
    answer = 0
    row = 0
    high = len(L)-1
    while(row <= high and high < len(L)):
        middle = (row + high) // 2
        if( L[middle] == x):
            return middle
        elif(L[middle] < x):
            row = middle +1
        else:
            high = middle - 1
    return -1
```


### 재귀 알고리즘

- 재귀 알고리즘을 사용해서 조합 (n개의 서로 다른 원소에서 m를 택하는 경우의 수)을 구해보자.

```
C(n,m) = n! / (m! * (n-m)!)
C(n,m) = C(n-1,m) + C(n-1, m-1)
-> 특정한 하나의 원소 입장에서 볼 때, 이 원소를 포함하는 경우와 그렇지 않은 경우를 따로 계산해서 더한다.
``` 

### 이분 탐색 알고리즘 재귀 버전

```py
def solution(L, x, l, u):
    if (u < l or len(L) <= u):
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)

    else:
        return solution(L, x, mid+1, u)

```


### 연결 리스트

```py
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        data = 0
        if self.nodeCount == 0 or pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        if self.nodeCount == 1:
            data = self.head.data
            self.head = None
            self.tail = None
        elif pos == 1:
            data = self.head.data
            self.head = self.head.next
        else:
            prev = self.getAt(pos-1)
            curr = self.getAt(pos)
            data = curr.data
            if pos == self.nodeCount: #tail
                self.tail = prev
                self.tail.next = None
            else:
                prev.next = curr.next
        self.nodeCount -= 1
        return data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0

```

### Level 2 연습문제

**문제 설명**
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 가장 끝쪽의 모서리 한 줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
빨간색 격자의 수 red는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

```s
입출력 예
brown	red	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
```

**문제 풀이**

- red + brown 값의 약수를 구한다.

```py
def solution(brown, red):
    answer = []
    total = brown + red
    comm_list = []
    for i in range(2,total//2):
        if(total % i == 0):
            brown_row = total // i
            brown_col = i
            brown_total = 2*brown_row + 2 * brown_col - 4
            # print( "brown : ", brown_row , brown_col,"red : ",brown_row - 2 ,brown_col -2)
            if(brown_total == brown):
                red_row = brown_row - 2
                red_col = brown_col -2
                red_total = red_row * red_col
                if(red_total == red):
                    return [brown_row , brown_col]
    return answer
```