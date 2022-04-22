---
title: "[알고리즘] 영지 선택"
date: 2022-01-10 11:19:28 -0400
categories: 알고리즘 동적계획법 C++
classes: wide
---

## 문제 내용

- 세종대왕은 현수에게 현수가 다스릴 수 있는 영지를 하사하기로 했다. 전체 땅은 사각형으로 표시된다. 그 사각형의 땅 중에서 세종대왕이 현수가 다스릴 수 있는 땅의 크기(세로의 길이와 가로의 길이)를 정해주면 전체 땅 중에서 그 크기의 땅의 위치를 현수가 정하면 되는 것이다.
- 전체 땅은 사각형의 모양의 격자로 되어 있으며, 그 사각형 땅 안에는 많은 오렌지 나무가 심겨져 있다. 현수는 오렌지를 무척 좋아하여 오렌지 나무가 가장 많이 포함되는 지역을 선택하고 싶어 한다. 현수가 얻을 수 있는 영지의 오렌지 나무 최대 개수를 출력하는 프로그램을 작성하세요. 다음과 같은 땅의 정보가 주어지고, 현수가 하사받을 크기가, 가로 2, 세로 3의 크기이면 가장 많은 오렌지 나무가 있는 영지는 총 오렌지 나무의 개수가 16인 3행 4열부터 시작하는 구역이다.


### 입력설명

- 첫 줄에 H(세로길이)와 W(가로길이)가 입력된다. (1<=H, W<=700) 그 다음 H줄에 걸쳐 각 사각형 지역에 오렌지의 나무 개수(1~9개) 정보가 주어진다.
- 그 다음 영지의 크기인 세로길이(1~H)와 가로길이(1~W)가 차례로 입력된다.


```
6 7
3 5 1 3 1 3 2
1 2 1 3 1 1 2
1 3 1 5 1 3 4
5 1 1 3 1 3 2
3 1 1 3 1 1 2
1 3 1 3 1 2 2
2 3
```

### 출력설명

- 첫 줄에 현수가 얻을 수 있는 오렌지 나무의 최대 개수를 출력한다.


```
16
```

### 구현 방식

- 동적 계획법을 이용해서 이전 기록을 누적하는 `M` 를 이용한다.
- `M[i][j]` 는 `input[1~i][1~j]`까지의 합을 의미한다.
- `input[ay + 1 ~ by][ax + 1 ~ by]` 까지의 합은 `M[by][bx] - M[ay][bx] - M[by][ax] + M[ay][ax]` 을 의미한다.
- 그래서 기록해가지고 최대값을 구하면 된다!

```cpp

void solution(int H, int W, int mH, int mW, vector<vector<int>>& inputs) {

    vector<vector<int>> accMat = vector<vector<int>>(H + 1, vector<int>(W + 1 ,0));
    for (int y = 1; y <= H; y++)
    {
        for (int x = 1; x <= W; x++)
        {
            accMat[y][x] = inputs[y][x] + accMat[y - 1][x] + accMat[y][x - 1] - accMat[y - 1][x - 1];
        }
    }
    int maxSum = INT_MIN;
    for (int y = mH; y <= H; y++)
    {
        for (int x = mW; x <= W; x++)
        {
            pair<int, int> minPos = make_pair(y - mH, x - mW);
            pair<int, int> maxPos = make_pair(y , x);
            int subSum = accMat[maxPos.first][maxPos.second]
                    - accMat[minPos.first][maxPos.second]
                    - accMat[maxPos.first][minPos.second]
                    + accMat[minPos.first][minPos.second];
            maxSum = max(subSum, maxSum);
        }
    }
    cout << maxSum;
}

```

