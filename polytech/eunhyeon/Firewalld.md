---
layout: home
---

# 리눅스 방화벽 제어하기
## 0421. Firewalld
<hr/>

> 방화벽(Firewall)은 불필요한 네트워크 연결을 완전히 차단하여, 악의적인 외부 공격으로부터 시스템의 항구를 보호하는 가장 강력하고 기본적인 보안 문지기 장치입니다. 리눅스 서버에서는 특정 허용된 규약(Port, IP)만 서버에 접속할 수 있도록 엄격한 차단(Default Drop) 정책을 적용해야 합니다.

전통적인 리눅스 커널 방화벽 통제 체계로 `iptables`가 오랜 세월 사용되어 왔으나, 구문이 직관적이지 않고 관리가 몹시 복잡했습니다. 최근 레드햇/CentOS 및 범용 배포판들은 더욱 유연한 설계 사상을 가진 **`firewalld`**를 표준 방화벽 관리 도구로 채택하는 추세입니다.

## 1. Firewalld의 주요 특징
1. **존(Zone) 기반의 논리적 관리 체계:**
   신뢰성 수준에 따라 네트워크 인프라 규칙을 `public`, `home`, `trusted` 등의 여러 '구역(Zone)' 그룹으로 분리하여 관리할 수 있게 해 주어 관리가 매우 수월합니다.
2. **동적(Dynamic) 업데이트 지원:**
   기존 `iptables` 처럼 룰 하나를 변경할 때마다 방화벽 전체 데몬을 완전 재시작하는 치명적 단점을 개선하였습니다. 현재 허용된 다른 클라이언트의 접속이나 연결(Session)을 끊지 않으면서도, 런타임(Runtime) 상태에서 실시간으로 룰만 추가할 수 있습니다.

## 2. 방화벽 설치 및 데몬 시작

```bash
# firewalld 패키지 설치
sudo dnf install firewalld   

# 서버 부팅 시 데몬이 자동 실행되도록 시스템 레지스트리(systemd)에 등록
sudo systemctl enable firewalld   

# 현재 즉시 방화벽 구동 시작
sudo systemctl start firewalld   

# 데몬의 구동 상태 체크
sudo firewall-cmd --state
```

## 3. 핵심 명령어 (firewall-cmd) 패턴

방화벽 정책을 세울 때, 기본적으로 **포트 번호(Port)**를 개방하거나 혹은 널리 알려진 **서비스 명칭(Service)** 자체를 개방할 수 있습니다. 

어떤 룰을 추가할 때 뒤에 `--permanent` 인자를 붙이지 않으면 영구 저장되지 않으며, 서버를 재부팅하면 즉시 규칙 증발을 겪게 되므로 실무에서는 인자를 명시하여 영구 설정하고, 즉시 반영되도록 릴로드 시키는 방식을 주로 사용합니다.

```bash
# 1. 특정 서비스(HTTP) 방화벽 빗장 해제 및 차단
sudo firewall-cmd --permanent --add-service=http     # 허용(Open)
sudo firewall-cmd --permanent --remove-service=http  # 차단(Drop)

# 2. 특정 포트(Port) 직접 명시하여 해제 및 차단
sudo firewall-cmd --permanent --add-port=8080/tcp    # 8080 TCP포트 개방
sudo firewall-cmd --permanent --remove-port=8080/tcp # 8080 TCP포트 차단

# 3. 특정 IP 주소 원천 차단 및 허가 (IP 블로킹)
sudo firewall-cmd --permanent --add-source=192.168.0.100

# 4. 방화벽 룰 재적용 (필수 마무리 작업)
# --permanent로 설정한 룰은 곧바로 적용되지 않으므로 데몬을 릴로드하여 반영합니다.
sudo firewall-cmd --reload

# 5. 현재 활성화된 적용 리스트 최종 확인
sudo firewall-cmd --list-all
```