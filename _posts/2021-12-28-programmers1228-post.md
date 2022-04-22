---
title: "[알고리즘] 행렬 테두리 회전하기"
date: 2021-12-28 10:22:28 -0400
categories: 알고리즘 구현 C#
classes: wide
---


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/09.png){: .align-center}

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/10.png){: .align-center}

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/11.png){: .align-center}


### 구현 방식


- 통으로 배열로 만든 뒤, 회전 시킨다.
  - `RotateAndCheckMin` : 하나의 `query`를 회전시키고, 최솟값 구하기
  - `OnDirectionIncrease` : 총 네 방향으로 움직여야하는데(오른쪽, 아래, 왼쪽, 위) , 한 방향으로 움직일때 배열 변화 체크

```csharp

int[,] board;
int minNum = int.MaxValue;
public int[] solution(int rows, int columns, int[,] queries)
{
    board = new int[rows, columns];
    int[] answer = new int[queries.GetLength(0)];
    for (int i = 1; i <= rows; i++)
        for (int j = 1; j <= columns; j++)
            board[i - 1, j - 1] = (i - 1) * columns + j;
    for(int queryIdx = 0; queryIdx < queries.GetLength(0); queryIdx++)
    {
        answer[queryIdx] = RotateAndCheckMin((queries[queryIdx, 0] - 1, queries[queryIdx, 1] - 1), (queries[queryIdx, 2] - 1, queries[queryIdx, 3] - 1));
    }
    return answer;
}

public int RotateAndCheckMin((int y , int x) minPos , (int y, int x) maxPos)
{

    minNum = int.MaxValue;
    int prevNum = board[minPos.y +1, minPos.x];
    prevNum = OnDirectionIncrease((minPos.y, minPos.x), (minPos.y, maxPos.x), (0, 1), prevNum);
    prevNum = OnDirectionIncrease((minPos.y, maxPos.x), (maxPos.y, maxPos.x), (1, 0), prevNum);
    prevNum = OnDirectionIncrease((maxPos.y, maxPos.x), (maxPos.y, minPos.x), (0, -1), prevNum);
    prevNum = OnDirectionIncrease((maxPos.y, minPos.x), (minPos.y, minPos.x), (-1, 0), prevNum);
    return minNum;
}

public int OnDirectionIncrease((int y, int x) startPos , (int y, int x) endPos , (int y, int x) term, int initNum)
{
    (int y, int x) pos = startPos;
    int prevNum = initNum;
    while(pos.x != endPos.x || pos.y != endPos.y)
    {
        int tmpNum = board[pos.y, pos.x];
        board[pos.y, pos.x] = prevNum;
        prevNum = tmpNum;

        pos.x += term.x;
        pos.y += term.y;
        minNum = Math.Min(tmpNum, minNum);
    }

    return prevNum;
}

```
