---
layout: home
---

# Nginx 설치(Yum)
centos linux에서는 yum을 통하여 Nginx를 설치할 수 있습니다.

## 준비작업 및 패키지 검색
루트 사용자로 로그인하거나 다음 명령을 실행하여 루트 사용자로 전환합니다.

```bash
sudo su -
```
다음 명령을 실행하여 패키지 목록을 업데이트합니다.

```bash
yum update
```



## 패키지 설치
Linux yum 명령을 통해 Nginx를 설치하려면 다음 단계를 따르십시오.

### 설치
yum install 명령어를 이용해서 설치해 줍니다. 

```
yum install -y nginx
```
설치 프로세스가 완료될 때까지 기다리십시오.

### Nginx 목록 경로 추가 설정
최신 또는 특정 버젼의 Nginx를 설치하기 위해서는 적절한 저장소의 위치를 추가 설정해 주는 것도 좋습니다. 

```
sudo vi /etc/yum/repos.d/nginx.repo
```

nginx repository 생성하기 위해서는 다음과 같이 내용을 수정합니다.

```
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```


## Nginx 데몬 실행
설치가 완료되면 다음 명령을 사용하여 Nginx 서비스를 시작합니다.

```
systemctl start nginx
```

다음 명령을 실행하여 Nginx의 상태를 확인합니다.

```bash
systemctl status nginx
```

상태가 Nginx가 실행 중이라고 표시되면 yum 명령을 사용하여 Linux 시스템에 Nginx를 성공적으로 설치한 것입니다.