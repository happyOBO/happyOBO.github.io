---
title: "[정보처리기사] 정보시스템구축관리-2"
date: 2020-09-16 23:15:28 -0400
categories: 정보처리기사
---

### 복구 통제

- 부적절한 상황/ 사건으로인해 발생한 피해 극복
- 데이터 백업, 수작업 대체 처리

### 시스로그

- 기본 적인 시스템 로그 파일

### 스택 가드

- 메모리 상, 프로그램 복귀주소 변수 특정 값 저장
- 값 변경 시, 스택 오버플로로 가정하여 프로그램을 중단 시킨다.

### 백도어 탐지 방법

- 현재 동작중인 프로세스 및 열린 포트 확인
- SetUID 파일 검사
- 백도어 탐지 툴 사용
- 무결성 검사
- 로그 분석

### CMM / CMMI

- 능력 성숙도 통합 모델
- 초기 -> 관리 -> 정의 -> 정량적 관리 -> 최적화

### trace 

- 한 스텝씩 추적

### tripwire

- 시스템의 특정 파일 변화 모니터링 및 알람, 보안 무결성 도구

### udpdump

- UDP 데이터를 DUMP

### cron

- 시간 기반 잡 스케줄러

### 네트워크 관련 신기술

- IoT : 사물 기반 인터넷
- M2M(Machine to Machine) : 사물 통신, 부호 분할 다중 접근(CDMA), 무선통신
- 모바일 컴퓨팅 : 휴대기기, 무선 고속 대용량
- 클라우드 컴퓨팅 : 중앙 컴퓨터
- 그리드 컴퓨팅 : 여러 컴퓨터를 하나로 묶어서 분산 처리
- 모바일 클라우드 컴퓨팅 : 소비자와 소비자 파트너가 모바일 기기로 컴퓨팅 인프라 구성
- 인터 클라우드 컴퓨팅 : 다른 클라우드들 연동
    - 대등 접속 : 직접 연계
    - 연합 : 사용 요구량에 따른 동적 할당
    - 중개 : 중개 서비스 제공
- 메시 네트워크 : 대규모 디바이스 네트워크 생성, 라우터를 무선 망처럼 구성
- 와이선 : 저전력 장거리 무선 통신
- NDN (Named Data Net) : 콘텐츠 정보, 라이터 기능 으로 데이터 전송
- NGN (Next Generation Net) : 차세대 이동 통신 , 유선망을 패킷으로 압축
- SDN (Sw Definde Net) : 소프트웨어들로 네트워크를 가상화
- NFC : 근거리 무선 통신
- UWB : 근거리 엄청많은 데이터 통신
- 피코넷 : 독립된 송신 장치로 통신망 형성
- WBAN : 웨어러블
- GIS : 지리정보 시스템
- USN : 각종 센서, 유비쿼터스
- SON : 주변 상황에 맞춰서 자동으로 망 구성
- 애드 혹 네트워크 : 재난 현장같은 상황에서 모바일로 망구성
- 네트워크 슬라이싱 : 5G 와 관련
- BLE : 블루투스

### 하둡

- 빅데이터 처리 분산 응용 프로그램

### 비컨

- 근거리에 있는 스마트 기기 자동인식(블루투스)

### 포스퀘어

- 위치기반 소셜 네트워크 서비스

### 맴리스터

- 기억효과를 나타내는 양방향 디바이스

### 테일러링

- 프로젝트의 특성에 따라 각 산출물 적용 여부, 변경 여부 체크
- 절차
    - 표로젝트 특성 파악
    - 베이스 라인 방법론 산정
    - 테일러링 수행
    - 테일러링 프로세스 교육
- 기준 
    - 내부적 : 목표 환경, 요구사항, 프로젝트 규모, 보유 기술
    - 외부적 : 법적 제약 사항, 표준 품질 기준
- 프레임 워크
    - ISO/IEC 12207
    - CMMI
    - SPICE