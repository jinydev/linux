---
layout home
---

# 비밀번호 명령어 
---

# 리눅스 계정 종류

## **사용자 분류**

- 루트 계정 : 모든 권한을 가진 특별한 사용자
- 시스템 계정 : 리눅스 설치시 기본으로 생성되는 계정
- 사용자 계정 : 실제 리눅스 사용자를 위한 계정
   <br/><br/>

리눅스에서는 사용자를 root(관리자)와 일반사용자로 구분한다.

각각 계정은 흔히 사용하는 ID가 아니라 번호로 부여하는 **UID(User Identity)**로 관리한다.
   <br/><br/>
**root (Super User)계정**은 UID값이 0으로 지정된 관리자계정이다.
여기서는 다른 계정을 생성하거나 권한을 부여하고 비밀번호를 바꿀 수 있다. 즉 모든 권한을 가진 계정이다. 만약 다른계정에 UID값을 0으로 변경한다면 관리자와 마찬가지로 모든 권한을 가질 수 있다.
   <br/><br/>
**일반사용자(Normal user)**는 관리자에게 권한을 부여받아 사용한다.
리눅스에서 파일을 생성 시 소유주의 권한을 가지는데 만약 일반유저라면 root 권한을 가진 파일을 실행하거나 볼 수 없다. 따라서 root가 파일의 권한을 부여해야만 일반관리자가 해당 파일을 열어볼 수 있다.
   <br/><br/>
root와 일반사용자를 제외한 계정으로는 **시스템계정(서비스계정)**이 있다.
필요에 의해 자동으로 생성되는 시스템계정은 bin, daemon, adm, lp,sync, shutdown, halt, mail 등 여러가지가 있으며 일반적으로 로그인은 불가능하다.

![Untitled](https://user-images.githubusercontent.com/127702320/233010129-4fa89929-1317-4a25-ad19-942707926486.png)

![Untitled (1)](https://user-images.githubusercontent.com/127702320/233010123-49a59d56-cd6f-4929-a34f-8fb7415748a0.png)

## 계정 패스워드 명령어

### Q. 패스워드 명령어를 알아야 하는 이유 ?

> 리눅스 시스템에서는 여러 사용자가 동시에 작업하고, 각각의 사용자는 자신의 계정을 가지고 있다. 이러한 사용자 계정은 보안 상 이유로 각각 고유한 비밀번호로 보호되어야 한다. 따라서, 사용자 비밀번호를 관리하기 위한 명령어는 매우 중요하다.   
또한, 사용자 비밀번호 명령어는 시스템 보안 관련 법규 준수를 위해서도 매우 중요합니다. 예를 들어, PCI-DSS (Payment Card Industry Data Security Standard)와 같은 기준을 준수하기 위해서는, 사용자 비밀번호를 규칙에 맞게 설정하고 주기적으로 변경하는 등의 조치가 필요하다. 
> 

⇒ 리눅스 시스템의 보안을 유지하고, 법적인 요구 사항을 준수하기 위함 
   <br/><br/>
### **패스워드 설정 (passwd)**

`passwd`  명령은 사용자의 비밀번호를 변경

```bash
$ passwd [option][username] 

Changing password for user username. 
New password: Retype new password:
passwd: all authentication tokens updated successfully
```
   <br/><br/>
### passwd 옵션

|  | 설 명 |
| --- | --- |
| -d, --delete | 패스워드 삭제. 비밀번호없이 로그인 가능 |
| -e, --expire | 사용자의 패스워드를 만료 |
| -i, --inactive | 패스워드 만료후 비활성화전 유예기간 일 지정 |
| -l, --lock | 사용자 패스워드에 락 걸어 로그인 막음 |
| -u, --unlock | 락을 걸었던 패스워드를 다시 해제 |
| -w, --warndays | 패스워드 만료전 경고날짜 지정 |
| -x, --maxdays | 최대사용기간 설정(만료 기간 설정) |
| -n, --mindays | 비밀번호 변경할수 있을때까지 유지해야할 일수 설정(변경 간격 설정) |
| -q, --quiet | 화면 출력없이 명령을 수행 |
| -S, --status | 사용자의 로그임명, 패스워드 상태, 설정여부, 마지막으로 변경한 날짜, 패스워드 변경까지 남은 기간 등 다양한 정보 출력 |

```bash
# 사용자 패스워드 설정
$ sudo passwd testuser

# 현재사용자 패스워드 변경
$ passwd

# 지정한 사용자 패드워드 만료
$ sudo passwd -e testuser

# 지정한 사용자의 패스워드 상태를 출력
$ sudo passwd -S testuser

# 지정한 사용자 패스워드 락
$ sudo passwd -l testuser

# 지정한 사용자 패스워드 삭제
$ sudo passwd -d testuser

# 패스워드 변경후 7일간 변경 불가능, 365일간 사용할수 있고 5일전부터 패스워드 변경 경고. 만료후 10일 유예기간
$ sudo passwd -n 7 -x 365 -w 5 -i 10 testuser
```
   <br/><br/>
### **패스워드 유효기간 관리 (chage)**

`change` 를 통해 사용자의 비밀번호를 주기적으로 변경하도록 설정


```bash
$ chage [options] usernameCopy
```

| 옵 션 | 설 명 |
| --- | --- |
| -d,--lastday | 패스워드를 변경해야 할 날짜수 지정 |
| -E,--expiredate | 계정이 만료되는 날 설정 |
| -I,--inactive | 계정만료후 패스워드가 비활성화될때까지 유예기간을 설정 |
| -l,--list | 계정의 매스워드 만료 정보 보여줌 |
| -m,--mindays | 패스워드 변경할 때 최소 날짜를 지정 |
| -M,--maxdays | 패스워드 변경할 때 최대날짜 지정 |
| -W,--warndays | 패스워드 만료에 대한 경고 메시지를 보여줄 날짜를 지정 |

```bash
# 만료정보 출력
$ sudo chage -l test

# test 계정의 패스워드 최소 사용날짜 7일, 최대 사용날짜 365일 5일전부터 경고메시지. 만료후 3일 유예기간
$ sudo chage -m 7 -M 365 -W 5 -I 3 test

# test 계정의 만료일 지정.
$ sudo chage -E 2019-12-24 test

# test계정의 패스워드 변경일 10000 설정
$ sudo chage -d 10000 test
```

## MAN(manual)

로컬 시스템에서 여러 참고 문서들을 이용하여 특정 명령이나 자원들의 메뉴얼을 출력하는 영역으로 유닉스에서는 총 8개의 영역으로 되어있으나 리눅스 커널 부분이 추가되어 총 9개의 영역으로 구성되어있다.

### 사용법

```
$ man [options] [section] command
```

- [SPACE] : 한 페이지 밑으로 내려간다
- [ENTER] : 한 줄 밑으로 내려간다.
- [b] : 전 페이지로 올라간다.
- [q] : man 명령을 종료한다.

### 주요 옵션

- k 키워드 : 해당 키워드로 발견되는 모든 매뉴얼의 내용을 검색하여 보여준다.
- f 키워드 : 해당 키워드에 대한 완벽히 일치되는 매뉴얼 페이지에 대한 정보를 보여준다.
- w 키워드 : man 명령 실행 시에 호출되는 '메뉴얼 페이지' 파일의 위치를 보여준다.(--path)
- s, -S : 특정 section을 지정할 때 사용한다. (--sections=섹션번호)

### 사용예

```bash
$ man ls
ls 명령어의 메뉴얼 페이지를 보여준다. 기본적으로 영역 값을 지정하지 않으면 첫 번째 영역의 페이지 정보를 출력한다.

$ man man
man 명령어의 매뉴얼 페이지를 보여준다.

$ man -k passwd
passwd라는 키워드가 포함된 메뉴얼 페이지를 찾아서 출력한다.

$ man -f passwd
passwd라는 키워드와 일치하는 메뉴얼 페이지의 목록 정보를 출력한다.

$ man 5 passwd
다섯 번째 영역에 있는 passwd의 메뉴얼 페이지를 출력한다.

$ man -w mkdir
man mkdir 실행 시에 출력되는 '메뉴얼 페이지' 파일의 경로를 출력한다.
```