---
layout: home
---

# systemd
`systemd`는 리눅스 시스템의 부팅 및 서비스 관리에 사용되는 시스템 및 서비스 관리 도구입니다. 
> systemd는 이전에 사용되던 `SysVinit`와 `Upstart`와 같은 기존 시스템 관리 도구들을 대체하고 있습니다.

## Systemd의 역할
`systemd`는 시스템의 `초기화` 및 `부팅`을 담당하며, 시스템 서비스 및 데몬을 시작, 중지, 재시작, 감시 및 로그 기록과 같은 관리 작업을 수행합니다. 또한, systemd는 병렬 부팅 및 데몬 로딩을 지원하여 부팅 시간을 단축시키는 등 성능 향상을 제공합니다.

systemd는 대부분의 `최신 리눅스 배포판`에서 기본 시스템 관리 도구로 사용되고 있습니다


## systemd 프로세스
`systemd`는 운영 체제 시작 시, [런레벨](runlevel) 변경 시, 시스템 및 서비스 오류 시 등 다양한 이벤트에서 실행되는 프로세스입니다. 이를 통해 시스템 및 서비스 구성 및 관리에 대한 자동화 수준이 높아지고, 복잡한 서비스 구성 및 관리 작업을 단순화할 수 있습니다.

systemd는 또한 cgroups를 사용하여 프로세스 그룹을 만들어 프로세스 관리와 자원 할당을 향상시키는 등 다양한 기능을 제공합니다. 이를 통해 운영 체제 및 서비스의 안정성과 보안성을 향상시킬 수 있습니다.

## systemd 동작
`systemd`는 1번 PID를 갖는 프로세스로 프로세스 트리에서 가장 상위의 프로세스이며 모든 프로세스의 직간접 부모인 데몬이다. 즉 OS부팅시 systemd 프로세스가 가장 먼저 실행되어서, OS에 필요한 여러 데몬들을 `init`해주는 역할을 하고 있다.  

## systemctl 
Service는 시스템 데몬 및 사용자 정의 데몬을 의미하며, `systemctl` 명령은 service(데몬)들을 관리한다.

## Service 명령
`systemd`를 사용하는 리눅스 배포판에서 service 파일은 서비스를 관리하는 데 사용됩니다. service 파일은 일반적으로 `/etc/systemd/system` 디렉토리에 위치하며 `.service` 확장자를 갖습니다.

이 경로에 있는 service 들은 systemd에 의해 관리되고 있는 service라는 뜻이다.

### service 파일 생성
새로운 서비스 파일을 만드는 방법은 다음과 같습니다.

텍스트 편집기를 사용하여 새로운 파일을 만듭니다.  
예를 들어, `/etc/systemd/system/my-service.service`와 같은 경로에 `my-service.service` 파일을 만듭니다.

서비스 이름과 설명을 정의합니다. 
예를 들어, 다음과 같이 `[Unit]` 섹션을 추가할 수 있습니다.

```
[Unit]
Description=My custom service
```

서비스의 동작을 정의합니다.  
예를 들어, 다음과 같이 `[Service]` 섹션을 추가할 수 있습니다.

```
[Service]
ExecStart=/usr/bin/my-service
Restart=always
```

위의 예에서는 서비스 실행 파일 경로와 재시작 옵션을 정의하고 있습니다.

서비스가 의존하는 다른 서비스를 정의합니다.  
예를 들어, 다음과 같이 `[Unit]` 섹션에 `Requires` 옵션을 추가할 수 있습니다.

```
[Unit]
Description=My custom service
Requires=network.target
```

위의 예에서는 서비스가 `network.target` 서비스에 의존하고 있다는 것을 나타냅니다.

### 서비스 실행하기
서비스 파일을 저장하고 `systemctl` 명령어를 사용하여 서비스를 활성화합니다.

```
$ sudo systemctl daemon-reload
$ sudo systemctl enable my-service.service
$ sudo systemctl start my-service.service
```

위와 같이 하면 새로운 서비스가 생성되고, 서비스를 관리할 수 있게 됩니다.


## Service 파일 속성
Service파일은 `[Unit]`, `[Service]`, `[Install]`의 섹션으로 구성되어 있다.  

* Unit
* Service
* Install