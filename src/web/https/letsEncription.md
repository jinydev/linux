---
layout: home
---

# letsEncription
Ubuntu에 Let's Encrypt를 설치하는 단계는 다음과 같습니다.

## 준비사항
다음 명령을 실행하여 패키지 목록을 업데이트합니다.

```bash
sudo apt-get update
```

## Certbot 설치
Certbot Let's Encrypt 클라이언트를 설치합니다.

```bash
sudo apt-get install certbot
```

다음 명령을 실행하여 Certbot이 올바르게 설치되었는지 확인합니다.

```bash
sudo certbot --version
```

Certbot 사용 방법을 선택합니다. 예를 들어 Certbot을 사용하여 Apache용 인증서를 얻고 설치하려면 다음 명령을 실행합니다.

```bash
sudo certbot --apache
```

프롬프트에 따라 필요한 정보를 제공하고 인증서를 구성합니다.

인증서가 설치되면 HTTPS를 사용하여 웹 사이트를 방문하여 올바르게 작동하는지 확인할 수 있습니다. 브라우저의 주소 표시줄에 녹색 자물쇠 아이콘이 표시되어야 합니다.

