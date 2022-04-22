---
title: "[알고리즘] 체육복"
date: 2021-11-27 12:31:28 -0400
categories: 알고리즘 그리디 C#
classes: wide
---


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/02.png){: .align-center}



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
            int[,] sizes = new int[,] { { 14, 4 }, { 19, 6 }, { 6, 16 }, { 18, 7 }, { 7, 11 } };
            int answer = sol.solution(5, new int[] {2,3,4 }, new int[] {1,2,3});
            Console.WriteLine();
        }
        public int solution(int n, int[] lost, int[] reserve)
        {
            List<int> losts = new List<int>();
            losts.AddRange(lost);
            List<int> reserves = new List<int>();
            reserves.AddRange(reserve);
            losts.Sort();
            reserves.Sort();

            int count = n - lost.Length;
            foreach(int ls in lost)
            {
                if(reserves.Contains(ls))
                {
                    losts.Remove(ls);
                    reserves.Remove(ls);
                    count++;
                }    
            }

            int num = losts[0];
            while (losts.Count > 0 && reserves.Count > 0)
            {
                if (num - 1 == reserves[0] || num + 1 == reserves[0] || num == reserves[0])
                {
                    losts.Remove(num);
                    if (losts.Count > 0)
                        num = losts[0];
                    reserves.Remove(reserves[0]);
                    count++;
                }
                else if (num < reserves[0])
                {
                    losts.Remove(num);
                    if (losts.Count > 0)
                        num = losts[0];
                }
                else
                {
                    reserves.Remove(reserves[0]);
                }
            }
            return count;
        }


    }

}
```