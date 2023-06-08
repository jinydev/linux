# 커맨드 라인 분석

## 흐름 제어: While 루프와 Until 루프

이번 장은 루핑(looping)이라는 프로그램 개념에 대해 알아볼 것!

- 이는 프로그램의 일부를 반복적으로 실행할 때 사용
- 쉘은 루프를 수행하기 위해 세 개의 합성 명령어를 제공
- 그 중 2가지에 대해 학습할 것!

## 루프 돌기(반복)

- 일상 생활은 반복적인 행동으로 이뤄짐
- 이러한 행동을 의사코드로 표현하면 다음과 같은 단계로 구성

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled.png)

## while

- bash는 앞의 방식과 유사하게 표현 가능
- bash 스크립트로 만든 예시

### 코드

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%201.png)

- count에 1을 할당
- count가 5보다 작거나 같은 경우 do 실행
- count를 출력
- count에 1 추가
- done 다 끝났을 경우 Finished 출력

### 결과

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%202.png)

### while 명령어의 문법

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%203.png)

## 루프 탈출

- bash는 두 개의 내장 명령어 제공
- 루프 내에서 프로그램의 흐름을 제어하기 위함
- **break와 continue**

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%204.png)

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%205.png)

- while문의 무한 루프
- 메뉴 0이 선택되면 break 명령어로 루프를 종료한다.
- continue 명령어를 사 용함으로써 선택 메뉴가 확인된 경우 불팔요해진 코드는 건너뛴다.

- **uptime**
리눅스 시스템이 실행되고 난 후 부터 지금까지의 시간과 시스템에 로그인 된 사용자 수 그리고 시스템 부하율을 표시하는 명령어
- ***du***
disk usage의 약자로 디렉토리(폴더)와 파일의 용량을 출력해주는 명령어

## until

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%206.png)

- **조건문이 참이 될때까지(조건이 거짓인 동안 실행)**
- until 명령어는 0이 아닌 종료 상태를 만났을 때 루프를 종료하는 대신에 계속 수행되는 것만 제외하고 while과 동일
- until 루프는 종료 상태 값으로 0을 받을 때까지 계속됨

![Untitled](%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20ff14ec5d3f614df4b44b1a86fba56d97/Untitled%207.png)

- count가 5보다 클때까지 반복
    
    **→ 참이 될때까지 반복**