---
layout: home
title: "Service 명령"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# Service 명령

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


---

[⬅️ 이전](../)
