---
layout: home
---

# 스케쥴 알고리즘
스케줄러는 CPU 자원을 효율적으로 사용하기 위해 다양한 알고리즘을 사용합니다. 
알고리즘을 사용하여 프로세스들에게 적절한 CPU 시간 할당을 결정하며, 이를 통해 시스템의 성능과 안정성을 향상시킵니다.

## 알고리즘의 종류
일반적으로 사용되는 스케줄링 알고리즘으로는 Round Robin, Priority Scheduling, Shortest Job First 등이 있습니다.  

* Round Robin
* Priority Scheduling
* Shortest Job First

## 알고리즘의 변경
리눅스에서는 스케줄링 알고리즘을 변경할 수 있는 다양한 방법도 제공합니다. 예를 들어, `/proc/sys/kernel/sched_` 계열의 파일들을 조정하여 스케줄링 알고리즘을 변경할 수 있습니다. 이 외에도, 리눅스 커널의 컴파일 시에 커널 소스코드를 수정하여 사용자 정의 스케줄링 알고리즘을 구현할 수도 있습니다.
