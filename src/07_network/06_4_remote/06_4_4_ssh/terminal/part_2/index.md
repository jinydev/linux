---
layout: home
title: "02.Moba Xterm 사용하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 02.Moba Xterm 사용하기

## 02.Moba Xterm 사용하기

서버 접속 프로그램 MobaXterm을 이용하여 터미널 접속을 합니다.
무료 버젼을 제공하기 때문에 부담없이 사용을 할 수 있습니다.

### 02.1 공식사이트 및 다운로드

MobaXterm 공식사이트로 접속합니다. 사이트 주소는 https://mobaxterm.mobatek.net/ 입니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200628572.png -->

다운로드페이지로 이동을 합니다. https://mobaxterm.mobatek.net/download.html

MobaXterm은 `무료버젼` 과 유료버젼을 같이 제공합니다. 무료 버젼을 선택합니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200806191.png -->

MobaXterm은 직접 컴퓨터에 설치를 하여 사용하는 버젼과, 이동형으로 사용할 수 있는 포터블 버젼을 제공합니다.

원하는 파일을 다운로드 받습니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200922346.png -->

### 02.2 설치하기

> [설치 msi 파일 다운로드 받기](https://download.mobatek.net/2062020111930940/MobaXterm_Installer_v20.6.zip)

다운로드 받은 압축파일을 풀어서 실행을 합니다. 다음 설치 과정으로 넘어가기 위해서 `next`를 클릭합니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200059891.png -->

사용자 라이센스 동의를 선택한 후에 `next`를 클릭합니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200144890.png -->

MobaXterm을 설치할 경로를 선택합니다. 

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200308759.png -->

설치를 진행합니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200343885.png -->

설치를 위해서 잠시 기다립니다. 디바이스를 변경하고자 한다는 경고 화면이 나오면, 허용을 클릭합니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200400394.png -->

설치가 완료되었습니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127200507548.png -->

### 02.3 실행하기

설치한 MobaXterm을 실행합니다. 

처음 실행할때 다음과 같이 방화벽 설정을 요구하면, 이를 허용 합니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127201153786.png -->

다음과 같이 MobaXterm이 실행된 것을 확인 할 수 있습니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127201330307.png -->

`SSH` 를 이용하여 원격 서버에 `터미널 접속`을 해보도록 합니다. 

새로운 `세션(session)`을 하나 생성해 봅니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127201457952.png -->

접속 유형을 SSH로 선택 합니다. 

Remote host에 접속하고자 하는 서버의 주소를 입력합니다. Sepecify  username 에 아이디를 입력합니다. 

접속 포트를 선택합니다. 기본적으로 ssh는 22번 포트를 사용합니다. 만일 다른 포트로 변경하였다면, 숫자를 수정해 주세요.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127201828591.png -->

OK를 선택합니다. 다음과 같이 터미널 접속이 되는 것을 확인할 수 있습니다.

비밀 번호만 입력하시면 됩니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127201930246.png -->

SSH 접속시 비밀번호를 저장하겠느지 여부를 물어봅니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127202000209.png -->

정상적으로 터미널 접속이 된 것을 확인해 볼 수 있습니다.

<!-- Broken Image Removed: D:\jinydev\linux\src\img\image-20210127202110040.png -->

---

[⬅️ 이전: 우분투 에서 OpenSSH 설치하기](../apt/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: Virtualbox_ip ➡️](../virtualbox_ip/)


---

[⬅️ 이전](../)
