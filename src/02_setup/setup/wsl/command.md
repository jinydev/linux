---
layout: home
---

# WSL 설치 및 명령어
WSL(Windows Subsystem for Linux)은 윈도우 10에서 리눅스 환경을 지원하는 기능으로, 터미널에서 다양한 명령어를 사용할 수 있습니다.

## WSL 명령어
일반적인 리눅스 명령어 외에도 WSL에서만 사용하는 명령어도 있습니다. 일부 예시는 아래와 같습니다.

* wsl: WSL 배포판에서 명령어를 실행합니다.
* wslconfig: WSL 배포판을 구성하고 관리합니다.
* code: Visual Studio Code를 WSL에서 실행합니다.
* explorer.exe: 파일 탐색기를 WSL에서 실행합니다.
* powershell.exe: PowerShell을 WSL에서 실행합니다.
* cmd.exe: Windows 명령 프롬프트를 WSL에서 실행합니다.

이외에도 다양한 명령어가 있으며, WSL에서는 대부분의 리눅스 명령어를 사용할 수 있습니다.

## 지원가능한 WSL 리눅스
현재 WSL에서 지원 가능한 리눅스 배포판(Distribution)은 다음과 같습니다.

* Ubuntu
* Debian
* Kali Linux
* OpenSUSE Leap
* SUSE Linux Enterprise Server
* Fedora Remix for WSL
* Pengwin
* Pengwin Enterprise

이외에도 여러 가지 리눅스 배포판이 WSL에서 작동할 수 있지만, 위에서 언급한 배포판들은 공식적으로 Microsoft에서 지원하고 있는 배포판입니다.

```
wsl -l -o
```

WSL에서는 Windows에서 Linux 애플리케이션을 실행하는 데 필요한 라이브러리, 실행환경 등을 지원하므로, 리눅스 애플리케이션을 Windows에서 바로 실행할 수 있습니다. 또한, WSL에서는 Windows와 Linux 간의 파일 공유, 네트워크 공유 등이 가능합니다.


## WSL 설치하기
* [관리](list)
* [설치하기](install)
* [사용자 계정](user)
* [접속](access)
