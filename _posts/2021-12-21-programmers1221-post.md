---
title: "[알고리즘] 교점에 별만들기"
date: 2021-12-21 23:46:28 -0400
categories: 알고리즘 구현 C# Linq
classes: wide
---

![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/07.png){: .align-center}

### 구현 방식

- 교점에 해당 하면 `Intersections`에 추가
- 원래는 주석 처리한 부분처럼 `Aggregate`를 이용해서 `MinMaxValue`를 따졌지만, 그렇게 했더니, 오류가 나서 일단 클래스를 새로 만들어서 진행한 상태
- 테스트 입력값이 계산중에 int 자료 형을 넘어서 `long`으로 중간에 치환을 해줘야하기 때문에 중간 캐스팅이 많아짐..

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace Programmers
{

    public class MinMax
    {
        public int maxY = int.MinValue;
        public int minY = int.MaxValue;
        public int maxX = int.MinValue;
        public int minX = int.MaxValue;

    }

    class Program
    {


        static void Main(string[] args)
        {
            Program sol = new Program();
            //int[,] line = new int[,] { { 2, -1, 4 }, { -2, -1, 4 }, { 0, -1, 1 }, { 5, -8, -12 }, { 5, 8, 12 } };
            //int[,] line = new int[,] { {0,1,-1 }, { 1,0,-1}, { 1,0,1}};
            int[,] line = new int[,] { {2, -1, 4 }, { -2, -1, 4}, { 0, -1, 1}, { 5, -8, -12}, { 5, 8 , 12} };
            string[] answer = sol.solution(line);
            Console.WriteLine();
        }

        public string[] solution(int[,] line)
        {
            List<((int a, int b, int c) line1, (int a, int b, int c) line2)> lineCrt = new List<((int a, int b, int c) line1, (int a, int b, int c) line2)>();
            for (int i = 0; i < line.GetLength(0); i++)
            {
                for (int j = i + 1; j < line.GetLength(0); j++)
                {
                    lineCrt.Add(((line[i, 0], line[i, 1], line[i, 2]), (line[j, 0], line[j, 1], line[j, 2])));
                }
            }

            IEnumerable<(long y, long x)> Intersections = lineCrt.Where(
                l =>
                {
                    long mod = (long)l.line1.a * (long)l.line2.b - (long)l.line1.b * (long)l.line2.a;
                    if (mod != 0.0f)
                    {
                        long yNumer = (long)l.line1.c * (long)l.line2.a - (long)l.line1.a * (long)l.line2.c;
                        long xNumer = (long)l.line1.b * (long)l.line2.c - (long)l.line1.c * (long)l.line2.b;
                        return yNumer % mod == 0 && xNumer % mod == 0;
                    }
                    return false;
                }
                ).Select(l =>
                {
                    long mod = (long)l.line1.a * (long)l.line2.b - (long)l.line1.b * (long)l.line2.a;
                    long yNumer = (long)l.line1.c * (long)l.line2.a - (long)l.line1.a * (long)l.line2.c;
                    long xNumer = (long)l.line1.b * (long)l.line2.c - (long)l.line1.c * (long)l.line2.b;
                    return (yNumer / mod, xNumer / mod);
                }
                );

            //(int maxY, int minY, int maxX, int minX) MinMaxValue= Intersections.Aggregate(
            //    (int.MinValue, int.MaxValue, int.MinValue, int.MaxValue),
            //    ((int maxY, int minY, int maxX, int minX) result, (int y, int x) point) => 
            //    (Math.Max(result.maxY, point.y), Math.Min(result.minY, point.y) , Math.Max(result.maxX, point.x), Math.Min(result.minX, point.x)));

            MinMax MinMaxValue = new MinMax();
            foreach ((long y, long x) point in Intersections)
            {
                MinMaxValue.maxY = Math.Max(MinMaxValue.maxY, (int)point.y);
                MinMaxValue.minY = Math.Min(MinMaxValue.minY, (int)point.y);
                MinMaxValue.maxX = Math.Max(MinMaxValue.maxX, (int)point.x);
                MinMaxValue.minX = Math.Min(MinMaxValue.minX, (int)point.x);
            }

            List<char>[] starBoard = new List<char>[MinMaxValue.maxY - MinMaxValue.minY + 1];
            char[] resRow = new char[MinMaxValue.maxX - MinMaxValue.minX + 1];
            for (int i = 0; i <= MinMaxValue.maxX - MinMaxValue.minX; i++) resRow[i] = '.';
            for (int i = 0; i <= MinMaxValue.maxY - MinMaxValue.minY; i++) starBoard[i] = new List<char>(resRow);
            int standardX = MinMaxValue.minX;
            int standardY = MinMaxValue.maxY;
            foreach ((long y, long x) point in Intersections)
            {
                starBoard[standardY - (int)point.y][(int)point.x - standardX] = '*';
            }

            string[] answer = new string[MinMaxValue.maxY - MinMaxValue.minY + 1];
            for (int i = 0; i <= MinMaxValue.maxY - MinMaxValue.minY; i++)
                answer[i] = starBoard[i].Aggregate("", (string result, char x) => { result += x; return result; });

            return answer;
        }


    }

}

```