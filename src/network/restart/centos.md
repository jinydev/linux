---
layout: home
---

# 네트워크 재시작 (centos)

CentOS에서 네트워크 설정을 변경한 후, 변경 내용을 적용합니다.

## 네트워크 서비스 재시작

```
sudo systemctl restart network
```
<<<<<<< HEAD

위 명령어는 네트워크 서비스를 완전히 중지하고 다시 시작합니다. 이 때, 네트워크 연결이 일시적으로 끊어질 수 있습니다.

=======
위 명령어는 네트워크 서비스를 완전히 중지하고 다시 시작합니다. 이 때, 네트워크 연결이 일시적으로 끊어질 수 있습니다.

### CentOS 7 이상 버전
CentOS 7 이상 버전에서 "network" 서비스가 더 이상 사용되지 않기 때문에 다음과 같은 오류가 발생합니다. 

```
Failed to restart network.service: unit network.service not found
```

대신 "NetworkManager"를 사용하게 됩니다.

따라서 네트워크 구성 변경 후 변경 내용을 적용하려면 다음과 같은 명령어를 사용해야 합니다.

```
sudo systemctl restart NetworkManager.service
```

위 명령어를 사용하면 변경 내용이 즉시 적용됩니다. 또한 네트워크 구성이 변경된 후에는 systemctl을 사용하여 "NetworkManager" 서비스를 시작하고 활성화해야 합니다.

```
sudo systemctl start NetworkManager.service
sudo systemctl enable NetworkManager.service
```

위 명령어를 사용하여 "NetworkManager" 서비스를 시작하고 부팅 시 자동으로 실행되도록 설정할 수 있습니다.

>>>>>>> master
## 인터페이스 재시작
네트워크 인터페이스를 로드하거나 비활성화하려면, 다음 명령어를 사용합니다.

네트워크 인터페이스 로드:
```
sudo ifup [인터페이스 이름]
```

네트워크 인터페이스 비활성화:

```
sudo ifdown [인터페이스 이름]
```

위 명령어에서 [인터페이스 이름]은 변경한 인터페이스의 이름으로 대체해야 합니다.

ifup 명령어를 사용하여 인터페이스를 로드하면 변경된 네트워크 설정이 즉시 적용됩니다. ifdown 명령어를 사용하여 인터페이스를 비활성화하면 해당 인터페이스의 네트워크 연결이 끊어지게 됩니다.



