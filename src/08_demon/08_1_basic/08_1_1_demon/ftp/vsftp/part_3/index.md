---
layout: home
title: "anonymous"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# anonymous

## anonymous 
익명 사용자의 접속 및 파일 업로드를 허용하도록 설정하기.  

```bash
sudo /etc/vsftpd.conf
```
vi 에디터로 `/etc/vsftpd.conf` 파일 열기, anonymous 계정의 권한 변경

```ini
anonymous_enable=YES #25
write_enable=YES # 31
anon_upload_enable=YES # 40
anon_mkdir_write_enable=YES # 44
```

한글폴더 폴기 허용
```ini
utf8_filesystem=YES
```

### 패시브 모드
기본적으로 `vsftpd`는 데이터 전송에 `패시브` 모드를 사용합니다. 클라이언트가 수동 모드를 사용하도록 구성되지 않은 경우 서버와의 데이터 연결을 설정할 수 없어 파일 목록이 표시되지 않을 수 있습니다. 수동 모드를 사용하도록 클라이언트를 구성하거나 vsftpd 구성 파일(/etc/vsftpd.conf)에 다음 줄을 추가하여 vsftpd에서 활성 모드를 활성화할 수 있습니다.

```bash
pasv_enable=NO
```

### 익명 폴더
anonymous로 접속되는 기본 디렉터리는 `/srv/ftp` 
이 디렉터리 안에 `pub 디렉터리`를 만들고 모든 사용자의 `읽기`, `쓰기` 권한 허용합니다.

```bash
cd /srv/ftp
mkdir pub
chmod 777 pub
```

### 재시작
변경된 설정을 적용하기 위하여 vsftpd 데몬을 재시작 합니다.
```bash 
sudo systemctl restart vsftpd
sudo systemctl enable vsftpd
```

vsftpd 데몬이 정상적으로 실행되고 있는지 확인합니다.  

```bash
systemctl status vsftpd 
```


---

[⬅️ 이전](../)
