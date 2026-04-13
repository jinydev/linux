---
layout: home
---

# 부하 테스트
리눅스에서 웹서버의 부하를 테스트하는 방법은 다양합니다. 

## Apache Bench (ab)
Apache Bench (ab)는 아파치 웹 서버에서 제공하는 툴로, 여러 클라이언트에서 동시에 웹서버에 요청을 보내는 테스트를 할 수 있습니다. 아래 명령어를 이용하여 설치할 수 있습니다.  

```bash
sudo apt-get install apache2-utils
```
사용 예시는 다음과 같습니다.

```bash
ab -n 1000 -c 100 http://localhost/
```
위 명령어는 1000개의 요청을 100개의 클라이언트에서 동시에 보내는 테스트를 수행합니다.

```bash
poly@u22d:~$ ab -n 1000 -c 100 http://localhost/
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.18.0
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        3875 bytes

Concurrency Level:      100
Time taken for tests:   10.696 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      4428000 bytes
HTML transferred:       3875000 bytes
Requests per second:    93.49 [#/sec] (mean)
Time per request:       1069.611 [ms] (mean)
Time per request:       10.696 [ms] (mean, across all concurrent requests)
Transfer rate:          404.28 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.0      0       5
Processing:    54 1014 189.8   1015    1391
Waiting:       49 1014 189.8   1014    1391
Total:         56 1015 189.0   1015    1391

Percentage of the requests served within a certain time (ms)
  50%   1015
  66%   1038
  75%   1059
  80%   1091
  90%   1223
  95%   1306
  98%   1341
  99%   1358
 100%   1391 (longest request)
```

Apache Bench (ab) 테스트를 수행할 때, 테스트 대상 URL에는 IP 주소 또는 도메인 이름을 지정할 수 있습니다. 이를 이용하여 다른 IP 주소를 가진 서버를 테스트할 수 있습니다.

예를 들어, 다음과 같은 명령어를 사용하여 특정 IP 주소를 가진 서버를 대상으로 1000개의 요청을 100개의 클라이언트에서 동시에 보내는 테스트를 수행할 수 있습니다.

```bash
ab -n 1000 -c 100 http://123.45.67.89/
```
위 명령어에서 "http://123.45.67.89/" 부분은 테스트 대상의 URL을 나타내며, 실제 서버의 IP 주소로 변경하여 사용하면 됩니다.

또한, 테스트 대상 서버의 포트 번호가 기본값인 80번이 아닌 경우에는 "-p" 옵션을 사용하여 포트 번호를 지정할 수 있습니다. 예를 들어, 포트 번호가 8080인 서버를 테스트하는 경우에는 다음과 같은 명령어를 사용할 수 있습니다.

```bash
ab -n 1000 -c 100 http://123.45.67.89:8080/
```
위와 같이 IP 주소와 포트 번호를 지정하여 Apache Bench (ab)를 이용하면, 해당 서버의 부하를 테스트할 수 있습니다.


## Siege
Siege는 웹 서버를 공격하는 스트레스 테스트 도구 중 하나입니다. 아래 명령어를 이용하여 설치할 수 있습니다.
```bash
sudo apt-get install siege
```
사용 예시는 다음과 같습니다.

```bash
siege -c 100 -r 10 http://localhost/
```
위 명령어는 100개의 클라이언트에서 10회의 반복을 수행하여 웹서버에 부하를 가하는 테스트를 수행합니다.

## JMeter
JMeter는 자바 기반의 웹 응용 프로그램의 성능을 테스트하는 도구 중 하나입니다. GUI 기반으로 동작하며, 다양한 기능을 제공합니다. 아래 링크를 참조하여 설치 및 사용 방법을 확인할 수 있습니다.
https://jmeter.apache.org/usermanual/get-started.html


