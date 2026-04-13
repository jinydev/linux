---
layout: home
title: "VNC 서버 설치"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# VNC 서버 설치

## VNC 서버 설치

VNC를 서버를 실행하기 위해서는 리눅스 운영체제를 데스크탑형으로 선택하여 x-window 를 같이 설치되어 있어야 합니다.

### 화면 공유 설정하기

화면 오른쪽 상단 아이콘을 클릭하여 `Setting`을 선택합니다.

* 설정텝에서 `Sharing`을 선택합니다.

* Sharing 항목을 `켬`으로 변경합니다.

  > 설정을 변경할때 암호를 물어보게 됩니다.

![image-20230329235026872](../../img/image-20230329235026872.png)

### Remote Desktop 활성화

`Remote Desktop`을 선택합니다. 세부 설정창이 실행되면 `켬`으로 변경합니다.

![image-20230330002923765](../../img/image-20230330002923765.png)

`remote Desktop`이 `on`상태로 변경되었습니다.

![image-20230329235226217](../../img/image-20230329235226217.png)

### 추가설치

```
sudo apt install dconf-editor
```

방화벽 열기, 5900 포트 허용

```
ufw allow 5900/tcp
```

Server의 IP 주소 확인

```
ifconfig
```


---

[⬅️ 이전](../)
