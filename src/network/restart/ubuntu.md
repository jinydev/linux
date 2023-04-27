---
layout: home
---

# 네트워크 재시작(우분투)
우분투 리눅스에서 네트워크 IP를 변경한 후 변경 내용을 적용하려면, 다음 두 가지 방법 중 하나를 사용할 수 있습니다.

## Network Service 재시작
네트워크 설정을 변경한 후, 다음 명령어를 사용하여 네트워크 서비스를 재시작합니다.

```
sudo service networking restart
```
위 명령어는 네트워크 서비스를 완전히 중지하고 다시 시작하므로, 네트워크 연결이 일시적으로 끊어질 수 있습니다.

### ifupdown 패키지
Ubuntu 16.04부터 네트워크 설정 방식이 변경되면서 networking.service 서비스가 deprecated되었습니다.

따라서 `networking`명령을 입력하게 되면 다음과 같은 오류가 발생될 수 있습니다.

```
failed to restart networking.service: unit networking.service not found
```

이 오류는 systemd-networkd.service와 systemd-resolved.service가 추가되면서 발생하는 문제입니다.

따라서, Ubuntu 16.04 이상 버전에서는 systemd-networkd.service와 systemd-resolved.service를 사용하여 네트워크 설정을 관리해야 합니다.

만약, networking.service를 사용하여 네트워크 설정을 관리하고 싶다면, 다음과 같이 `ifupdown` 패키지를 설치하여 networking.service를 사용할 수 있습니다.

#### ifupdown 패키지 설치
먼저, 다음 명령어를 사용하여 ifupdown 패키지를 설치합니다.

```
sudo apt update
sudo apt install ifupdown
```

#### networking.service 활성화 및 시작
다음으로, 다음 명령어를 사용하여 networking.service를 활성화하고 시작합니다.

```bash
sudo systemctl enable networking.service
sudo systemctl start networking.service
```

이제 networking.service를 사용하여 네트워크 설정을 관리할 수 있습니다. 하지만, systemd-networkd.service와 systemd-resolved.service가 제공하는 다양한 기능을 사용할 수 없게 됩니다. 따라서, Ubuntu 16.04 이상 버전에서는 systemd-networkd.service와 systemd-resolved.service를 사용하여 네트워크 설정을 관리하는 것을 권장합니다.

## 인터페이스 다시 로드
또 다른 방법은 변경된 네트워크 설정을 인터페이스에 다시 로드하는 것입니다. 이 방법은 네트워크 연결이 끊어지지 않습니다.

먼저, 다음 명령어를 사용하여 네트워크 인터페이스를 비활성화합니다.

```
sudo ip link set [인터페이스 이름] down
```
그리고나서, 다음 명령어를 사용하여 인터페이스를 다시 로드합니다.


```
sudo ip link set [인터페이스 이름] up
```
위 명령어에서 [인터페이스 이름]은 변경한 인터페이스의 이름으로 대체해야 합니다.

이 방법은 Network Service를 재시작하는 것보다 빠르고 안정적입니다.