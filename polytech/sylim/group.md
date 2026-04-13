---
layout: home
---

# 리눅스 권한 관리 모델: 그룹(Group) 제어 통제
<hr/>

리눅스는 완벽한 다중 사용자(Multi User) 운영체제로 설계되었기 때문에 보안이 생명입니다. 하나의 중요 시스템 파일이 있을 때, 이 파일에 접근할 수 있는 권한을 크게 3단계 계층 **1. 소유자(User) 2. 그룹(Group) 3. 나머지 타인(Others)**으로 분리하여 관리합니다. 특정 멤버들(Group)에게만 권한을 일괄 부여하기 위해 사용하는 그룹 관리 핵심 명령어를 숙지해야 합니다.

## 1. 그룹 조회 명령어
```bash
# 내가 현재 어느 그룹들에 소속되어 있는지 출력
groups      

# 특정 사용자(jane)가 어떤 그룹에 소속되어 있는지 출력
groups jane  
```

## 2. 그룹 생성, 수정, 삭제(C/U/D) 명령어
보안과 시스템 영역을 건드리는 작업이므로 모두 관리자(root/sudo) 권한이 필수적입니다.
```bash
# 새로운 빈 그룹 생성 (GID는 시스템이 자동 부여)
sudo groupadd devs

# GID를 3333이라는 고유 숫자로 지정하며 그룹 생성
sudo groupadd --gid 3333 devops

# 그룹의 이름을 A에서 B로 변경
sudo groupmod --new-name new_devs devs

# 그룹을 완전히 삭제 파기함
# 단, 특정 사용자의 '주(Primary) 그룹'으로 지정된 뼈대 그룹이라면 삭제가 불가능(거부)됨
sudo groupdel new_devs
```

## 3. 그룹 비밀번호 및 멤버 배정 관리 (`gpasswd`)
그룹 관리에 있어 현업에서 가장 빈번하게 쓰이는 명령어입니다.

```bash
# 그룹 자체에 비밀번호를 잠금 설정함
sudo gpasswd devs

# 시스템 관리자가 평사원 'john'을 'devs' 그룹의 '서브 관리자'로 임명함 (권한 위임)
sudo gpasswd -A john devs

# 그룹에 특정 팀원(member1)을 새로 가입(add) 시킴
sudo gpasswd -a member1 devs

# 그룹에서 특정 팀원(member1)을 강제 탈퇴(delete) 시킴
sudo gpasswd -d member1 devs
```
> ※ 그룹 권한은 내부적으로 `/etc/group` (목록)과 `/etc/gshadow` (비밀번호 암호화) 파일에 저장되어 관리됩니다.

## 4. `usermod`를 활용한 그룹 재배정
`gpasswd`가 'A그룹에 멤버들을 구겨 넣는' 방식이라면, `usermod`는 'A라는 유저의 정보 자체를 수정해서 서브 그룹 뱃지를 달아주는' 방향으로 동작합니다. 같은 효과를 냅니다.
```bash
# jane이라는 사용자에게 기존 소속들은 건드리지 않고(-a) devs 그룹 뱃지(-G)를 추가함
sudo usermod -a -G devs jane
```
> ※ 주의: `-a` (append) 옵션을 빼먹고 대문자 `-G`만 쓸 경우, 기존에 가입된 소속 동아리(그룹)에서 모두 튕겨나가고 오직 명시한 한 그룹에만 단독 소속되는 대참사가 터질 수 있습니다.

## 5. 터미널 내 일시적 주 그룹 전환 (`newgrp`)
유저가 기본(Primary) 그룹이 아닌 두 번째, 세 번째 소속 그룹의 자격으로 파일 권한 시스템 명령을 내리고 싶을 때 사용합니다.
```bash
newgrp devs
```
이를 입력할 시 현재 검은색 쉘 터미널 세션의 주 그룹 자격표가 `devs`로 잠시 바뀝니다. 해당 창을 `exit`으로 닫거나 로그아웃을 하면 원상복구됩니다.
