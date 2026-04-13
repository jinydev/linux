---
layout: home
title: "관련 명령어와의 차이점"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 관련 명령어와의 차이점

## 관련 명령어와의 차이점

### whoami vs who vs id

```console
# whoami - 현재 사용자명만 출력
hojin@DESKTOP-11LMH3B:~$ whoami
hojin

# who - 현재 로그인한 모든 사용자 정보 출력
hojin@DESKTOP-11LMH3B:~$ who
hojin    :0           2020-05-21 15:30 (:0)
hojin    pts/0        2020-05-21 15:31 (:0)

# id - 사용자 ID와 그룹 정보 출력
hojin@DESKTOP-11LMH3B:~$ id
uid=1000(hojin) gid=1000(hojin) groups=1000(hojin),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare)
```

### 비교 표

| 명령어 | 출력 내용 | 용도 |
|--------|-----------|------|
| `whoami` | 현재 사용자명만 | 현재 사용자 확인 |
| `who` | 로그인 세션 정보 | 로그인된 사용자 목록 |
| `id` | 사용자 ID와 그룹 | 상세한 사용자 정보 |


---

[⬅️ 이전](../)
