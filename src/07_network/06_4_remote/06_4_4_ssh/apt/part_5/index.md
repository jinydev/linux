---
layout: home
title: "03.root 접속 허용"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 03.root 접속 허용

## 03.root 접속 허용

기본적으로 리눅스 배포폰은 root 접속을 허용하지 않습니다. 보안상 root 접속을 허용하는 것은 좋지 않다. 하지만, 내부 개발용으로 사용시 편의를 의해서 root를 허용하고자 할때 다음과 같이 하면 된다.

### 03.1 설정파일 수정

/etc/ssh/sshd_config 파일을 수정합니다. vi를 통하여 수정합니다.

```
$ sudo vi /etc/ssh/sshd_config
```

vi 에디터가 실행됩니다. `esc+i`를 선택하여 입력 모드로 전환합니다. 그리고, 다음과 같은 라인을 찾아서 수정합니다.

```
#PermitRootLogin prohibit-password
PermitRootLogin yes
```

설정부분에서 PermitRootLogin 주석을 제거해 주거나, 아래에 다시 작성을 합니다. prohibit-password 대신에 yes를 적어 줍니다.

`esc+:wq`를 입력하여 저장후 종료합니다.

### 03.2 ssh 재시작

ssh 서버를 재시작 합니다.

```
$ sudo systemctl restart sshd

```

### 03.3 루트 암호 변경하기

기본적으로 루트의 암호는 Ubuntu 20.04에 설정되어 있지 않으며 Permission denied라는 오류 메시지가 나타납니다. 

루트 사용자로 SSH 로그인을 시도하면 다시 시도하십시오. 이러한 이유로 우리는 루트의 암호를 설정해야합니다. 프롬프트가 표시되면 현재 사용자 비밀번호와 새 루트 비밀번호를 입력하십시오.

```
$ sudo passwd
[sudo] password for linuxconfig: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
```

### 03.4 root로 putty 접속해 보기

putty를 다시 실행합니다. 로그인 창에서 아이디를 root로 입력합니다.

<!-- Broken Image Removed: ../../../img/image-20210103122209602.png -->

루트로 SSH가 접속된 것을 확인할 수 있습니다.

---

[⬅️ 이전: SSH](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: 원격터미널 접속 ➡️](../terminal/)


---

[⬅️ 이전](../)
