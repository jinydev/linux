---
layout: post
title: "Day6_Bridge, NAT, Host-Only 비교"
date: 2023-04-24 18:10:32 +0900
comment: true
---


### Bridged

Bridged 설정은 Host-PC, 즉 VMware를 돌리고 있는 자신의 PC 랜 설정을 그대로 복사한다고 생각하면 편합니다.

Host-PC의 네트워크 설정

![https://blog.kakaocdn.net/dn/cS8isZ/btrgTEnJfSN/kALLSJFtsvEFwU1diKd6Ak/img.png](https://blog.kakaocdn.net/dn/cS8isZ/btrgTEnJfSN/kALLSJFtsvEFwU1diKd6Ak/img.png)

Win10안에 실행되는 VMware에서 Bridged 네트워크 설정을 한다면 Host-PC의 랜카드와 Direct로 연결이 되면서 인터넷이 가능해지는 구조입니다. 그러므로 IP도 Host-PC와 같이 192.169.0.X 대역을 할당받게 됩니다.

![1](https://user-images.githubusercontent.com/47453097/234159809-61664058-b440-4c39-8ad7-6654d63bca1c.png)


Win7을 Bridged로 설정하고 네트워크 설정을 보면 IP를 192.168.0.x대로 받고 게이트웨이도 Host-PC와 같은 것을 볼 수 있습니다.

---

### NAT(Network Adress Translation)

NAT설정은 가상머신들이 사설 IP를 할당받아 가상머신들끼리 네트워크를 구축하면서 인터넷도 사용할 수 있는 설정이라고 생각하면 편합니다.

![https://blog.kakaocdn.net/dn/HlkAI/btrgMz1q7Fy/KtfpJGyicUYLDHhKXyo0Fk/img.png](https://blog.kakaocdn.net/dn/HlkAI/btrgMz1q7Fy/KtfpJGyicUYLDHhKXyo0Fk/img.png)

저희가 예전을 돌이켜보면 DB시간에 CentOS7를 사용했을때 VMware인데도 인터넷이 잘 됐었습니다. 그런데 최근 리눅스시간에 VMware로 인터넷을 접속하려 했는데 다 안돼서 VirtualBox로 갈아탔습니다. 그 이유가 여기에 있습니다.

저희는 NAT IP를 192.168.119.1로 고정해놨기 때문에, CentOS에서 이 고정된 IP를 사용해서 인터넷이 됐었고, 추후 설치한 Ubuntu와 Rocky에서 인터넷이 할당되지 않았기 때문에 인터넷이 되지 않았던 것입니다.

![2](https://user-images.githubusercontent.com/47453097/234159848-e271e2fe-707e-4b7e-93ab-17629accb710.png)

Ubuntu와 Rocky에서 인터넷을 사용하려면, 이렇게 자동으로 IP를 받을 수 있게 DHCP 기능을 켜주면 됩니다.

![3](https://user-images.githubusercontent.com/47453097/234159838-037500fe-eb4b-4927-97d1-24c51f73cb71.png)

그렇다면 인터넷으로 패킷이 나갈때 IP는 어떻게 될 것인가?

![4](https://user-images.githubusercontent.com/47453097/234159857-41e84320-1db9-440c-aabb-f879b2aef3b1.png)

Wireshark로 이더넷과 VMnet8의 패킷을 캡쳐해보면 VMnet8에서 8.8.8.8로 패킷을 보내면 이더넷에서 Host-PC의 IP로 8.8.8.8과 통신을 하는 것을 볼 수 있습니다.

즉, 주소가 자동으로 변환(Network Adress Translation)되어 인터넷을 할 수 있는것을 볼 수 있습니다.

---

### Host-only

Host-only는 쉽게 얘기하면 위의 NAT에서 이더넷과 연결되어 있는 게이트웨이가 없어서 가상머신들끼리만 통신할 수 있는 네트워크 설정입니다. Host-only는 내부네트워크설정과 비슷하지만, 내부네트워크와 다르게 가상머신 안의 HostOS(밖에 기준으론 GuestOS)에 HostIP를 각각 할당해 줄 수 있습니다.

![https://blog.kakaocdn.net/dn/rXZ3E/btrgWD2tnP4/jeKDwTdN2JltkFw0cykH91/img.png](https://blog.kakaocdn.net/dn/rXZ3E/btrgWD2tnP4/jeKDwTdN2JltkFw0cykH91/img.png)

Host-only의 구성도입니다. Hub덕분에 가상머신들끼리는 통신할 수 있지만 이더넷에 연결이 되지 않아 인터넷을 쓸 수는 없습니다.

![5](https://user-images.githubusercontent.com/47453097/234159884-897fe69d-8e96-4177-b296-5cc536c6a75c.png)