---
layout: home
---

# Go
리눅스에 Go를 설치하려면 다음과 같은 단계를 따르면 됩니다.

## Go 다운로드하기
Go 공식 웹사이트에서 Linux용 Go 바이너리를 다운로드합니다. 다운로드 페이지는 https://golang.org/dl/ 에서 확인할 수 있습니다. 최신 버전의 경우, 예를 들어 Go 1.16.3 버전을 다운로드할 경우 아래와 같은 명령어를 실행합니다.

```
wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz

```

## 압축 해제하기
다운로드한 Go 바이너리 파일을 압축 해제합니다. 아래와 같은 명령어를 실행합니다.  

```
tar -xvf go1.16.3.linux-amd64.tar.gz
```

## 설치 경로 설정하기
Go 바이너리 파일을 /usr/local 디렉토리에 설치하기로 합니다. 다음과 같은 명령어를 실행하여 /usr/local/go 디렉토리를 생성합니다.  
```
sudo chown -R root:root ./go
sudo mv go /usr/local
```

## 환경 변수 설정하기
Go 바이너리를 사용하기 위해 PATH와 GOPATH 환경 변수를 설정합니다. PATH는 Go 바이너리를 실행할 수 있도록, GOPATH는 Go 프로젝트를 저장할 경로를 지정합니다. ~/.profile 파일을 열어 아래와 같은 내용을 추가합니다.

```
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin

```

변경한 환경 변수를 적용하기 위해 다음 명령어를 실행합니다.

```
source ~/.profile
```

## 설치 확인하기
설치가 제대로 되었는지 확인하기 위해 아래 명령어를 실행합니다.

```
go version
```

위와 같이 간단한 단계를 따르면 리눅스에 Go를 설치할 수 있습니다.