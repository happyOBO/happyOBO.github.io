---
title: "[알고리즘] 교점에 별 만들기"
date: 2021-11-04 19:15:28 -0400
categories: 알고리즘 구현 C#
---

### 문제 설명

- Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

- 예를 들어, 다음과 같은 직선 5개를
  - 2x - y + 4 = 0
  - -2x - y + 4 = 0
  - -y + 1 = 0
  - 5x - 8y - 12 = 0
  - 5x + 8y + 12 = 0
- 이때, 모든 교점의 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4), (1.5, 1.0), (2.1, -0.19), (0, -1.5), (-2.1, -0.19), (-1.5, 1.0)입니다.
- 이 중 정수로만 표현되는 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4)입니다.

- 문자열로 나타낼 때, 별이 그려진 부분은 *, 빈 공간(격자선이 교차하는 지점)은 .으로 표현하면 다음과 같습니다.

```sh
"..........."  
".....*....."  
"..........."  
"..........."  
".*.......*."  
"..........."  
"..........."  
"..........."  
"..........."  
".*.......*."  
"..........."  
```

- 이때 격자판은 무한히 넓으니 모든 별을 포함하는 최소한의 크기만 나타내면 됩니다.

- 따라서 정답은

```sh
"....*...."  
"........."  
"........."  
"*.......*"  
"........."  
"........."  
"........."  
"........."  
"*.......*"  
```

- 직선 A, B, C에 대한 정보가 담긴 배열 line이 매개변수로 주어집니다. 이때 모든 별을 포함하는 최소 사각형을 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- line의 세로(행) 길이는 2 이상 1,000 이하인 자연수입니다.
- line의 가로(열) 길이는 3입니다.
- line의 각 원소는 [A, B, C] 형태입니다.
- A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
- 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
- A = 0이면서 B = 0인 경우는 주어지지 않습니다.
- 정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
- 별이 한 개 이상 그려지는 입력만 주어집니다.

### 입출력 예

```sh
line	result
[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
[[0, 1, -1], [1, 0, -1], [1, 0, 1]]	["*.*"]
[[1, -1, 0], [2, -1, 0]]	["*"]
[[1, -1, 0], [2, -1, 0], [4, -1, 0]]	["*"]
```


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
            int[,] line = new int[,] { { 0, 1, -1 }, { 1, 0, -1 }, { 1, 0, 1 } };
            string[] answer = sol.solution(line);
            Console.WriteLine();
        }

        Tuple<int, int> maxX = new Tuple<int, int>(int.MaxValue, -int.MaxValue);
        Tuple<int,int> maxY = new Tuple<int, int>(int.MaxValue, -int.MaxValue);
        public string[] solution(int[,] line)
        {
            List<Tuple<int, int>> starPoints = new List<Tuple<int, int>>();
            for(int i = 0; i < line.GetLength(0); i++)
            {

                for(int j = i + 1; j < line.GetLength(0); j++)
                {
                    Tuple<int, int> intersectionPoint = calcintersectionpoint((double)line[i, 0], (double)line[i, 1], (double)line[i, 2], (double)line[j, 0], (double)line[j, 1], (double)line[j, 2]);
                    if (intersectionPoint != null)
                        starPoints.Add(intersectionPoint);

                }
            }
            string[] answer = new string[maxY.Item2 - maxY.Item1+1];
            string resRow = "";
            for (int i = maxX.Item1; i <= maxX.Item2; i++) resRow += ".";
            for (int i = 0; i <= maxY.Item2 - maxY.Item1; i++) answer[i] = resRow;
            int standardX = maxX.Item1;
            int standardY = maxY.Item2;
            foreach (Tuple<int,int> point in starPoints)
            {
                int y = point.Item1;
                int x = point.Item2;
                answer[standardY - y] = ReplaceAt(ref answer[standardY - y], x - standardX, '*');
            }
            return answer;
        }

        public string ReplaceAt(ref string target , int idx , char obj)
        {
            string res = "";
            for(int i = 0; i < target.Length; i++)
            {
                if (i == idx)
                    res += obj;
                else
                    res += target[i];
            }

            return res;
        }
        public Tuple<int,int> calcintersectionpoint(double a1, double b1 , double c1 , double a2 , double b2, double c2)
        {
            int resX;
            int resY;
            if((a1 * b2 - b1 * a2) == 0.0)
            {
                if (a1 == 0.0 && a2 == 0.0 || b1 == 0.0 && b2 == 0.0)
                    return null; 
                if (a1 == 0.0)
                {
                    resX = c2 == 0.0 ? 0 : (int)(-a2 / c2);
                    resY = c1 == 0.0 ? 0 : (int)(-b1 / c1);
                }
                else
                {
                    resX = c1 == 0.0 ? 0 : (int)(-a1 / c1);
                    resY = c2 == 0.0 ? 0 : (int)(-b2 / c2);
                }
            }
            else
            {
                double x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1);
                double y = (c1 * a2 - a1 * c2) / (a1 * b2 - b1 * a2); 
                if (Math.Abs(x - (int)x) > 0 || Math.Abs(y - (int)y) > 0)
                    return null;
                if (double.IsNaN(x) || double.IsNaN(y))
                    return null;
                resX = (int)x;
                resY = (int)y;

            }
            maxX = new Tuple<int,int> (Math.Min(resX, maxX.Item1) , Math.Max(resX, maxX.Item2) );
            maxY = new Tuple<int, int>(Math.Min(resY, maxY.Item1), Math.Max(resY, maxY.Item2));
            Tuple<int,int> point = new Tuple<int,int>(resY, resX);
            return point;
        }

    }
}

```