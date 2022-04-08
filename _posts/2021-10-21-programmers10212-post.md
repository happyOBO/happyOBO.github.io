---
title: "[알고리즘] 기능개발"
date: 2021-10-21 16:15:28 -0400
categories: 알고리즘 C# 큐
---

### 문제 설명

- 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

- 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

- 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

### 제한 사항

- 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

### 입출력 예

```sh
progresses                  speeds	            return
[93, 30, 55]                [1, 30, 5]	        [2, 1]
[95, 90, 99, 99, 80, 99]    [1, 1, 1, 1, 1, 1]  [1, 3, 2]
```


### 접근 방식

1. 일단 형식을 큐로 변경한다.
2. 현재 작업의 완료 기간이 현재 릴리즈 기준 기간보다 크면 다음 릴리즈 배열 인덱스로 넘어가고
3. 아니라면 현재 릴리즈 배열 인덱스에 1을 더한다.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace pgm_dev
{
    class Program
    {

        

        static void Main(string[] args)
        {
            Program sol = new Program();
            int[] progresses = new int[] { 95, 95, 95, 95 };
            int[] speeds = new int[] { 4, 3, 2, 1 };
            int[] answer = sol.solution(progresses, speeds);
            Console.WriteLine( "");
        }

        public int[] solution(int[] progresses, int[] speeds)
        {
            
            Queue<Tuple<int, int>> taskSchedule;
            pushTask(progresses, speeds, out taskSchedule);

            int[] answer = calcReleaseTaskRate(taskSchedule).ToArray();

            return answer;
        }

        public void pushTask(int[] progresses, int[] speeds, out Queue<Tuple<int,int>> taskSchedule)
        {
            taskSchedule = new Queue<Tuple<int, int>>();
            int taskLength = progresses.Length;
            for(int i = 0; i < taskLength; i++)
            {
                taskSchedule.Enqueue(new Tuple<int, int>(progresses[i], speeds[i]));
            }

        }

        public List<int> calcReleaseTaskRate(Queue<Tuple<int, int>> taskSchedule)
        {
            List<int> releaseTaskRate = new List<int>();
            int currentReleaseDate = 0;
            int releaseCount = -1;
            while(taskSchedule.Count > 0)
            {
                int completeDate = calcCompleteDate(taskSchedule.Dequeue());
                if (currentReleaseDate < completeDate)
                {
                    releaseCount++;
                    releaseTaskRate.Add(1);
                    currentReleaseDate += (completeDate - currentReleaseDate);
                }
                else
                {
                    releaseTaskRate[releaseCount]++;

                }

            }

            return releaseTaskRate;

        }


        public int calcCompleteDate(Tuple<int,int> task)
        {
            int progress = task.Item1;
            int speed = task.Item2;
            int remainProgress = 100 - task.Item1;
            int completeDate = remainProgress / speed;
            if (remainProgress % speed > 0) completeDate++;
            return completeDate;
        }

  }
}

```

