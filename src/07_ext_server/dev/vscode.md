---
layout: home
---

vscode 연동
우분투 터미널에서 `code .`을 입력합니다.
다음과 같이 자동으로 vscode를 다운로드 하여 설치를 합니다.

```
hojin@hojin1:~$ code .
Installing VS Code Server for x64 (ff915844119ce9485abfe8aa9076ec76b5300ddd)
Downloading:  45%
```

보안확인을 클릭합니다.
![wsl](./img/wsl.png)


# vscod로 원격 서버 접속하여 개발하기



WSL의 경우에는 ssh를 사용하지 않아도 wsl 확장이 따로 있습니다.

원격 서버까지 워킹 디렉토리로 삼을 수 있습니다.





## 확장 페키지 설치

Remote Development 확장 패키지를 설치합니다.

![image-20210101145030369](D:\onedrive\강의준비\linux\img\image-20210101145030369.png)



## 서버 접속하기

 F1을 눌러 **Remote-SSH: Connect to Host...** 를 실행합니다. 

![image-20210101145323806](D:\onedrive\강의준비\linux\img\image-20210101145323806.png)



Add New SSH Host를 선택합니다.



```
ssh 계정@ip주소or도메인
```

과 같은 형태로 입력을 해줍니다.



다음으로 새창으로 비밀번호를 물어봅니다.





## 리모드 접속



#### 환경설정

![image-20210102231329962](D:\onedrive\강의준비\linux\img\image-20210102231329962.png)



자신의 계정 정보에 환경 설정을 합니다.

```
Host 127.0.0.1
  HostName 127.0.0.1
  port 22
  User 아이디
```

![image-20210102135159200](D:\onedrive\강의준비\linux\img\image-20210102135159200.png)

과 같은 형태로 입력해주시면 


하시면 이제 서버에 접속을 할 수 있습니다. 


![image-20210102135052334](D:\onedrive\강의준비\linux\img\image-20210102135052334.png)


