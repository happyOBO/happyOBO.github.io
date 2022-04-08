---
title: "[알고리즘] 단어 변환"
date: 2021-12-27 22:22:28 -0400
categories: 알고리즘 그래프 BFS C#
---


![[no-alignment]]({{ site.url }}{{ site.baseurl }}/assets/images/post-programmers/08.png){: .align-center}

### 구현 방식


- 그래프 세팅
  - 그래프로 단어들 마다(`begin` 을 포함한) Vertex 로 추가하고, 하나의 문자만 차이나는 단어들을 `edges`에 추가한다.
- BFS 로 탐색해서 최단 거리를 찾아낸다.
- 이때 최단거리를 찾아낼수 없는 경우면 0을 리턴한다.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace Programmers
{

    public class Vertex
    {
        public Vertex(string word)
        {
            this.word = word;
        }
        public string word;
        public int dist = 0;
        public List<Vertex> edges = new List<Vertex>();
    }

    class Program
    {


        static void Main(string[] args)
        {
            Program sol = new Program();
            int[,] line = new int[,] { {2, -1, 4 }, { -2, -1, 4}, { 0, -1, 1}, { 5, -8, -12}, { 5, 8 , 12} };
            int answer = sol.solution("hit", "cog", new string[] { "hot", "dot", "dog", "lot", "log", "cog" });
            Console.WriteLine();
        }

        Dictionary<string, Vertex> wordGraph;
        Dictionary<string, bool> visited;
        Dictionary<string, string> parent;

        public int solution(string begin, string target, string[] words)
        {
            List<string> wordList = new List<string>();
            wordList.AddRange(words);
            wordList.Add(begin);

            SetWordGraph(out wordGraph, wordList);

            return bfs(begin, target);
        }

        public void SetWordGraph(out Dictionary<string, Vertex> wordGraph, List<string> words)
        {
            wordGraph = new Dictionary<string, Vertex>();
            visited = new Dictionary<string, bool>();
            parent = new Dictionary<string, string>();
            for (int i = 0; i < words.Count; i++)
            {
                wordGraph[words[i]] = new Vertex(words[i]);
                visited[words[i]] = false;
            }
            for (int i = 0; i < words.Count; i++)
            {

                for (int j = i + 1; j < words.Count; j++)
                {

                    if (isDifferOneChar(words[i], words[j]))
                    {
                        wordGraph[words[i]].edges.Add(wordGraph[words[j]]);
                        wordGraph[words[j]].edges.Add(wordGraph[words[i]]);
                    }
                }

            }
        }

        public bool isDifferOneChar(string s1, string s2)
        {
            bool isDiffered = false;
            for(int i = 0; i < s1.Length; i++)
            {
                if(s1[i] != s2[i])
                {
                    if (!isDiffered)
                        isDiffered = true;
                    else
                        return false;
                }
            }

            return true;
        }

        public int bfs(string begin, string target)
        {
            visited[begin] = true;
            parent[begin] = begin;
            Queue<string> queue = new Queue<string>();
            wordGraph[begin].dist = 0;
            queue.Enqueue(begin);
            while (queue.Count != 0)
            {
                string currWord = queue.Dequeue();
                foreach (Vertex next in wordGraph[currWord].edges)
                {
                    if (!visited[next.word])
                    {
                        next.dist = wordGraph[currWord].dist + 1;
                        queue.Enqueue(next.word);
                        visited[next.word] = true;
                        parent[next.word] = currWord;
                    }
                }
            }

            if (!parent.ContainsKey(target))
                return 0;
            string tmpWord = target;
            int count = 0;
            while(parent[tmpWord] != tmpWord)
            {
                tmpWord = parent[tmpWord];
                count++;
            }

            return count;
        }
    }

}
```