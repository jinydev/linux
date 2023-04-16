---
layout: home
---

# 권환 획득
`su` 명령은 `Super User`의 약자로, 다른 사용자로 전환하여 명령을 실행할 수 있도록 해주는 명령어입니다. 기본적으로 `root` 계정으로 전환하는 명령어이며, 사용자가 지정한 다른 계정으로 전환할 수도 있습니다.

## 권환이 있는 다른 사용자로 로그인 합니다.
`su` 명령은 다른 사용자로 로그인할 수 있습니다.

```bash
$su 사용자
```

## 루트사용자
`su` 명령을 실행하면 기본적으로 `root` 계정으로 로그인하게 됩니다. 따라서 root의 비밀번호가 요구됩니다. 예를 들어, `root` 계정으로 전환하려면 다음과 같이 입력합니다.

```bash
su
```
root 비밀번호를 입력한 후에는, 새로운 쉘 세션에서 root 권한으로 명령을 실행할 수 있습니다.  
또는 다음과 같이 명령을 입력할 수도 있습니다.

```bash
$su -
```

`-` 는 root를 의미합니다. 다음과 같은 명령과 같습니다.

실행결과
```bash
hojin@hojin3:~$ su -
Password:
su: Authentication failure
```

## 루트 사용자 설정
루트로 로그인을 하기 위해서는 먼저 루트 사용자의 비밀번호를 설정해 주어야 합니다.
```bash
$sudo passwd root
```

다시 루트로 로그인을 해봅니다.

```bash
su root
```

실행결과
```
hojin@hojin3:~$ su -
Password:
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.90.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This message is shown once a day. To disable it please create the
/root/.hushlogin file.
root@hojin3:~#
```

## 사용 제한
`su` 명령은 보안상의 이유로 가능한 사용하지 않는 것이 좋습니다. 대신 `sudo` 명령어를 사용하여 필요한 명령어만 root 권한으로 실행하는 것이 좋습니다.