---
title: "[알고리즘] 병합 정렬"
date: 2021-10-10 11:19:28 -0400
categories: 알고리즘 정렬 C++
classes: wide
---

### 입력설명

- 이미 정렬 되어 있는 두 배열을 합쳐서 정렬된 하나의 배열을 만든다.
- 그래프의 후위 탐색 방식을 이용해서 `left ~ mid` 와 `mid +1 ~ right` 배열 원소들이 각각 정렬되어 있다고 가정하고, 
- 두 배열을 하나의 정렬 배열로 합친다.


```cpp
void mergeSort(int lt, int rt)
{
    int mid;
    int p1, p2, p3;
    if (lt < rt)
    {
        mid = (lt + rt) / 2;
        mergeSort(lt, mid);
        mergeSort(mid + 1, rt);

        p1 = lt; p2 = mid + 1; p3 = lt;

        while (p1 <= mid && p2 <= rt)
        {
            if (arr[p1] < arr[p2])tmp[p3++] = arr[p1++];
            else tmp[p3++] = arr[p2++];
        }

        while (p1 <= mid) tmp[p3++] = arr[p1++];
        while (p2 <= rt) tmp[p3++] = arr[p2++];

        for (int i = lt; i <= rt; i++) arr[i] = tmp[i];

    }

}
```


