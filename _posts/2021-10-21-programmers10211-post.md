---
title: "[알고리즘] 위장"
date: 2021-10-21 14:15:28 -0400
categories: 알고리즘 백트랙킹 C#
classes: wide
---


### 문제

- 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
- 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

```sh
종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
```

- 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

#### 제한사항
- clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
- 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 존재하지 않습니다.
- clothes의 모든 원소는 문자열로 이루어져 있습니다.
- 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
- 스파이는 하루에 최소 한 개의 의상은 입습니다.


### 접근 방식 -1

- 딕셔너리로 변경한 뒤에 백트래킹으로 풀자.
- 딕셔너리에서 키 1 ~ N개까지 뽑는 조합을 구해서 더한다.
- 마지막에 시간 초과가 발생한다.

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace pgm_dev
{
    class Program
    {

        Dictionary<string, int> closet;
        int N;
        bool[] visited;
        string[] KindsOfClothes;
        int backtrkResult = 0;

        static void Main(string[] args)
        {
            Program sol = new Program();
            string[,] clothes = new string[,] { { "0", "0" }, { "10", "1" }, { "20", "2" }, { "30", "3" }, { "40", "4" }, { "50", "5" }, { "60", "6" }, { "70", "7" }, { "80", "8" }, { "90", "9" }, { "100", "10" }, { "110", "11" }, { "120", "12" }, { "130", "13" }, { "140", "14" }, { "150", "15" }, { "160", "16" }, { "170", "17" }, { "180", "18" }, { "190", "19" }, { "200", "20" }, { "210", "21" }, { "220", "22" }, { "230", "23" }, { "240", "24" }, { "250", "25" }, { "260", "26" }, { "270", "27" }, { "280", "28" }, { "290", "29" } }
            int answer = sol.solution(clothes);
            Console.WriteLine( answer);
        }

        public int solution(string[,] clothes)
        {

            closet = parseKeyandValue(clothes);
            N = closet.Count();
            visited = new bool[N];
            KindsOfClothes = closet.Keys.ToArray();


            for(int i = 0; i < visited.Length; i++)
            {
                visited[i] = false;
            }

            int answer = pickOneToN();


            return answer;
        }

        public Dictionary<string, int> parseKeyandValue(string[,] clothes)
        {
            Dictionary<string, int> closet = new Dictionary<string,int>();
            for (int i = 0; i < clothes.GetLength(0); i++)
            {
                string KindOfClothes = clothes[i, 1];
                string NameOfClothes = clothes[i, 0];
                if (!closet.ContainsKey(KindOfClothes))
                    closet.Add(KindOfClothes, 1);
                else
                    closet[KindOfClothes] += 1;
            }
            return closet;
        }

        public int pickOneToN()
        {
            for(int pickCnt = 1; pickCnt <= N; pickCnt++)
            {
                backtrk(0, pickCnt);
            }

            return backtrkResult;
        }

        public void backtrk(int cnt, int destCnt)
        {
            if(cnt == destCnt)
            {
                int res = 1;
                for(int i = 0; i < N;i++)
                {
                    if (visited[i])
                        res *= closet[KindsOfClothes[i]];                 
                }

                backtrkResult += res;
                return;
            }

            for(int i = cnt; i < N; i++)
            {
                if(!visited[i])
                {
                    visited[i] = true;
                    backtrk(cnt + 1, destCnt);
                    visited[i] = false;
                      
                }
            }

        }

    }
}

```


### 접근 방식 -2

- 구글링해서 얻은 접근 방식이다. 
- 옷을 최소 1종류는 입어야한다.
- 만약에 옷이 2 종류 이고 각각 2 벌 , 3 벌 이라면, 안입는 경우의 수를 포함해서 2 + 1 벌 , 3 + 1 벌 이라고 생각할 수 있다.
- 그러면 3 * 4 를 해서 총 12 종류의 옷을 입을 수 있지만, 아예 안 입는 경우 ( X , X ) 도 포함되어 있기 때문에 1을 빼준다.

```sh
X :  A, B -- > A , B , X
Y : a , b, c -- > a, b, c, X

(X + 1) * (Y + 1) - 1 = 11
```

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace pgm_dev
{
    class Program
    {

        Dictionary<string, int> closet;

        static void Main(string[] args)
        {
            Program sol = new Program();
            string[,] clothes = new string[,] { { "0", "0" }, { "10", "1" }, { "20", "2" }, { "30", "3" }, { "40", "4" }, { "50", "5" }, { "60", "6" }, { "70", "7" }, { "80", "8" }, { "90", "9" }, { "100", "10" }, { "110", "11" }, { "120", "12" }, { "130", "13" }, { "140", "14" }, { "150", "15" }, { "160", "16" }, { "170", "17" }, { "180", "18" }, { "190", "19" }, { "200", "20" }, { "210", "21" }, { "220", "22" }, { "230", "23" }, { "240", "24" }, { "250", "25" }, { "260", "26" }, { "270", "27" }, { "280", "28" }, { "290", "29" } };
            int answer = sol.solution(clothes);
            Console.WriteLine( answer);
        }

        public int solution(string[,] clothes)
        {

            closet = parseKeyandValue(clothes);

            int answer = calcNumPickClothes();


            return answer;
        }

        public Dictionary<string, int> parseKeyandValue(string[,] clothes)
        {
            Dictionary<string, int> closet = new Dictionary<string,int>();
            for (int i = 0; i < clothes.GetLength(0); i++)
            {
                string KindOfClothes = clothes[i, 1];
                if (!closet.ContainsKey(KindOfClothes))
                    closet.Add(KindOfClothes, 1);
                else
                    closet[KindOfClothes] += 1;
            }
            return closet;
        }
        public int calcNumPickClothes()
        {
            int result = 1;
            foreach(KeyValuePair<string, int> keyValue in closet)
            {
                result *= (keyValue.Value + 1);
            }

            result -= 1;
            return result;
        }


    }
}



```