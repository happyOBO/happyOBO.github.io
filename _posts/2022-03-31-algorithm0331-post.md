---
title: "[알고리즘] 세그먼트 트리"
date: 2022-03-30 21:30:28 -0400
categories: 알고리즘 세그먼트트리 C++
---

### 세그먼트 트리

- 구간 합, 구간 곱을 구할 때 유용하게 쓸 수 있는 자료구조.
- 원래 구간 합을 구할 때 하나하나씩 더하면 `O(N)` 이 걸리지만, 트리 구조로 부분 구간 합들을 구해놓으면, 빠르게 구할 수 있다.
- [참고 사이트 블로그](https://m.blog.naver.com/ndb796/221282210534)


### 코드

- 최종 코드는 아래와 같다.


```cpp
#include <bits/stdc++.h>

#define NUMBER 12

using namespace std;


int a[] = { 1,9,3,8, 4, 5,5,9, 10, 3, 4, 5 };
int tree[4 * NUMBER];

int init(int start, int end, int node)
{
	if (start == end) return tree[node] = a[start];
	int mid = (start + end) / 2;
	// node * 2 : 왼쪽 자식 노드 , node * 2 + 1 : 오른쪽 자식 노드
	return tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}

// left , right  가 start ~ end 사이(현재 탐색하고 있는 구간합)에 있으면 더하기
int sum(int start, int end, int node, int left, int right)
{
	if (left > end || right < start) return 0;
	if (left <= start && end <= right) return tree[node];
	int mid = (start + end) / 2;
	return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right);
}

// diff : index 에 있던 이전값과 업데이트 된값의 차이
// a[index] : 10 -> 5 , diff : -5
void update(int start, int end, int node, int index, int diff)
{
	if (index < start || index > end) return;
	tree[node] += diff;
	if (start == end) return;
	int mid = (start + end) / 2;
	update(start, mid, node * 2, index, diff);
	update(mid + 1, end, node * 2 + 1, index, diff);

}

int main()
{
	init(0, NUMBER - 1, 1);
	int s = sum(0, NUMBER - 1, 1, 4, 8);
	update(0, NUMBER - 1, 1, 8, 5 - a[8]);
	return 0;
}
```
