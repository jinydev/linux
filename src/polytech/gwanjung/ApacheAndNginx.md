---
layout: home
---
# Apache와 Nginx
차이점을 알아보자
## Apahche?
아파치 HTTP 서버(Apache HTTP Server)는 아파치 소프트웨어 재단에서 관리하는 무료 HTTP 웹 서버 소프트웨어다. 리눅스 등 유닉스 계열 뿐 아니라 마이크로소프트 윈도우에서도 무료로 운용할 수 있다. 프로그램의 이름은 httpd이다. 기본적인 작동 방법은 사용자의 HTTP 요청이 올 때마다 프로세스나 스레드를 새로 만든다.

### Apache 구동 방식

1. Prefork MPM 방식
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcbFKg7%2Fbtrr1NgUUcP%2FEsQYlUXqWvl6zdYtJpahC1%2Fimg.png)

- HTTP 연결 요청이 올 때마다 프로세스를 매번 복제하여 프로세스에서 싱글 스레드로 해당 HTTP 요청을 처리한다.
- 사용자 요청 수 = 프로세스 수

2. Worker MPM 방식
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbmzK3M%2Fbtrr1NaasvA%2Fmy4N0J0Hc0haYp8rVYfjP0%2Fimg.png)
한 개의 프로세스가 여러 스레드를 생성하여 해당 HTTP 요청을 처리하므로 Prefork 방식보다 메모리 소모가 적다. 하지만 멀티 스레드 방식은 CPU 스케줄링을 위한 처리 시간과 문맥 전환 비용이 발생하는 단점이 있다. 

## Nginx(비동기 이벤트 기반)?
Nginx는 웹 서버 소프트웨어로, Apache의 C10K 문제를 해결하고자 등장하였다. Nginx는 요청에 응답하기 위해 비동기 이벤트 기반 구조를 가진다. 이것은 아파치 HTTP 서버의 스레드/프로세스 기반 구조를 가지는 것과는 대조적이다.
Nginx의 비동기 이벤트란 HTTP 요청이 수 천 개여도 정해진 수의 프로세스(worker procss)가 이 요청들을 이벤트로 등록하고 비동기 방식으로 대기시켜 완료되는 요청(이벤트)부터 응답(처리)해주는 것을 말한다. 

### Nginx 구동 방식
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQRh8u%2FbtrsfWbzQPo%2FMRnkr4DxlZddNd08gukih0%2Fimg.png)\
NGINX에서는 커넥션 생성 및 커넥션 제거, 그리고 새로운 요청을 처리하는 것을 이벤트라고 부른다. 이 이벤트들은 OS커널이 큐 형식으로 worker 프로세스에게 전달해주고, 이벤트가 큐에 담긴 상태에서 worker 프로세스가 처리할 때까지 비동기 방식으로 대기한다. 그리고 워커 프로세스는 하나의 스레드로 이벤트를 꺼내서 처리해 나간다. 이렇게 되면 워커 프로세스가 쉴틈없이 일하기 때문에 아파치 서버에서 요청이 없다면 방치되던 프로세스보다 서버 자원을 더 효율적으로 쓸 수 있게 되는 것이다.

그러나 네모 칸(큐)에 있는 요청(이벤트) 중 하나가 시간이 오래걸리는 작업(ex. Disk I/O)이면 어떻게 될까?

그 뒤에 있는 이벤트는 요청을 처리하는 긴 시간동안 블로킹이 된다. 그래서 NGINX는 시간이 오래 걸리는 작업은 따로 수행하는 스레드 풀(Thread Pool)을 만들어놓고, 워커 프로세스는 지금 처리할 요청이 시간이 많이 걸릴 것 같다면 스레드 풀에 그 이벤트를 위임하고 큐 안에 있는 다른 이벤트를 처리하러 가게 된다.
