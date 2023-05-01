---
layout: home
---

# __Zabbix__
## 0428. Zabbix에 대한 설명
![1](./images/zabbix.png)

> ### Zabbix는 네트워크, 서버, 애플리케이션, 데이터베이스, 클라우드 인프라 등 다양한 **IT 인프라를 모니터링**할 수 있는 오픈 소스 소프트웨어

- Zabbix는 데이터 수집, 처리, 분석, 알림 및 보고서 작성 등의 기능을 제공하여 IT 인프라의 **성능, 가용성, 안정성**을 지속적으로 모니터링하고 개선할 수 있도록 도와줌

- Zabbix는 **클라이언트-서버 모델로 구성**되며, 에이전트 또는 SNMP 등의 프로토콜을 사용하여 모니터링 대상에서 데이터를 수집함. 
- Zabbix 서버는 **수집된 데이터를 처리하고 분석**하여 대시보드, 그래프, 보고서 등으로 **시각화**함. 또한, 사용자가 지정한 기준에 따라 이상 징후를 감지하고, 이상 **징후가 발생하면 알림을 보내서 사용자가 즉각적으로 대응**할 수 있도록 함.

    1. Zabbix는 다양한 **모니터링 기능**을 제공.   

        -> 예를 들어, 서버와 네트워크 성능 모니터링, 서버와 애플리케이션 상태 모니터링, 로그 분석 및 이상 징후 감지, 클라우드 인프라 모니터링, 데이터베이스 성능 모니터링 등이 있음.    
    또한, 사용자가 직접 모니터링 대상을 정의하고, 사용자 정의 템플릿을 사용하여 모니터링 대상을 구성할 수 있음.

    2. Zabbix는 **대규모 IT 인프라에서의 모니터링에 적합**함.   

        -> Zabbix는 대용량 데이터를 처리하는 데 특화된 데이터베이스를 사용하며, 분산 모니터링 아키텍처를 지원하여 여러 대의 Zabbix 서버를 사용하여 모니터링 대상을 분산 처리할 수 있음. 
    또한, Zabbix는 대량의 데이터를 효율적으로 저장 및 조회하기 위한 기능을 제공합니다.

    3. Zabbix는 **오픈 소스 소프트웨어**로, 다양한 운영 체제와 데이터베이스를 지원. 

    4. 사용자는 Zabbix의 **소스 코드를 직접 수정**하여 사용자의 요구 사항에 맞게 사용할 수 있음. 
    Zabbix는 많은 사용자 커뮤니티를 가지고 있으며, 커뮤니티에서는 다양한 문제 해결 방법과 정보를 제공함.   

- 가상환경 우분투 버전은 22로 해야 함

```linux
sudo wget https://repo.zabbix.com/zabbix/6.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.4-1+ubuntu22.04_all.deb
sudo dpkg -i zabbix-release_6.4-1+ubuntu22.04_all.deb
sudo apt update

sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent
sudo apt install mysql-server
```

```mysql
mysql -uroot -p
mysql> create database zabbix character set utf8mb4 collate utf8mb4_bin;
mysql> create user zabbix@localhost identified by 'password';
mysql> grant all privileges on zabbix.* to zabbix@localhost;
mysql> set global log_bin_trust_function_creators = 1;
mysql> quit;
```
```linux
sudo zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix
sudo mysql -uroot -p
```

```mysql
mysql> set global log_bin_trust_function_creators = 0;
mysql> quit;
```
```linux
sudo vim /etc/zabbix/zabbix_server.conf
DBPassword=password

sudo systemctl restart zabbix-server zabbix-agent apache2
sudo systemctl enable zabbix-server zabbix-agent apache2
```

- GUI 접속   
    1. 가상머신 : localhost/zabbix    
    내 pc : 192.168.56.200/zabbix    
    2. port 3306   
    user zabbix   
    password password   

![1](./images/zabbixlogin.png)

에러나면
```linux
mysql -uroot -p
password
drop database zabbix;
drop user 'zabbix'@'localhost';
```