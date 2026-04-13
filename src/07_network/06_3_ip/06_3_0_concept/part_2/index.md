---
layout: home
title: "2. 실습 고정 IPStatic로 영구 변경하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 2. 실습 고정 IPStatic로 영구 변경하기

## 2. [실습] 고정 IP(Static)로 영구 변경하기

> 외부 레퍼런스 참고: [우분투 22.04 LTS 고정 IP 설정 가이드](https://it-svr.com/ubuntu-22-04-lts-static-ip/)

최신 우분투는 네트워크 관리를 모두 `yaml(야믈)`이라는 띄어쓰기 엄격 포맷을 사용하는 **Netplan 매니저** 로 컨트롤합니다. 아래와 같이 root 관리자 모드로 야믈 파일을 열고 세팅합니다.

### 실습 1. Netplan 설정 파일 열고 편집
```bash
# 반드시 관리자 (sudo) 권한으로 /etc/netplan 폴더 깊은 곳의 파일을 에디터로 엽니다.
# (파일명 01-network... 등은 컴퓨터마다 앞 숫자가 다를 수 있습니다)
sudo vi /etc/netplan/01-network-manager-all.yaml
```

### 실습 2. YAML 편집 (수동 IP 입력)
에디터 화면에서 다음과 같이 공백(Space) 간격을 철저히 맞추어 IP 세트를 강제 입력합니다.
```yaml
# This is the network config written by 'subiquity'
network:
  version: 2
  ethernets:
    ens18:     # (본인 컴퓨터의 ifconfig 통신 인터페이스 이름으로 맞춰야 함)
      addresses:
        - 192.168.1.12/24    # (강제로 고정할 서버 주소와 /24 대역 마스크)
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]   # (구글의 글로벌 접속 DNS 세우기)
      routes:
        - to: default
          via: 192.168.1.1   # (인터넷으로 나가는 내 집/회사 공유기의 게이트웨이 주소)
```

### 실습 3. 변경 사항 시스템 강제 적용 (Apply)
위처럼 파일을 저장하고 빠져나온 후, Netplan 백그라운드 엔진을 재부팅시켜 바뀐 고정IP를 즉시 입혀줍니다.
```bash
sudo netplan apply
```

---


---

[⬅️ 이전: 9.2 IP 설정 및 확인](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../) &nbsp;|&nbsp; [다음 ➡️](../)


---

[⬅️ 이전](../)
