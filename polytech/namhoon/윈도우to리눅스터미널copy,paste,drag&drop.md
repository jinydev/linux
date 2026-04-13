---
layout: home
title: "클립보드 장벽 돌파: 버추얼박스 Additions"
---

# 가상화의 저주 풀기: Guest Additions (클립보드 및 드래그 앤 드롭)

버추얼박스 프로그램 안에서 돌아가는 리눅스 화면은 철저하게 보안 격리된 모니터 그림장에 불과합니다. 윈도우 크롬에서 치던 명령어를 마우스로 Ctr+C 해서 가상 리눅스 터미널에 Ctrl+V 붙여 넣으려 해도 절대 들어가지 않는 이 클립보드 장벽을 뚫기 위해 마법의 유틸리티인 **'Guest Additions'** 컴포넌트를 주입해야 합니다.

---

## 1. 우분투 환경의 클립보드 동기화 수술

우분투가 윈도우 본체의 명령을 유연하게 수용하도록 커널 의존성 패키지를 먼저 컴파일해 주입해야 합니다. 

1. **사전 공구 라이브러리 빌드:** 
   우분투 터미널 창을 열고, 펌웨어 빌드를 뚫어낼 C언어 컴파일러 공구 상자를 먼저 때려 박습니다.
```bash
sudo apt-get update
sudo apt-get install virtualbox-guest-additions-iso
sudo apt install gcc make perl
```
2. **ISO CD 찔러넣기:** 
   VirtualBox 상단 메뉴바인 `Devices (장치)` 탭에서 `Insert Guest Additions CD image... (게스트 확장 CD 이미지 삽입)` 버튼을 클릭합니다. 바탕화면에 CD가 마운트 되면 실행하여 설치를 완료합니다.
3. **양방향 클립보드 터널 개방:** 
   VirtualBox 장치 탭 메뉴 -> `Shared Clipboard (클립보드 공유)` 와 `Drag and Drop (드래그 앤 드롭)` 설정을 **'Bidirectional (양방향)'** 으로 강제 전환시키면 윈도우와 리눅스가 한 몸처럼 마우스를 공유합니다.

---

## 2. 레드햇 기반(Rocky Linux / CentOS)의 특수 수술

기업용 인프라인 레드햇 클론(Rocky 리눅스) 환경은 우분투보다 보안이 폐쇄적이므로, 추가적인 확장 팩 아키텍처(epel-release)와 리눅스 심장 뼈대(kernel-headers)를 뽑아내야만 CD 코어 접근이 허용됩니다.

1. **사전 공구 라이브러리 빌드:**
```bash
sudo dnf update
sudo dnf install epel-release
sudo dnf install gcc make perl kernel-devel kernel-headers bzip2 dkms
```
2. 이후 우분투와 똑같이 상단 메뉴바에서 CD를 찔러 넣고 패키지를 설치한 후 양방향(Bidirectional) 세팅을 키면 완료 돱니다.

---

> **🚨 치명적 에러: CD 이미지가 마운트만 되고 무반응일 때**
> 
> 종종 리눅스 터미널이 권한 보안 문제로 CD 자동 실행(Autorun)을 차단해 먹통이 되는 경우가 흔합니다. 이때는 엔지니어가 수동으로 CD룸 깊숙이 걸어 들어가 강제로 심장 스크립트 실행 명령어를 주입해야 합니다.
> 
> ```bash
> # 1. 무적의 root 권한 탈취
> sudo su
> 
> # 2. CD가 장착된 드라이브 위치를 전수 스캔 (경로 탐색)
> mount | grep -i vbox
> 
> # 3. 찾아낸 궤도(/media/cdrom0)로 돌진해 .run 컴파일러 파일 수동 강제 실행
> sh /media/cdrom0/VBoxLinuxAdditions.run
> 
> # 4. 패치 직후 강제 우주 폭발 재부팅
> reboot
> ```
