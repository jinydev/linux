---
layout: home
title: "2. 필수 시스템 패키지 명령어 DNF"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 2. 필수 시스템 패키지 명령어 DNF

## 2. 필수 시스템 패키지 명령어 (DNF)

우분투 서버의 `apt` 문법 체계와 비교해보면 알파벳 단어만 바뀌었을 뿐 매커니즘은 매우 흡사합니다. (마찬가지로 최상위 관리자 권리인 `sudo`가 강제됩니다.)

### 2.1 서버 패키지 카탈로그 업데이트 (`update`)
```bash
sudo dnf update
# (apt update + apt upgrade 두 가지 명령어를 이 dnf 한 줄이 전부 흡수하여 처리해 줍니다!)
```

### 2.2 새 패키지 강력 설치 (`install`)
```bash
sudo dnf install 패키지이름
```

### 2.3 시스템에서 패키지 지우기 (`remove`)
```bash
sudo dnf remove 패키지이름
```

### 2.4 원하는 패키지가 있는지 창고에서 색출 (`search / info`)
```bash
# 창고에 nginx 서버용 파일이 존재하는지 이름으로 검색합니다
sudo dnf search nginx

# 다운받기 전에 그 패키지의 용량, 제작사 등 엄청 상세한 정보를 표출합니다.
sudo dnf info nginx
```

---


---

[⬅️ 이전](../)
