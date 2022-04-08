---
title: "[알고리즘] 피로도"
date: 2021-10-27 11:15:28 -0400
categories: 알고리즘 완전탐색 백트랙킹 C#
---

### 문제 설명

- XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다.
- "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다.
-  예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

- 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다.
- 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- k는 1 이상 5,000 이하인 자연수입니다.
- dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
- dungeons의 가로(열) 길이는 2 입니다.
- dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
- "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
- "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
- 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.


### 입출력 예

```sh
k	    dungeons	                result
80	    [[80,20],[50,40],[30,10]]	3
```

### 접근 방식

- 정렬해서 풀려고 했는데, 충족 피로도가 크면 탐험을 못하고 감소 피로도가 너무 크면 이후 탐험에 지장이 생기기 때문에,, 완전 탐색으로 결과를 찾기로한다.
- 큐에 던전 정보를 담았다가, 하나씩 뽑아내고 갈 수 있는 던전이면 `questCount`를 1 증가시키고 다음 던전을 탐색하고 아니라면, 바로 다음 던전을 탐색한다.
- 그 후에 해당 던전을 먼저 탐색하지 않고 다른 던전을 먼저 탐색하기 위해 큐에 뽑아낸 던전을 다시 추가한다.



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
            int[,] dungeons = new int[,] { { 80, 20 }, { 50, 40 }, { 30, 10 } };
            int answer = sol.solution(80, dungeons);
            Console.WriteLine();
        }

        int maxQuestCount = 0;
        Queue<Tuple<int, int>> questQueue;
        public int solution(int k , int[,] dungeons)
        {
            int currentFatigue = k;
            questQueue = new Queue<Tuple<int, int>>();
            parseQuest(ref dungeons);
            backtrk(0, k);
            return maxQuestCount;

        }

        void parseQuest(ref int[,] quest)
        {
            for (int i = 0; i < quest.GetLength(0); i++)
            {
                Tuple<int, int> tuple = new Tuple<int, int>(quest[i, 0], quest[i, 1]);
                questQueue.Enqueue(tuple);
            }
        }

        void backtrk(int questCount, int currentFatigue)
        {
            if(questQueue.Count == 0)
            {
                maxQuestCount = Math.Max(questCount, maxQuestCount);
                return;
            }
            else
            {
                for(int idx = 0; idx < questQueue.Count; idx++)
                {
                    Tuple<int, int> fatigueQuest = questQueue.Dequeue();
                    if(currentFatigue >= fatigueQuest.Item1)
                    {
                        backtrk(questCount + 1, currentFatigue - fatigueQuest.Item2);
                    }
                    else
                        backtrk(questCount, currentFatigue);
                    questQueue.Enqueue(fatigueQuest);

                }
            }
        }

    }
}
```

