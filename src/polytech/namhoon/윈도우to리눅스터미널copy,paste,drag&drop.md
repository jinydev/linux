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



# cf) 만약!! CD image가 실행이 안 되면?

만약!!!!!!! 여기서 CD 이미지가 마운트는 되는데 실행이 안되면!!

터미널에서 강제로 실행해줘야합니다.

게스트 확장 CD 이미지를 삽입하면, 게스트 운영 체제에서 해당 CD를 자동으로 마운트하고 설치 프로그램을 실행해야 합니다. 그러나 이미지가 마운트되었지만 실행되지 않는 경우, 다음 단계를 시도해 보세요.

1. 마운트된 CD 이미지를 열고 실행 파일을 찾습니다. 일반적으로 VBoxLinuxAdditions.run이라는 파일 이름으로 불리는 것을 찾을 수 있습니다.

2. 터미널 창을 열고, root 사용자 권한을 부여합니다. 이는 일반 사용자 권한으로는 실행되지 않는 명령어를 실행할 수 있도록 해줍니다.

   ```
   Copy code
   sudo su
   ```

3. VBoxLinuxAdditions.run 파일을 실행합니다.

   ```
   arduinoCopy code
   sh /media/cdrom/VBoxLinuxAdditions.run
   ```

   여기서 "/media/cdrom" 경로는 이미지가 마운트된 위치에 따라 달라질 수 있습니다.

4. 설치가 완료되면 게스트 운영 체제를 다시 시작합니다.

   ```
   Copy code
   reboot
   ```

이렇게 하면 VirtualBox 게스트 확장 CD가 설치되어야 합니다. 그러나 이 방법이 작동하지 않으면, VBoxGuestAdditions.iso 파일을 수동으로 다운로드하고 마운트하여 설치해 보십시오. 이 파일은 VirtualBox 설치 폴더의 "VBoxGuestAdditions.iso" 경로에 있습니다.

다음은 다운로드한 VBoxGuestAdditions.iso 파일을 마운트하는 방법입니다.

1. VirtualBox에서 가상 머신을 종료합니다.

2. VBoxGuestAdditions.iso 파일을 다운로드하고 파일을 저장합니다.

3. VirtualBox를 열고 해당 가상 머신을 선택한 다음, 설정(S)를 클릭합니다.

4. 저장소(R) 탭에서 아래쪽의 CD 아이콘을 클릭하고 "VBoxGuestAdditions.iso" 파일을 선택합니다.

5. 마운트(M) 확인란을 선택하고, 확인(O)을 클릭합니다.

6. 가상 머신을 시작하고, CD가 자동으로 마운트되지 않으면 다음 명령을 터미널에서 실행합니다.

   ```
   bashCopy code
   sudo mount /dev/cdrom /mnt
   ```

7. 마운트된 CD에서 VBoxLinuxAdditions.run 파일을 실행합니다.

   ```
   arduinoCopy code
   sudo sh /mnt/VBoxLinuxAdditions.run
   ```

8. 설치가 완료되면 가상 머신을 다시 시작합니다.

   ```
   Copy code
   sudo reboot
   ```

이제 VirtualBox 게스트 확장 CD가 설치되었는지 확인해 보세요.

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2738%27%20height=%2738%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2738%27%20height=%2738%27/%3e)

sh /media/cdrom/VBoxLinuxAdditions.run

cannot open : No such file이래

만약 "cannot open : No such file" 에러가 발생한다면, 아마도 마운트된 CD 이미지가 다른 위치에 있을 수 있습니다. 다음 명령어를 실행하여 현재 마운트된 CD 이미지의 경로를 확인해 보십시오.

```
cssCopy code
sudo mount | grep -i vbox
```

위 명령어는 현재 마운트된 CD 이미지를 확인하고, 해당 CD 이미지에 대한 정보를 출력합니다. 일반적으로 이 명령어는 다음과 같은 결과를 출력합니다.

```
bashCopy code
/dev/sr0 on /media/cdrom0 type iso9660 (ro,nosuid,nodev,relatime,nojoliet,check=s,map=n,blocksize=2048)
```

이 경우, 마운트된 CD 이미지의 경로는 "/media/cdrom0" 입니다. 그러나 결과가 다르다면, 출력된 경로를 사용하십시오.

따라서 다음 명령어를 실행하여 VBoxLinuxAdditions.run 파일을 실행하십시오.

```
arduinoCopy code
sudo sh /media/cdrom0/VBoxLinuxAdditions.run
```

그리고 가상머신을 다시 시작합니다.

```
Copy code
sudo reboot
```

이제 VirtualBox 게스트 확장 CD가 설치되었는지 확인해 보십시오.
