---
layout: home
---

# CentOS에서 ICMP 패킷을 허용

## 방화벽 설정 확인하기
먼저 CentOS에서 방화벽이 활성화되어 있는지 확인합니다. 방화벽이 활성화되어 있다면, ICMP 패킷을 허용하는 규칙을 추가해야 합니다. 방화벽 설정을 확인하려면 다음 명령어를 실행합니다.

```
sudo firewall-cmd --list-all
```

## 방화벽 규칙 추가하기
ICMP 패킷을 허용하는 규칙을 추가하려면 다음 명령어를 실행합니다.

```
sudo firewall-cmd --zone=public --add-icmp-block-inversion
sudo firewall-cmd --zone=public --add-icmp-block=echo-request
sudo firewall-cmd --runtime-to-permanent
```

위 명령어는 public zone에 대해 ICMP 패킷을 허용하는 규칙을 추가합니다.

## 방화벽 규칙 적용하기
규칙을 추가한 후, 방화벽 서비스를 재시작하여 규칙을 적용합니다.

```
sudo systemctl restart firewalld
```

이제 CentOS에서 ICMP 패킷을 허용하도록 설정되었습니다. 다른 시스템에서 CentOS로 ping 요청을 보내면 응답이 돌아와야 합니다.