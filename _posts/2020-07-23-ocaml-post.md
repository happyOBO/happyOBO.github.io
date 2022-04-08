---
title: "[OCaml] 리스트 형식대로 리스트 출력하기"
date: 2020-07-23 15:44:28 -0400
categories: OCaml
---

### 리스트 형식대로 리스트 출력하기

```ocaml
let print_list f lst =
  let rec print_elements = function
    | [] -> ()
    | h::t -> f h; print_string " ; "; print_elements t
  in
  (print_string " [ ";
  print_elements lst;
  print_string " ] "
)
```

### 리스트 형식대로 문자열 생성

```ocaml
let to_string_list lst =
  let rec print_elements = function
    | [] -> ""
    | h::t -> h ^ " ; " ^ (print_elements t)
  in
  ("[ " ^ print_elements lst ^ " ]" )
```