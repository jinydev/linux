---
layout: home
title: "보안 계정 통제: PAM 패스워드 복잡도 강제"
---

# 규제와 통제의 보안 시스템: PAM (Pluggable Authentication Modules)

리눅스 서버에 사원들이 계정을 생성할 때 비밀번호를 `1234` 나 `password` 처럼 제멋대로 지정하여 회사 망 전체가 해킹당하는 참사를 막기 위한 강제 조율 매커니즘입니다. 
PAM은 사용자가 리눅스에 로그인하거나 패스워드를 바꿀 때 가로채서, **"대문자 1자 이상, 특수문자 1자 이상, 길이 8자리 이상"** 등의 융통성 없는 보안 컴플라이언스를 기계적으로 강제 집행하는 심문관 데몬입니다.

---

## 1. 패스워드 복잡성 심문관 설정 `/etc/pam.d/common-password`

기본 데비안/우분투 진영 통제 파일로, 이 파일에 파라미터를 먹이면 사원이 비밀번호를 바꿀 때마다 검열 필터를 거치게 됩니다.
`sudo vi /etc/pam.d/common-password` 를 열고 아래의 마법 코드를 추가합니다.

```bash
# pam_pwquality.so 심문관 모듈에 검증 파라미터(Parameter)를 주입
password requisite pam_pwquality.so retry=3 minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=3
```

### [실무 보안 컴플라이언스 인자 해독]
* **`retry=3`**: 비밀번호 입력(수정) 실패를 최대 3번까지만 허용합니다.
* **`minlen=8`**: 아무리 발악해도 무조건 8글자 텍스트는 넘어야 합니다.
* **`ucredit=-1` / `lcredit=-1`**: 대문자(Upper) 1개 이상, 소문자(Lower) 1개 이상을 무조건 포함(-1) 강제합니다.
* **`dcredit=-1` / `ocredit=-1`**: 숫자(Digit) 1개 이상, 특수기호(Other) 1개 이상 구성을 강제합니다.
* **`difok=3`**: 이전 비밀번호와 철자가 똑같은 글자가 3개 이상 중복되면 반려시킵니다 (돌려막기 금지).

---

## 2. 망각 방어: 패스워드 교체 주기 강제 `/etc/login.defs`

한번 만든 비밀번호를 10년 넘게 우려먹는 악습을 철폐하기 위한 운영 모듈의 유통기한 설정 파일입니다.

```bash
# /etc/login.defs 파일 강제 수정 내역
PASS_MAX_DAYS   90      # 비밀번호를 변경하지 않고 버틸 수 있는 최대 기간 (90일 지나면 강제 Lock)
PASS_MIN_DAYS   1       # 비밀번호를 바꾼 직후 또 바꾸려면 최소 1일은 숨을 참아야 함
PASS_WARN_AGE   7       # 비밀번호 만료 7일 전부터 로그인할 때마다 빨리 바꾸라고 경고 출력
```

## 3. 돌려막기 방어: 패스워드 히스토리 백업 `/etc/pam.d/common-password`

사원들이 90일이 지나 비밀번호 변경 창이 뜨면, 원래 쓰던 원래 암호 뒤에 숫자 하나만 붙이거나 아예 과거 비밀번호를 돌려쓰는 꼼수를 차단합니다. 

```bash
# pwhistory.so (과거 이력 추적) 로직 추가
password requisite pam_pwhistory.so use_authtok remember=5 enforce_for_root
```
* **`remember=5`**: 이 계정의 과거 패스워드 변천사 5건을 DB에 몰래 암호화해 박제해 두고, 새 비밀번호가 과거 5대장 안에 있는 비밀번호와 매치되면 "예전 비번 재활용 금지!" 라며 거부합니다.
* 모든 강제 세팅이 끝나면 시스템을 새로고침하는 `sudo pwconv` 렌더링으로 뼈대에 적용합니다.