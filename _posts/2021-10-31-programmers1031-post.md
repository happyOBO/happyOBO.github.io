---
title: "[알고리즘] 스킬트리"
date: 2021-10-31 10:15:28 -0400
categories: 알고리즘 구현 C#
---



### 문제 설명

- 선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.
- 예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.
- 위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

- 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

### 제한 조건

- 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
- 스킬 순서와 스킬트리는 문자열로 표기합니다.
- 예를 들어, C → B → D 라면 "CBD"로 표기합니다
- 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
- skill_trees는 길이 1 이상 20 이하인 배열입니다.
- skill_trees의 원소는 스킬을 나타내는 문자열입니다.
- skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

### 입출력 예

```sh
skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
```

### 접근 방식

- 스킬 순서의 0번째 원소부터 `skill_tree`의 몇번째에 위치한지 체크한다.
- 현재 탐색하고 있는 원소가 이전에 탐색했던 원소보다 `skill_tree`의 앞에 위치하면 불가능한 스킬트리로 생각한다.
- 만약에 `skill_tree`에 스킬 순서의 원소가 있지 않다면 `MAX_VALUE`를 넣어준다.
  - 현재 원소가 `skill_tree`에 있다면 다음 원소가 오면 안되기 때문.

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
            string[] skill_trees = new string[] { "Z", "BCA", "BZ", "CZD" };
            int answer = sol.solution("ABC", skill_trees);
            Console.WriteLine();
        }
        public int solution(string skill, string[] skill_trees)
        {
            int answer = 0;
            foreach(string skill_tree in skill_trees)
            {
                if(findPossibleSkillTree(skill, skill_tree))
                {
                    answer++;
                }
            }
            return answer;
        }

        public bool findPossibleSkillTree(string skill, string skill_tree)
        {
            int recentSkillIdx = int.MinValue;
            foreach(char unit_skill in skill)
            {
                int skillIdx = searchSkillIdx(unit_skill, ref skill_tree);
                if (recentSkillIdx > skillIdx) return false;
                else recentSkillIdx = skillIdx;
            }

            return true;
        }

        public int searchSkillIdx(char unit_skill, ref string skill_tree)
        {
            for(int i = 0; i < skill_tree.Length; i++)
            {
                if (unit_skill.Equals(skill_tree[i])) return i;
            }

            return int.MaxValue;
        }
    }
}

```