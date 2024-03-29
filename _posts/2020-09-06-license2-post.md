---
title: "[정보처리기사] 20200822 9-20번 요점 정리"
date: 2020-09-06 23:15:28 -0400
categories: 정보처리기사
classes: wide
---

## UI 상세 설계
- Tree, flow chart
- 시퀀스, 분기 조건, 루프 명시
- 규칙
    - 주요 키 위치와 기능
    - 공통단위 태스크 흐름
    - 공통 UI 요소
    - 기본 스크린 레이아웃
    - 기본 인터렉션
    - 케이스 문서
- UI 시나리오 문서 요건
    - 완전성 : 누락 없음
    - 일관성 : 유지
    - 이해성(직관성) : 누구나 쉽게 이해가능
    - 가독성 : 줄간격, 들여 쓰기, 시각적 효과
    - 수정 용이성
    - 추적 용이성

## 코드의 주요 기능

- 식별(데이터 간 성격), 분류 (특정 기준 그룹화), 배열 (의미를 부여 나열)

## 코드의 종류

- 순차 코드 : 일정 기준에 따라 일련 번호 부여
- 블록 코드 : 공통성 있는 것끼리 묶기
- 10진 코드 : 10진 분할하여 그룹 나누고 세부그룹은 거기서 또 10진 분할
- 그룹 분류 코드 : 대분류 - 중분류 - 소분류
- 연상 코드 : 명칭, 약어 사용
- 표의 숫자코드 : 물리적 수치를 코드에 적용
- 합성 코드 : 2개 이상의 코드 섞기

## 협약에 의한 설계 

- 클래스에 대한 여러 가정 공유, 명세하여 선행, 결과 불변

## 알면 좋을 용어들

- 트랜지션 : 전환, 장면 전환
- 클래스 : 공통된 연산을 갖는 객체 집합, 객체 지향 상속 단위
- 시퀀스 : 상호작용, 메시지
- 서브루틴 : 모듈화로 반복되는 부분
- 컴포넌트 : 독립적인 언어 또는 기능을 수행하는 실행 코드 기반 작성 모듈

## 디자인 패턴 구성 요소

- 문제 및 배경
- 사례
- 샘플 코드

## 객체 지향 설계 원칙 (SOLID 원칙)

- SRP : 단일 책임 원칙 (부품은 하나의 기능)
- OCP : 개방 폐쇄 원칙 (코드를 변경하지 않고, 기능 추가 설계 가능)
- LSP : 리스코프 치환 원칙 (자식은 부모가 할줄 아는것 포함)
- DIP : 의존 역전 원칙 (의존 관계)
- ISP : 인터페이스 분리 원칙 (여러개의 인터페이스)

## 자료 흐름도 구성요소

- 처리, 자료 흐름, 자료 저장, 단말

## CASE (Computer -Aided SW Engneering)

- 컴퓨터 SW 개발 과정 일부 또는 전체 자동화
- 표준화된 개발 환경 구축 및 문서 자동화 기능 제공
- 작업 과정 및 데이터 공유를 통해 작업자간 커뮤니케이션 증대

## 인터페이스 요구사항 검증 단계

1. 요구 사항 검토 계획 수립
2. 요구 사항 검토 및 오류 수정
3. 요구사항 베이스라인 설정

## 인터페이스 요구사항 검증 방법

1. 검토
    - 동료 검토 : 동료 및 이해 관계자
    - 워크 스루 : 짧게 , 명세서 미리 배포
    - 인스펙션 : 타 검토관들이 확인
2. 프로토타이핑
3. 테스트 설계
4. CASE 도구 활용 : 일관성 분석, 추적 ,관리


