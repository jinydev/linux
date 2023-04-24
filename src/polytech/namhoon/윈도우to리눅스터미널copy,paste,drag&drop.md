---
layout : home
---

# 윈도우 <-> 리눅스 터미널 Copy, Paste및 D&D





## 1. 우분투 리눅스

1. ![](https://www.manualfactory.net/wp-content/uploads/%EB%B2%84%EC%B6%94%EC%96%BC%EB%B0%95%EC%8A%A4-%ED%8C%8C%EC%9D%BC-%EC%A0%84%EC%86%A1-07.png)
   sudo Guest Additions가 설치된 후, VirtualBox의 메뉴에서 'Devices' -> 'Insert Guest Additions CD image...'를 선택하여 가상 CD-ROM에 Guest Additions ISO 파일을 마운트하고, CD-ROM을 실행하여 설치를 완료합니다.
   
2. Ubuntu에서 다음 명령어를 사용하여 Guest Additions를 설치해 보세요:

```
sudo apt-get update
sudo apt-get install virtualbox-guest-additions-iso
sudo apt install gcc make perl
```

3. 다시 sudo Guest Additions가 설치된 후, VirtualBox의 메뉴에서 'Devices' -> 'Insert Guest Additions CD image...'를 선택하여 가상 CD-ROM에 Guest Additions ISO 파일을 마운트하고, CD-ROM을 실행하여 설치를 완료합니다.
   

4.  ![](https://www.manualfactory.net/wp-content/uploads/%EB%B2%84%EC%B6%94%EC%96%BC%EB%B0%95%EC%8A%A4-%ED%8C%8C%EC%9D%BC-%EC%A0%84%EC%86%A1-01.png)
   이제 호스트 OS와 게스트 OS 사이의 클립 보드 공유 설정을 확인하십시오. VirtualBox의 'Settings' -> 'General' -> 'Advanced' -> 'Shared Clipboard' 설정이 'Bidirectional'로 설정되어 있는지 확인하십시오.

![](https://www.manualfactory.net/wp-content/uploads/%EB%B2%84%EC%B6%94%EC%96%BC%EB%B0%95%EC%8A%A4-%ED%8C%8C%EC%9D%BC-%EC%A0%84%EC%86%A1-03.png)

가상머신 메뉴에서 설정할 수도 있습니다. 게스트 실행 창의 장치 메뉴에 클립보드 공유와 드래그 앤 드롭을 설정하는 메뉴가 있습니다.

![](https://www.manualfactory.net/wp-content/uploads/%EB%B2%84%EC%B6%94%EC%96%BC%EB%B0%95%EC%8A%A4-%ED%8C%8C%EC%9D%BC-%EC%A0%84%EC%86%A1-04.png)

설정을 마치고 나면, 파일을 드래그하여 복사할 수 있습니다.

![](https://www.manualfactory.net/wp-content/uploads/%EB%B2%84%EC%B6%94%EC%96%BC%EB%B0%95%EC%8A%A4-%ED%8C%8C%EC%9D%BC-%EC%A0%84%EC%86%A1-05.png)



## 2. 록키 리눅스

1. sudo Guest Additions가 설치된 후, VirtualBox의 메뉴에서 'Devices' -> 'Insert Guest Additions CD image...'를 선택하여 가상 CD-ROM에 Guest Additions ISO 파일을 마운트하고, CD-ROM을 실행하여 설치를 완료합니다.
   
2. 아래 명령어를 실행합니다.

```sql
sudo dnf update
sudo dnf install gcc make perl
sudo dnf install epel-release
sudo dnf install gcc make perl kernel-devel kernel-headers bzip2 dkms
```

3. 호스트 OS와 게스트 OS 사이의 클립 보드 공유 설정을 확인하십시오. VirtualBox의 'Settings' -> 'General' -> 'Advanced' -> 'Shared Clipboard' 설정이 'Bidirectional'로 설정되어 있는지 확인하십시오.
