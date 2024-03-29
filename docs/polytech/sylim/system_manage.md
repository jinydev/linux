# 원격지 시스템 관리하기

### 텔넷 서버
텔넷 서버 : 지금은 많이 사용하지 않지만, 오랫동안 전통적으로 사용되어 온 원격 접속 방법 <br>
오래되었기 때문에 보안에 취약하기에 텔넷과 보안 기능을 더해서 사용한다.

###  텔넷 서버 구축하기
1. 텔넷 서버 설치
2. 텔넷 서비스 시작
3. 텔넷 전용 사용자 생성
4. 방화벽 설정 (포트 열기)
5. 텔넷 서비스 상시 가동
6. 클라이언트에서 접속

### OpenSSH 서버
OpenSSH 서버 : 텔넷과 용도는 같지만 보안이 강화된 서버 <br>
텔넷의 경우 서버와 클라이언트 사이에 데이터를 전송할 때 암호화를 하지 않아 보안상 취약한데 이를 해결하기 위해 사용하는 리눅스에서 지원하는 서버이다.

### OpenSSH 서버 구축하기
1. openssh 서버 확인
2. 방화벽 설정
3. 리눅스 & 윈도우 클라이언트에서 접속
4. 윈도우 클라이언트에서 접속 시 Putty 설치

### VNC 서버
VNC 서버 : 원격지에서 X 윈도 환경을 사용할 수 있게 하는 서버 프로그램 <br>
텔넷과 개념이 거의 같지만, VNC의 경우에는 별도의 클라이언트 프로그램을 설치해야 한다. <br>
또한 원격지로 그래픽 화면을 전송하는 원리이므로, 텍스트만 전송하는 텔넷과 비교했을 때 속도가 많이 느려지는 단점이 있다.

### VNC 서버 구축
1. VNC 서버 설치
2. 서버 설정 파일 복사 및 수정
3. 방화벽 설정
4. VNC 사용자 접속 및 서비스 시작
5. VNC 클라이언트 설치
6. VNC 클라이언트 실행
7. 해상도 조절

### 세 가지 서버 비교
|구분|텔넷 서버|SSH 서버|VNC 서버|
|---|---|---|---|
|속도|빠름|빠름|많이 느림|
|보안|취약|강함|취약하지만 SSH와 연동 가능|
|사용 가능 명령어|텍스트 모드|텍스트 모드|제한 없음|
|클라이언트 프로그램|대개의 운영체제에 기본적으로 있음|리눅스에는 기본적으로 있음, 윈도우는 별도 설치 필요|별도 설치 필요|
- 각각의 장단점이 있지만, 빠른 속도와 보안 강화 측면에서 SSH를 기본적으로 사용할 수 있게 설정하고, VNC서버는 설정만 해놓고 가동하지 않으면 된다. 
- 원격지에서 SSH서버로 접속해 관리하다가, X 윈도 환경 접속이 필요한 경우에는 SSH서버 접속창에서 VNC서버를 구동시켜주고 VNC클라이언트로 접속하면 된다.