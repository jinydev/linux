---
layout: home
---

# systemctl 명령어

### systemd
- systemd란 부팅부터 서비스 관리, 로그 관리 등의 시스템 전반적인 영역에 걸쳐있는 프로세스
- 리눅스는 OS이기 때문에 전원을 ON 시킬 경우, 부팅이 되는 과정에서 시스템을 초기화하고, 누군가 환경 설정을 해줘야한다.
- 따라서, 서비스라는 이름으로 띄울 수 있는 systemd라는 init system과 이를 관리하기 위한 도구인 systemctl이 있는 것

### 서비스 제어
- 서비스 목록 확인
```
systemctl list-unit-files
```
- 서비스 시작
```
systemctl start [서비스명]
```
- 서비스 종료
```
systemctl stop [서비스명]
```
- 서비스 재시작
```
systemctl restart [서비스명]
```
- 서비스 활성화
```
systemctl enable [서비스명]
```
- 서비스 비활성화
```
systemctl disable [서비스명]
```
- 서비스 갱신
```
systemctl reload [서비스명]
```

### 시스템 명령
- `systemctl halt` <br>
시스템을 종료시키는 명령어 <br>
이 명령어를 실행하면 시스템이 정지되며, 전원이 완전히 차단된다. 실행하면 모든 프로세스가 중지되고, 디스크와 파일 시스템이 안전하게 비활성화된다
- `systemctl reboot` <br>
시스템을 재부팅하는 명령어 <br>
이 명령어를 실행하면 시스템이 종료되고, 다시 부팅된다. 이 명령어를 실행하면 모든 프로세스가 중지되고, 디스크와 파일 시스템이 안전하게 비활성화됩니다. 그러나 시스템이 다시 부팅된다.