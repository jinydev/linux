---
layout : home
---

# WSL이란?

1. 정의 : Linux용 Windows  하위 시스템(Windows Subsystem for Linux)

2. 예전에는 윈도우에서 리눅스를 사용하려면 Virtual Machine과 같은 도구(Virtual Box, VMware 등)을 이용하여 환경을 구성하거나 듀얼 부팅 설정을 해야 했다. (라떼는 말이야..)

   그러나 **WSL을 이용하면 듀얼부팅이나 VM과 같은 느린 환경이 아니라 윈도우에서 리눅스 환경처럼 Powershell을 Bash 처럼 사용하고, Linux 명령어(sed, awk, vim, apt 등)를 사용할 수 있으며 Linux 커널조차 이용할 수 있다. (그것도 매우 빠른 부팅속도와 적은 메모리를 사용하면서 말이다!)**



# WSL1 vs WSL2

![](https://user-images.githubusercontent.com/37948906/117979025-71623200-b36d-11eb-9b8d-cc3204dc878a.png)

WSL1에서는 windows의 NT Kernel 위에 WSL을 올리고 리눅스용 어플리케이션을 돌렸다면, WSL2에서는 Hypervisor 위에 윈도우 NT 커널과 리눅스 커널을 각각 올리는 방식이다.

![](https://user-images.githubusercontent.com/37948906/117979981-7378c080-b36e-11eb-84c2-5c624ea68e41.png)

WSL2는 Linux커널을 직접 사용하기 때문에 파일 시스템 성능이 올라가고 리눅스 시스템 호출 호환성이 대폭 증가했다.



# WSL 명령어 from MS



## 설치

PowerShell

```powershell
wsl --install
```

WSL 및 Linux의 기본 Ubuntu 배포판을 설치합니다. [자세한 정보를 알아보세요](https://learn.microsoft.com/ko-kr/windows/wsl/install). 이 명령을 사용하여 `wsl --install <Distribution Name>`을(를) 실행하여 추가 Linux 배포를 설치할 수도 있습니다. 유효한 배포 이름 목록을 보려면 `wsl --list --online`을(를) 실행합니다.

표시되는 옵션은 다음과 같습니다.

- `--distribution`: 설치할 Linux 배포를 지정합니다. `wsl --list --online`을(를) 실행하여 사용 가능한 배포를 찾을 수 있습니다.
- `--no-launch`: Linux 배포를 설치하지만 자동으로 시작하지는 않습니다.
- `--web-download`: Microsoft Store를 사용하는 대신 온라인 원본에서 설치합니다.

WSL이 설치되지 않은 경우 옵션은 다음과 같습니다.

- `--inbox`: Microsoft Store를 사용하는 대신 Windows 구성 요소를 사용하여 WSL을 설치합니다. *(WSL 업데이트는 스토어를 통해 사용 가능으로 푸시되는 대신 Windows 업데이트를 통해 수신됩니다.)*
- `--enable-wsl1`: Microsoft Store 버전의 WSL을 설치하는 동안 "Linux용 Windows 하위 시스템" 선택적 구성 요소를 사용하도록 설정하여 WSL 1을 사용하도록 합니다.
- `--no-distribution`: WSL을 설치할 때 배포를 설치하지 마세요.

 참고

Windows 10 또는 이전 버전에서 WSL을 실행하는 경우 배포를 지정하기 위해 명령에 플래그 `--install` 를 `wsl --instal -d <distribution name>`포함 `-d` 해야 할 수 있습니다.



## 사용 가능한 Linux 배포판 나열

PowerShell

```powershell
wsl --list --online
```

온라인 스토어를 통해 받을 수 있는 Linux 배포판 목록을 참조하세요. 이 명령은 `wsl -l -o`으로 입력할 수도 있습니다.



## 설치된 Linux 배포판 나열

PowerShell

```powershell
wsl --list --verbose
```

상태(배포판이 실행 중인지 또는 중지되었는지 여부) 및 배포판을 실행하는 WSL 버전(WSL 1 또는 WSL 2)을 포함하여 Windows 머신에 설치된 Linux 배포 목록을 참조하세요. [WSL 1과 WSL 2를 비교](https://learn.microsoft.com/ko-kr/windows/wsl/compare-versions)해 보세요. 이 명령은 `wsl -l -v`로 입력할 수도 있습니다. list 명령과 함께 사용할 수 있는 추가 옵션으로는 모든 배포판을 나열하는 `--all`, 현재 실행 중인 배포판만 나열하는 `--running`, 배포판 이름만 표시하는 `--quiet`가 있습니다.



## WSL 버전을 1에서 2로 설정

PowerShell

```powershell
wsl --set-version <distribution name> <versionNumber>
```

Linux 배포판이 실행 중인 WSL 버전(1 또는 2)을 지정하려면 `<distribution name>`을 배포판 이름으로 바꾸고 `<versionNumber>`를 1 또는 2로 바꿉니다. [WSL 1과 WSL 2를 비교](https://learn.microsoft.com/ko-kr/windows/wsl/compare-versions)해 보세요.



## 기본 WSL 버전 설정

PowerShell

```powershell
wsl --set-default-version <Version>
```

WSL 1 또는 WSL 2의 기본 버전을 설정하려면 `<Version>`을 숫자 1 또는 2로 바꿔서 새 Linux 배포판 설치의 설치 기본값으로 사용할 WSL 버전을 표시합니다. 예: `wsl --set-default-version 2`. [WSL 1과 WSL 2를 비교](https://learn.microsoft.com/ko-kr/windows/wsl/compare-versions)해 보세요.



## 기본 Linux 배포판 설정

PowerShell

```powershell
wsl --set-default <Distribution Name>
```

WSL 명령에서 실행에 사용할 기본 Linux 배포판을 설정하려면 `<Distribution Name>`을 기본 Linux 배포판의 이름으로 바꿉니다.



## 디렉터리를 홈으로 변경

PowerShell

```powershell
wsl ~
```

`~`는 wsl과 함께 사용하여 사용자의 홈 디렉터리에서 시작할 수 있습니다. WSL 명령 프롬프트 내 디렉터리에서 홈으로 다시 이동하기 위해 `cd ~` 명령을 사용할 수 있습니다.



## PowerShell 또는 CMD에서 특정 Linux 배포판 실행

PowerShell

```powershell
wsl --distribution <Distribution Name> --user <User Name>
```

특정 사용자로 특정 Linux 배포판을 실행하려면 `<Distribution Name>`을 기본 Linux 배포판의 이름(즉, Debian)으로 바꾸고 `<User Name>`을 기존 사용자의 이름(예: 루트)으로 바꿉니다. 해당 사용자가 WSL 배포판에 없는 경우 오류가 발생합니다. 현재 사용자 이름을 출력하려면 `whoami` 명령을 사용합니다.



## WSL 업데이트

PowerShell

```powershell
wsl --update
```

WSL 버전을 최신 버전으로 업데이트합니다. 표시되는 옵션은 다음과 같습니다.

- `--web-download`: Microsoft Store가 아닌 GitHub에서 최신 업데이트를 다운로드합니다.



## WSL 상태 확인

PowerShell

```powershell
wsl --status
```

기본 배포판 유형, 기본 배포판 및 커널 버전과 같은 WSL 구성에 대한 일반 정보를 참조하세요.



## WSL 버전 확인

PowerShell

```powershell
wsl --version
```

WSL 및 해당 구성 요소에 대한 버전 정보를 확인합니다.



## Help 명령

PowerShell

```powershell
wsl --help
```

WSL에서 사용할 수 있는 옵션 및 명령 목록을 참조하세요.



## 특정 사용자로 실행

PowerShell

```powershell
wsl -u <Username>`, `wsl --user <Username>
```

WSL을 지정된 사용자로 실행하려면 `<Username>`를 WSL 배포에 있는 사용자의 이름으로 바꿉니다.



## 배포의 기본 사용자 변경

PowerShell

```powershell
<DistributionName> config --default-user <Username>
```

배포 로그인에 대한 기본 사용자를 변경합니다. 사용자가 기본 사용자가 될 수 있도록 배포 내에 이미 있어야 합니다.

예를 들어 `ubuntu config --default-user johndoe`는 Ubuntu 배포에 대한 기본 사용자를 "johndoe" 사용자로 변경합니다.

 참고

배포 이름을 확인하는 데 문제가 있는 경우 `wsl -l` 명령을 사용합니다.

 경고

가져온 배포에는 실행 가능한 시작 관리자가 없기 때문에 이 명령은 작동하지 않습니다. 대신 `/etc/wsl.conf` 파일을 사용하여 가져온 배포의 기본 사용자를 변경할 수 있습니다. [고급 설정 구성](https://learn.microsoft.com/ko-kr/windows/wsl/wsl-config#user-settings) 문서의 자동 탑재 옵션을 참조하세요.



## Shutdown

PowerShell

```powershell
wsl --shutdown
```

실행 중인 모든 배포판과 WSL 2 경량 유틸리티 가상 머신을 즉시 종료합니다. 이 명령은 [메모리 사용 제한 변경](https://learn.microsoft.com/ko-kr/windows/wsl/disk-space) 또는 [.wslconfig 파일 변경](https://learn.microsoft.com/ko-kr/windows/wsl/manage#)처럼 WSL 2 가상 머신 환경을 다시 시작해야 하는 인스턴스에서 필요할 수 있습니다.



## 종료

PowerShell

```powershell
wsl --terminate <Distribution Name>
```

지정된 배포판을 종료하거나 실행을 중지하려면 `<Distribution Name>`을 대상 배포판의 이름으로 바꿉니다.



## 배포 가져오기 및 내보내기

PowerShell

```powershell
wsl --export <Distribution Name> <FileName>
```

PowerShell

```powershell
wsl --import <Distribution Name> <InstallLocation> <FileName>
```

지정된 tar 파일을 새 배포로 가져오고 내보냅니다. 파일 이름은 표준 입력을 위한 것입니다. 표시되는 옵션은 다음과 같습니다.

- `--vhd`: 가져오기/내보내기 배포 지정은 tar 파일이 아닌 .vhdx 파일이어야 합니다.
- `--version`: 가져오기 전용의 경우, 배포를 WSL 1 또는 WSL 2 배포로 가져올지 여부를 지정합니다.



## 배포 위치로 가져오기

PowerShell

```powershell
wsl --import-in-place <Distribution Name> <FileName>
```

지정된 .vhdx 파일을 새 배포로 가져옵니다. 가상 하드 디스크는 ext4 파일 시스템 형식으로 포맷되어야 합니다.



## Linux 배포판 등록 취소 또는 제거

Linux 배포는 Microsoft Store를 통해 설치할 수 있지만 이를 통해 제거할 수는 없습니다.

WSL 배포를 등록 취소하고 제거하려면 다음을 수행합니다.

PowerShell

```powershell
wsl --unregister <DistributionName>
```

`<DistributionName>`를 대상 Linux 배포의 이름으로 바꾸면 WSL에서 해당 배포를 등록 취소하여 다시 설치하거나 정리할 수 있습니다. **주의:** 등록이 취소되면 해당 배포와 관련된 모든 데이터, 설정 및 소프트웨어가 영구적으로 손실됩니다. 스토어에서 다시 설치하면 배포의 새 복사본이 설치됩니다. 예를 들어 `wsl --unregister Ubuntu`는 WSL에서 사용할 수 있는 배포에서 Ubuntu를 제거합니다. `wsl --list`를 실행하면 더 이상 나열되지 않습니다.

다른 스토어 애플리케이션과 마찬가지로 Windows 머신에서 Linux 배포판 앱을 제거할 수도 있습니다. 다시 설치하려면 Microsoft Store에서 해당 배포를 찾아 "시작"을 선택합니다.



## 디스크 또는 디바이스 탑재

PowerShell

```powershell
wsl --mount <DiskPath>
```

`<DiskPath>`를 디스크가 있는 디렉터리\파일 경로로 바꿔서 모든 WSL2 배포판에 물리적 디스크를 연결하고 탑재합니다. [WSL 2에 Linux 디스크 탑재](https://learn.microsoft.com/ko-kr/windows/wsl/wsl2-mount-disk)를 참조하세요. 다음 옵션을 사용할 수 있습니다.

- `--vhd`: `<Disk>`(이)가 가상 하드 디스크를 참조하도록 지정합니다.
- `--name`: 탑재 지점에 대한 사용자 지정 이름을 사용하여 디스크를 탑재합니다.
- `--bare`: WSL2에 디스크를 연결하지만 탑재하지는 않습니다.
- `--type <Filesystem>`: 디스크를 탑재할 때 사용되는 파일 시스템 유형입니다. 지정하지 않으면 기본값은 ext4입니다. 이 명령은 `wsl --mount -t <Filesystem>`으로 입력할 수도 있습니다. `blkid <BlockDevice>` 명령을 사용하여 파일 시스템 형식을 검색할 수 있습니다(예: `blkid <dev/sdb1>`).
- `--partition <Partition Number>`: 탑재할 파티션의 인덱스 번호입니다. 지정하지 않으면 전체 디스크가 기본값입니다.
- `--options <MountOptions>`: 디스크를 탑재할 때 포함할 수 있는 몇 가지 파일 시스템 관련 옵션이 있습니다. `wsl --mount -o "data-ordered"` 또는 `wsl --mount -o "data=writeback` 같은 [ext4 탑재 옵션](https://www.kernel.org/doc/Documentation/filesystems/ext4.txt)을 예로 들 수 있습니다. 그러나 현재는 파일 시스템 관련 옵션만 지원됩니다. `ro`, `rw` 또는 `noatime`과 같은 일반 옵션은 지원되지 않습니다.

 참고

wsl.exe(64비트 도구)에 액세스하기 위해 32비트 프로세스를 실행하는 경우 `C:\Windows\Sysnative\wsl.exe --command`와 같은 방식으로 이 명령을 실행해야 할 수도 있습니다.



## 디스크 분리

PowerShell

```powershell
wsl --unmount <DiskPath>
```

디스크 경로에 지정된 디스크를 분리합니다. 디스크 경로가 지정되지 않은 경우, 이 명령은 탑재된 모든 디스크를 장착 해제하여 분리합니다.



## 사용되지 않은 WSL 명령

PowerShell

```powershell
wslconfig.exe [Argument] [Options]
```

PowerShell

```powershell
bash [Options]
```

PowerShell

```powershell
lxrun /[Argument]
```

이러한 명령은 WSL과 함께 설치된 Linux 배포판을 구성하는 원래 wsl 구문이지만 `wsl` 또는 `wsl.exe` 명령 구문으로 대체되었습니다.



# WSL 명령어 from powershell  wsl --help

사용량: wsl.exe [Argument] [Options...] [CommandLine]

Linux 바이너리를 실행하기 위한 인수:

      명령줄이 제공되지 않으면 wsl.exe가 기본 셸을 시작합니다.
    
    --exec, -e <CommandLine>
        기본 Linux 셸을 사용하지 않고 지정된 명령을 실행합니다.
    
    --shell-type <Type>
        제공된 셸 유형으로 지정된 명령을 실행합니다.
    
        유형:
            standard
                기본 Linux 셸을 사용하여 지정된 명령을 실행합니다.
    
            login
                기본 Linux 셸을 로그인 셸로 사용하여 지정된 명령을 실행합니다.
    
            none
                기본 Linux 셸을 사용하지 않고 지정된 명령을 실행합니다.
    
    --
        나머지 명령줄을 있는 그대로 전달합니다.

옵션:
    --cd <Directory>
        지정된 디렉터리를 현재 작업 디렉터리로 설정합니다.
        ~가 사용되면 Linux 사용자의 홈 경로가 사용됩니다. 경로가
        / 문자로 시작되면 절대 Linux 경로로 해석됩니다.
              그렇지 않으면 값은 절대 Windows 경로여야 합니다.

    --distribution, -d <Distro>
        지정된 배포를 실행합니다.
    
    --user, -u <UserName>
        지정된 사용자로 실행합니다.
    
    --system
        시스템 배포용 셸을 시작합니다.

Linux용 Windows 하위 시스템 관리에 대한 인수:

    --help
        사용 정보를 표시합니다.
    
    --debug-shell
        진단 목적을 위해 WSL2 디버그 셸을 엽니다.
    
     --event-viewer
        Windows 이벤트 뷰어의 애플리케이션 뷰를 엽니다.
    
    --install [Distro] [Options...]
        Linux 배포용 Windows 하위 시스템을 설치합니다.
         유효한 배포 목록을 보려면 'wsl.exe --list --online'을 사용하세요.
    
        옵션:
            --no-launch, -n
                설치 후 배포를 시작하지 마세요.
    
            --web-download
                Microsoft Store 대신 인터넷에서 배포를 다운로드하세요.
    
    --mount <Disk>
        모든 WSL 2 배포에 물리적 또는 가상 디스크를 연결하고 탑재합니다.
    
        옵션:
            --vhd
                <Disk>가 가상 하드 디스크를 참조하도록 지정합니다.
    
            --bare
                디스크를 WSL2에 연결하되 탑재하지는 마세요.
    
            --name <Name>
                탑재 지점에 대한 사용자 지정 이름을 사용하여 디스크를 탑재합니다.
    
            --type <Type>
                지정되지 않은 경우 디스크를 탑재할 때 사용할 파일 시스템은 기본적으로 ext4입니다.
    
            --options <Options>
                추가 탑재 옵션.
    
            --partition <Index>
                탑재할 파티션의 인덱스를 지정하지 않으면 기본적으로 전체 디스크가 됩니다.
    
    --release-notes
        웹 브라우저를 열어 WSL 릴리스 노트 페이지를 봅니다.
    
    --set-default-version <Version>
        새 배포의 기본 설치 버전을 변경합니다.
    
    --shutdown
        실행 중인 모든 배포와 WSL 2
        경량 유틸리티 가상 머신을 즉시 종료합니다.
    
    --status
        Linux용 Windows 하위 시스템의 상태를 표시합니다.
    
    --unmount [Disk]
        모든 WSL2 배포에서 디스크를 탑재 해제하고 분리합니다.
        인수 없이 호출되는 경우 모든 디스크를 탑재 해제하고 분리합니다.
    
    --update
        Linux용 Windows 하위 시스템 패키지를 업데이트합니다.
    
        옵션:
            --web-download
                Microsoft Store 대신 인터넷에서 업데이트를 다운로드합니다.
    
            --pre-release
                가능한 경우 사전 릴리스 버전을 다운로드합니다. --web-download를 의미합니다.
    
    --version, -v
        버전 정보를 표시합니다.

Linux용 Windows 하위 시스템에서 배포를 관리하기 위한 인수:

    --export <Distro> <FileName> [Options]
        배포를 tar 파일로 내보냅니다.
        파일 이름은 - 표준 출력일 수 있습니다.
    
        옵션:
            --vhd
                배포를 .vhdx 파일로 내보내도록 지정합니다.
    
    --import <Distro> <InstallLocation> <FileName> [Options]
        지정된 tar 파일을 새 배포로 가져옵니다.
        파일 이름은 표준 입력의 경우 -일 수 있습니다.
    
        옵션:
            --version <Version>
                새 배포에 사용할 버전을 지정합니다.
    
            --vhd
                제공된 파일이 tar 파일이 아닌 .vhdx 파일임을 지정합니다.
                이 작업은 지정된 설치 위치에 .vhdx 파일의 복사본을 만듭니다.
    
    --import-in-place <Distro> <FileName>
        지정된 .vhdx 파일을 새 배포로 가져옵니다.
        이 가상 하드 디스크는 ext4 파일 시스템 유형으로 포맷해야 합니다.
    
    --list, -l [Options]
        배포를 나열합니다.
    
        옵션:
            --all
                현재 설치 중이거나 제거 중인 배포를 포함하여
                모든 배포를 나열합니다.
    
            --running
                현재 실행 중인 배포만 나열합니다.
    
            --quiet, -q
                배포 이름만 표시합니다.
    
            --verbose, -v
                모든 배포에 대한 자세한 정보를 표시합니다.
    
            --online, -o
                'wsl.exe --install'을 사용하여 설치할 수 있는 배포 목록을 표시합니다.
    
    --set-default, -s <Distro>
        배포를 기본값으로 설정합니다.
    
     --set-version<Distro> <Version>
        지정된 배포의 버전을 변경합니다.
    
    --terminate, -t <Distro>
        지정된 배포를 종료합니다.
    
    --unregister <Distro>
        배포를 등록 취소하고 루트 파일 시스템을 삭제합니다.

