---
layout: home
typora-copy-images-to: ./img
---

# SystemCtl
서비스 유닛 (.service)을 관리 및 제어하는 명령어 이다. CentOS7 버전 부터 사용하는 명령어이며, 이전버전에서는 Service 명령어로 사용이 가능하다.

## SystemCtl이란
`systemctl`은 리눅스 시스템의 `서비스` 및 `프로세스 관리`를 위한 명령어입니다. `Systemd`라는 초기화 시스템을 사용하는 최신 리눅스 배포판에서 사용됩니다.

> `systemd`는 시스템의 부팅, 종료, 서비스 관리 등을 담당하는 초기화 시스템으로, 여러 프로세스 및 서비스를 시작하고 관리합니다. 이러한 systemd의 기능을 사용하기 위해서는 `systemctl` 명령어를 사용해야 합니다.

systemctl은 시스템 관리자가 서비스를 제어할 수 있도록 다양한 옵션을 제공합니다. 예를 들어, systemctl start, systemctl stop, systemctl restart, systemctl status 등의 명령어를 사용하여 서비스를 시작, 정지, 재시작 및 상태를 확인할 수 있습니다. 또한, systemctl enable 명령어를 사용하여 시스템 부팅 시 자동으로 서비스가 시작되도록 설정할 수 있습니다.


## wsl 에서 systemctl 사용
WSL은 Windows 운영체제에서 Linux 환경을 구현한 것으로, Windows 서비스 매니저와 Linux 서비스 매니저 간의 호환성 문제로 인해 WSL에서는 systemctl을 사용할 수 없습니다.

```bash
hojin@hojin3:~$ systemctl
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

wsl은 기본적으로 window를 main server로 사용할뿐 윈도우와 리눅스가 멀티부팅이 되는 시스템이 아니다.

ubuntu 리눅스의 `service`기능을 같이 사용하기 위해서는 호스트 윈도우가 시작시 리눅스의 서비스도 같이 실행해 주어야 하기 때문이다. 이를 위해서는 별도로 systemctl 명령어를 활성화 해야 한다.


`DamionGans`가 공개한 스크립트를 통하여 systemctl을 활성화 보도록 한다. 다음과 같이 git으로 저장소를 클론한다.
> 만일 git이 설치되어 있지 않다면 `apt install git`을 실행하여 설치 합니다.

```bash
# WSL2 regist Script clone
git clone https://github.com/DamionGans/ubuntu-wsl2-systemd-script.git
cd ubuntu-wsl2-systemd-script/
bash ubuntu-wsl2-systemd-script.sh
# Enter your password and wait until the script has finished
```

wsl을 다시 실행합니다. 다음과 같이 명령어를 입력해 봅니다.
```bash
# restart WSL window and Check status
systemctl
```

