---
layout: home
---

# 셀의 개념

리눅스를 조작하기 하기 위한 연결통로



## Shell의 역할

`Shell`의 영어단어 의미는 껍데기, 조개껍질 등을 의미합니다. 

![image-20230326161358434](./img/image-20230326161358434.png)



즉, 쉘은 `사용자 명령어 해석기`로 사용자가 `프롬프트`에 입력한 명령을 `해석`하여 운영체제에 `전달`하는 역할을 합니다.

> 명령프롬프트란? 운영체제에 명령을 입력할 수 있는 콘솔창을 의미합니다. 
>
> ```bash
> hojin@hojin3:~$
> ```
>
> 위와 같이 명령을 입력할 수 있는 콘솔 또는 터미널 창을 말합니다.



![image-20230326161456881](./img/image-20230326161456881.png)



### 쉘의 명령문 처리

명령 프롬프트에서 셸의 명령문 작성 형식은 다음과 같습니다.

```
$ 명령 [옵션…] [인자…]
```

명령문 작성에 대한  예를 들어 확인해 봅시다.

```bash
$ ls -l
$ rm -rf /mydir
$ find . / -name "*.conf"
```

### 셀 명령문 실습

예를 들어서 쉘의 역할에 대해서 보다 자세히 알아 보도록 하겠습니다. 

```bash
hojin@hojin3:~$ date
Sun Mar 26 16:10:03 KST 2023
hojin@hojin3:~$
```

명령창에서 `date` 명령을 입력해 보니다. 셀은 `date` 명령을 운영체제에 전달하고, 운영체제는 해당 명령을 실행한 `결과를 출력`합니다. 그리고, 다음 명령을 입력받을 수 있는 상태로 대기합니다.



## Shell의 종류

리눅스는 유닉스 운영체제를 모방하여 개발된 오픈소스 운영체제 입니다. 리눅스에서도 유닉스와 같이 다양한 종류의 셀을 사용할 수 있습니다.



유닉스에서 가장 인기 있는 3가지 셀(sh, csh,ksh)과  리눅스에서 가장 인기있는 bash 셀에 대해서 알아 봅니다.

### Bourne Shell(sh)
AT&T 벨 연구소의 스티븐 본(Stephen Bourne)이 개발한 쉘을 말합니다. 
* 최초의 유닉스의 Bourne shell과 호환되는 쉘

> 정리과제: 



### C Shell(csh, tcsh)
Bill Joy가 C언어의 기수을 넣어서 만든 Shell을 말합니다.  
C언어의 문벅을 적용하였으며, History, aliases, Job controll, vi command 기능등을 포함시켜 개량하였습니다.
* BSD 계열 유닉스에서 선호하는 쉘
> 정리과제:



### Korn Shell(ksh)
Daid Korn이 AT&T에서 기존 bourne shell과 C Shell의 기능을 결합한 쉘을 만들어 배포하였습니다.
* 유닉스 V계열 사용자들이 선호하는 셀
> 정리과제: ksh



### Bourne-Again Shell(bash)

GNU 프로젝트로 만들어진 쉘입니다. csh, ksh이 가진 기능들을 포함하면서 기존의 bourne shell과 호환성을 많이 높인 shell로 리눅스의 기본 셀로 사용되어 지고 있습니다. 또한 Mac OS와 윈도우에서도 사용이 가능합니다.

> 정리과제 : GNU란 어떤 곳인가요?
>
> 정리과제: bash



#### bash의 특징

* 에일리어스(alias, 명령 단축) 기능

* 히스토리 기능( ↑ 또는 ↓ )

* 연산 기능

* Job Control 기능

* 자동 이름 완성 기능( Tab )

* 프롬프트 제어 기능

* 명령 편집 기능





> 쉘 은 어디에 존재하나요?
>
> 우분투의 경우 sh와 bash 쉘이 같이 설치가 되어 있습니다. 셀은 기본적으로 `/bin` 디렉터리에 존재합니다.
>
> ```bash
> hojin@hojin3:~$ ls /bin/sh
> /bin/sh
> hojin@hojin3:~$ ls /bin/bash
> /bin/bash
> hojin@hojin3:~$
> ```





## 기본 Shell

운영체제에 설치되어 있는 셀의 종류와 사용하고 있는 셀을 확인/변경해 보도록 합니다. 



## 사용 가능한 쉘 리스트 확인하기

현재 시스템에서 사용이 가능한 셀의 종류에 대해서 확인할 수 있습니다.



```bash
cat /etc/shells
```



실습을 통하여 결과를 확인해 봅시다.

```bash
hojin@hojin3:~$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/sh
/bin/dash
/usr/bin/dash
/usr/bin/tmux
/usr/bin/screen
```

시스템에는 다양한 종류의 셀이 설치가 되어 있습니다. 셀은 기본적으로 `/bin` 디렉터리에 설치가 되어 있습니다.



### 현재의 사용중인 쉘 확인

시스템에는 다양한 종류의 셀이 설치되어 있습니다. 그러면, 현재 자신이 사용하고 있는 쉘은 무엇일까요?  



다음과 명령을 통하여 현재 사용중인 셀을 확인할 수 있습니다.

```bash
hojin@hojin3:~$ echo $SHELL
/bin/bash
```



### 로그인 셀

리눅스는 다중 사용자 운영체제 입니다. 등록된 사용자 마다 서로 다른 셀을 선택하여 사용 가능합니다. 사용자별 등록된 셀을 `로그인 셀`이라고 합니다.



등록된 로그인 쉘의 종류는 다음과 같이 확인할 수 있습니다.

```bash
cat /etc/passwd
```



실습을 통하여 내용을 확인해 봅시다.

```bash
hojin@hojin3:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
중간생략...
hojin:x:1000:1000:,,,:/home/hojin:/bin/bash
```

각줄의 마지막 항목이 등록된 `로그인 셀` 입니다.



### 셀 변경

사용중인 쉘을 변경할 수 있습니다. 쉘을 변경하기 위해서는 root 권환으로 명령을 실행해 주어야 합니다.



```bash
$ sudo chsh 사용자
```

> 주의: 사용자를 생략하게 되면 `root` 사용자의 셀이 변경됩니다.



```bash
hojin@hojin3:~$ sudo chsh hojin
[sudo] password for hojin:
Changing the login shell for hojin
Enter the new value, or press ENTER for the default
        Login Shell [/bin/bash]: /bin/sh
```

