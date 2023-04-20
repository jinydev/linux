---
layout:home
---

# simminjeong Report

# Linux Ubuntu에서 패스워드 복잡도 설정

### - 우분투는 리눅스 기반의 운영 체제로, 보안적인 측면에서 매우 안전한 운영 체제.


### - 패스워드의 복잡성을 강화하기 위한 조건
  1. 최소한 8자 이상의 길이
  2. 대문자와 소문자, 숫자, 특수문자 중 3가지 이상을 조합하여 구성
  3. 이전에 사용한 패스워드와 다른 새로운 패스워드로 설정

### - 우분투는 패스워드 정책을 구성할 수 있는 기능을 제공하여 시스템 관리자가 전체 시스템에서 일관된 패스워드 정책을 적용가능
### - 패스워드 복잡성을 강화하여 시스템 보안을 강화 가능
<br>
<br>

## 복잡성 설정 변수 설정
`* 각 변수에 대한 설명 / 각 항목에서 -1 값은 반드시 해당하는 문자를 포함시켜야 함.  

|권장 값| 기능   |   설명    |
|---|---|---|
|lcredit = -1|최소 소문자 요구|최소 소문자 1자 이상 요구|
|ucredit = -1|최소 대문자 요구|최소 대문자 1자 이상 요구|
|dcredit = -1|최소 숫자 요구|최소 숫자 1자 이상 요구|
|ocredit = -1|최소 특수문자 요구|최소 특수문자 1자 이상 요구|
|minlen = 8|최소 패스워드 길이 설정|최소 8자리 이상 설정|
|difok=N|기존 패스워드와 비교하는 정도|기본값 10(10%)|
|retry|입력 실패시 재시도 횟수|패스워드 입력 실패시 재시도 횟수|

<br>

## 리눅스 우분투 패스워드 정책 구성
### 1. 패스워드 복잡성 설정
- `sudo vi /etc/pam.d/common-password` 명령어를 사용하여 파일을 염
- 파일 내에서 다음 줄을 찾아서, 비활성화된 "password requisite pam_pwquality.so" 라인의 주석을 해제하고 다음과 같이 수정

    ```
    password requisite pam_pwquality.so retry=3 minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=3
    ```
    (패스워드 길이 최소 8자, 대문자 1개 , 소문자 1개, 숫자 1개, 특수문자 1개 이상. 패스워드 입력 실패 시 재시도 횟수 3회)

### 2. 패스워드 변경 주기 설정
- `sudo vi /etc/login.defs` 명령어을 사용하여 파일을 염
- 파일 내에서 "PASS_MAX_DAYS" 값을 원하는 변경 주기(예: 90)로 수정

### 3. 패스워드 기억할 횟수 설정
- `sudo vi /etc/pam.d/common-password` 명령어를 사용하여 파일을 염
- 파일 내에서 "password requisite pam_pwquality.so" 라인 아래에 다음 줄을 추가
    ```
    password requisite pam_pwhistory.so use_authtok remember=5 enforce_for_root
    ```
     "remember"는 이전에 사용된 패스워드 재사용 못하도록 설정(5개까지)


### 아래와 같은 명령어를 실행하여 설정한 패스워드 정책을 적용
```
sudo pwconv
```