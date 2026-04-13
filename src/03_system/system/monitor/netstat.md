---
layout: home
---

# netstat
Linux netstat 명령은 네트워크 연결, 라우팅 테이블, 인터페이스 통계 등과 같은 다양한 네트워크 관련 정보를 표시하는 도구입니다.  

```bash
poly@u22d:~$ netstat
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 localhost:zabbix-agent  localhost:52496         TIME_WAIT
tcp        0      0 localhost:35588         localhost:zabbix-agent  TIME_WAIT
tcp        0      0 localhost:zabbix-agent  localhost:43852         TIME_WAIT
tcp        0      0 localhost:zabbix-agent  localhost:52466         TIME_WAIT
tcp        0      0 localhost:zabbix-agent  localhost:43322         TIME_WAIT
tcp        0      0 localhost:41192         localhos:zabbix-trapper TIME_WAIT
tcp        0      0 localhost:zabbix-agent  localhost:43282         TIME_WAIT
tcp        0      0 localhost:zabbix-agent  localhost:43838         TIME_WAIT
tcp        0      0 localhos:zabbix-trapper localhost:42914         TIME_WAIT
tcp        0      0 localhost:zabbix-agent  localhost:35564         TIME_WAIT
```



다음은 netstat에서 사용되는 몇 가지 주요 용어입니다.


Proto: TCP 또는 UDP와 같이 네트워크 연결에 사용되는 프로토콜입니다.
로컬 주소: 네트워크 연결의 로컬 끝 IP 주소 및 포트 번호입니다.
외부 주소: 네트워크 연결의 원격 끝 IP 주소 및 포트 번호입니다.
상태: "ESTABLISHED", "CLOSE_WAIT" 또는 "TIME_WAIT"와 같은 네트워크 연결의 현재 상태입니다.
Recv-Q: 연결의 로컬 끝에서 수신 대기 중인 데이터의 양.
Send-Q: 연결의 로컬 끝에서 전송을 기다리는 데이터의 양.
Inode: 네트워크 연결에 대한 고유 식별자입니다.
설정됨: 현재 설정된 네트워크 연결 수입니다.
Syn-Sent: SYN-SENT 상태에서 활성 TCP 연결 수.
Syn-Recv: SYN-RECV 상태에서 활성 TCP 연결 수입니다.
Fin-Wait-1: FIN-WAIT-1 상태에서 활성 TCP 연결 수.
Fin-Wait-2: FIN-WAIT-2 상태에서 활성 TCP 연결 수.
Time-Wait: TIME-WAIT 상태에서 활성 TCP 연결 수.
닫기: CLOSE 상태에서 활성 TCP 연결 수.
Close-Wait: CLOSE-WAIT 상태에서 활성 TCP 연결 수.
Last-Ack: LAST-ACK 상태에서 활성 TCP 연결 수.
Listen: Listening 상태의 소켓 수.
Cwnd: 연결을 위한 혼잡 윈도우 크기.
RTT: 연결에 대한 예상 왕복 시간.
MSS: 연결을 위한 최대 세그먼트 크기.
Windows: 연결을 위한 수신 창의 크기.