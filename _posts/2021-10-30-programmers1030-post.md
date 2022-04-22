---
title: "[알고리즘] 거리두기 확인하기"
date: 2021-10-30 13:15:28 -0400
categories: 알고리즘 구현 C#
classes: wide
---

### 문제 설명

- 개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

- 코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
- 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

- 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
- 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
- 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
- 예를 들어,

- 5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다.
- 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다.
- 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

### 제한사항

- places의 행 길이(대기실 개수) = 5
- places의 각 행은 하나의 대기실 구조를 나타냅니다.
- places의 열 길이(대기실 세로 길이) = 5
- places의 원소는 P,O,X로 이루어진 문자열입니다.
- places 원소의 길이(대기실 가로 길이) = 5
- P는 응시자가 앉아있는 자리를 의미합니다.
- O는 빈 테이블을 의미합니다.
- X는 파티션을 의미합니다.
- 입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.
- return 값 형식
- 1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
- places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.
- 각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.


### 입출력 예

```sh
places	result
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	[1, 0, 1, 1, 1]
```

### 접근 방식

- 상하좌우 비교


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace Programmers
{
    class Program
    {

        static void Main(string[] args)
        {
            Program sol = new Program();
            string[,] places = new string[,] { { "OOOOP", "OOOPO", "OPXPX", "OOXOX", "POXXP" },
                                                { "POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP" },
                                                { "PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX" }, 
                                                { "OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO" }, 
                                                { "PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP" } };
            int[] answer = sol.solution(places);
            Console.WriteLine();
        }

        const int PLACE_SIZE = 5;
        int[] deltaY = new int[] { -1, 0, 1, 0 };
        int[] deltaX = new int[] { 0, -1, 0, 1 };
        public int[] solution(string[,] places)
        {
            int[] answer = new int[places.GetLength(0)];
            for(int place_idx = 0; place_idx < places.GetLength(0); place_idx++)
            {
                answer[place_idx] = searchManhattanAndPartitionRules(place_idx, ref places);
            }
            return answer;
        }

        public int searchManhattanAndPartitionRules(int place_idx, ref string[,] places)
        {
            for (int y = 0; y < PLACE_SIZE; y++)
            {
                for(int x = 0; x < PLACE_SIZE; x++)
                {
                    if(places[place_idx,y][x] == 'O')
                    {
                        int pCount = 0;
                        for(int i = 0; i < deltaY.Length; i++)
                        {
                            int surY = y + deltaY[i];
                            int surX = x + deltaX[i];
                            if(surX < 0 || surX >= PLACE_SIZE || surY < 0 || surY >= PLACE_SIZE)
                            {
                                continue;
                            }
                            if (places[place_idx, surY][surX] == 'P')
                                pCount++;

                        }
                        if (pCount > 1)
                            return 0;
                    }
                    if (places[place_idx, y][x] == 'P')
                    {
                        for (int i = 0; i < deltaY.Length; i++)
                        {
                            int surY = y + deltaY[i];
                            int surX = x + deltaX[i];
                            if (surX < 0 || surX >= PLACE_SIZE || surY < 0 || surY >= PLACE_SIZE)
                            {
                                continue;
                            }
                            if (places[place_idx, surY][surX] == 'P')
                                return 0;

                        }
                    }
                }

            }

            return 1;
        }

    }
}

```