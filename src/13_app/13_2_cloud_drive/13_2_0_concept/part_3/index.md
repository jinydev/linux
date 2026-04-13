---
layout: home
title: "3. Nextcloud 다운로드 및 배치"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 3. Nextcloud 다운로드 및 배치

## 3. Nextcloud 다운로드 및 배치

공식 홈페이지에서 아카이브 압축 파일을 다운로드하여 웹 서버 경로(`DocumentRoot`)로 이동시킵니다.

```bash
# wget으로 최신 zip/tar 형태의 릴리즈 다운로드
wget https://download.nextcloud.com/server/releases/latest.zip

# 압축 해제
unzip latest.zip

# 아파치 루트 디렉토리(/var/www/html)로 폴더 이동
sudo mv nextcloud /var/www/html/

# (중요) 웹 서버 데몬이 파일들을 수정/저장할 수 있도록 소유권(chown) 전부 위임!
sudo chown -R apache:apache /var/www/html/nextcloud
```
> [!CAUTION] 
> 소유권(`chown`) 변경을 생략하면, 브라우저에서 접속 시 디렉토리 쓰기 불가능 에러로 인해 설치 화면이 뜨지 않습니다.

---


---

[⬅️ 이전](../)
