---
layout: home
---

# Rsync
Rsync는 데이터 동기화 및 백업 목적으로 사용되는 강력한 명령줄 도구입니다. 서로 다른 두 시스템 간에 파일과 디렉토리를 로컬 및 원격으로 동기화할 수 있습니다. Rsync는 원본 파일과 대상 파일 간의 차이만 전송하므로 네트워크를 통해 대용량 파일을 효율적으로 전송할 수 있습니다.

다음은 rsync를 사용하는 방법에 대한 몇 가지 기본 예입니다.

한 디렉터리에서 다른 디렉터리로 파일 복사:
한 디렉토리에서 다른 디렉토리로 파일을 복사하려면 다음 명령을 사용하십시오.

```bash
rsync -avh /path/to/source /path/to/destination
```
설명:

-a 옵션: 모든 파일 속성과 권한을 보존하는 아카이브 모드.
-v 옵션: 자세한 정보 표시 모드로 프로세스에 대한 자세한 정보를 표시합니다.
-h 옵션: 파일 크기를 보다 이해하기 쉬운 형식으로 표시하는 사람이 읽을 수 있는 출력.
예:

```bash
rsync -avh /home/user/documents/ /media/usb_drive/backups/documents/
```
이 명령은 /home/user/documents 디렉토리에서 /media/usb_drive/backups/documents 디렉토리로 모든 파일과 디렉토리를 복사합니다.

디렉토리 동기화:
두 디렉토리를 동기화하려면 다음 명령을 사용하십시오.

```bash
rsync -avh /path/to/source/ /path/to/destination/
```
설명:

소스 및 대상 디렉토리 뒤의 후행 슬래시는 rsync가 소스 디렉토리의 내용을 대상 디렉토리에 복사하도록 하는 데 중요합니다.
예:

```bash
rsync -avh /home/user/documents/ /media/usb_drive/backups/documents/
```
이 명령은 /home/user/documents 디렉토리의 내용을 /media/usb_drive/backups/documents 디렉토리와 동기화합니다.

SSH를 통해 파일 전송:
SSH를 통해 파일을 전송하려면 다음 명령을 사용하십시오.

```bash
rsync -avh -e ssh user@remote_host:/path/to/source /path/to/destination
```
설명:

-e ssh 옵션: 원격 파일 전송에 SSH 프로토콜 사용을 지정합니다.
```bash
user@remote_host:/path/to/source: 원격 시스템의 소스 디렉토리.
```
예:

```bash
rsync -avh -e ssh user@192.168.1.100:/home/user/documents/ /media/usb_drive/backups/documents/
```
이 명령은 IP 주소가 192.168.1.100인 원격 시스템의 /home/user/documents 디렉토리에서 로컬 시스템의 /media/usb_drive/backups/documents 디렉토리로 모든 파일과 디렉토리를 전송합니다.

이것은 rsync를 사용하는 방법에 대한 몇 가지 예일 뿐입니다. rsync의 다양한 옵션 및 기능에 대한 자세한 내용은 터미널에 man rsync를 입력하여 rsync 매뉴얼 페이지를 참조할 수 있습니다.