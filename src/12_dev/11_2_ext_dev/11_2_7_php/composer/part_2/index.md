---
layout: home
title: "설치하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 설치하기

## 설치하기
다운로드 받은 컴포터 파일을 설치합니다.

```
php -r "if (hash_file('sha384', 'composer-setup.php') === '756890a4488ce9024fc62c56153228907f1545c228516cbf63f885e036d37e9a59d27d63f46af1d4d07ee0f76181c7d3') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
```

설치를 진행합니다.

```
php composer-setup.php 
```

설치후, 기존 설치파일은 제거 합니다.
```
php -r "unlink('composer-setup.php');"
```

<br>


---

[⬅️ 이전](../)
