---
layout: home
---

# 리눅스에 도커 설치하기
도커(Docker)는 리눅스에서 컨테이너 기반의 가상화 기술을 제공하는 오픈소스 프로젝트입니다. 도커를 설치하는 방법은 다음과 같습니다.

* 운영체제 업데이트: 최신 버전의 패키지를 설치하기 위해 우분투를 포함한 리눅스 배포판의 패키지 관리자를 업데이트합니다.

```bash
sudo apt-get update
```

* 도커 패키지 저장소 추가: 도커 패키지를 다운로드할 수 있는 도커 공식 패키지 저장소를 추가합니다.

```bash
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

* 도커 설치: 도커 패키지를 설치합니다.
```bash
sudo apt-get update
sudo apt-get install docker-ce
```

* 도커 실행: 도커를 실행하고, 자동으로 부팅시에도 도커가 실행되도록 합니다.
```bash
sudo systemctl start docker
sudo systemctl enable docker
```
