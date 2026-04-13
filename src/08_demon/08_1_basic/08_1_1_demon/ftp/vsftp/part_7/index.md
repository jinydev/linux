---
layout: home
title: "계정별 접속"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 계정별 접속

## 계정별 접속
특정 계정을 사용하여 vsftpd에 대한 액세스를 허용하려면 다음 단계를 수행해야 합니다.

* FTP 서버에 액세스하는 데 사용할 새 시스템 사용자 계정을 만듭니다. "adduser" 명령을 사용하여 새 사용자를 만들 수 있습니다. 예를 들면 다음과 같습니다.

```bash
sudo adduser ftpuser
```

* `passwd` 명령을 사용하여 새 사용자 계정의 암호를 설정합니다.

```bash
sudo passwd ftpuser
```

* 인증에 로컬 사용자 계정을 사용하도록 vsftpd를 구성합니다. 이는 vsftpd 구성 파일(/etc/vsftpd.conf)에 다음 줄을 추가하여 수행할 수 있습니다.

```bash
local_enable=YES
```

* 선택적으로 사용자를 자신의 홈 디렉토리로 chroot하도록 vsftpd를 구성할 수도 있습니다. 이렇게 하면 FTP 서버에 대한 액세스가 자신의 홈 디렉토리로만 제한됩니다. 이는 vsftpd 구성 파일에 다음 줄을 추가하여 수행할 수 있습니다.

```bash
chroot_local_user=YES
allow_writeable_chroot=YES
```

* vsftpd 서비스를 다시 시작하여 변경 사항을 적용합니다.
```bash
sudo systemctl restart vsftpd
```

이 단계를 완료한 후 새 사용자 계정과 설정한 암호를 사용하여 vsftpd 서버에 연결할 수 있어야 하며 사용자는 홈 디렉토리로 제한됩니다(chrooting이 활성화된 경우).

---

[⬅️ 이전: vsftpd](../ubuntu-vsftp/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../../) &nbsp;|&nbsp; [다음: 메일 ➡️](../../mail/)


---

[⬅️ 이전](../)
