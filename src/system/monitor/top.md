---
layout: home
---

# Top 명령어

## 첫번째줄
최상위 명령의 첫 번째 줄은 현재 시간, 시스템 실행 시간, 현재 로그인한 사용자 수, 지난 1, 5, 15 동안의 시스템 로드 평균을 포함하여 시스템 성능에 대한 일반 정보를 표시합니다. 

### 업타임
첫번째줄의 앞부분은 현재의 시간과 리눅스의 업타임을 의미 합니다.


### 평균부하
부하 평균은 각각 쉼표로 구분된 세 개의 값으로 표시됩니다. 이러한 값은 실행 가능한 상태에 있거나 지정된 시간 동안 입력/출력 작업이 완료되기를 기다리는 평균 프로세스 수를 나타냅니다.


예를 들어 1분 동안 로드 평균이 0.5라는 것은 평균적으로 해당 1분 간격 동안 실행을 대기하거나 입력/출력 작업이 완료되기를 기다리는 프로세스가 0.5개라는 의미입니다. 5분 동안 로드 평균 2.0은 평균적으로 5분 간격 동안 실행 대기 중이거나 입력/출력 작업 완료를 대기 중인 프로세스가 2.0개임을 의미합니다.


로드 평균은 시스템 사용량과 높은 수요로 인해 성능 문제가 발생할 수 있는지 여부를 나타내는 유용한 지표가 될 수 있습니다.


## CPU 리소스 확인
 top 명령어에서 보이는 각각의 항목은 다음과 같습니다.

* us (User Time) : 사용자 모드에서 실행된 CPU 사용 시간입니다.
* sy (System Time) : 시스템 모드에서 실행된 CPU 사용 시간입니다.
* ni (Nice Time) : nice 값이 높은 프로세스가 사용한 CPU 시간입니다.
* id (Idle Time) : CPU가 아무 작업도 하지 않고 대기한 시간입니다.
* wa (I/O Wait Time) : I/O 작업을 대기하면서 CPU를 사용하지 않은 시간입니다.
* hi (Hardware IRQ Time) : 하드웨어 인터럽트를 처리하는데 사용된 CPU 시간입니다.
* si (Software Interrupt Time) : 소프트웨어 인터럽트를 처리하는데 사용된 CPU 시간입니다.
* st (Stolen Time) : 가상머신(VM)에서 실행되는 경우 호스트 시스템에서 해당 가상머신의 CPU 자원을 빼앗아 사용한 시간입니다.

이들은 CPU 사용률을 파악하는데 도움을 줍니다. 사용자 모드에서 실행된 시간(us)이 많다면 사용자 프로세스가 CPU를 많이 사용하는 것을 의미합니다. 반면, 시스템 모드에서 실행된 시간(sy)이 많다면, 커널의 시스템 호출이 많은 것을 의미합니다. nice 값이 높은 프로세스가 많은 CPU 시간(ni)을 사용한다면, 해당 프로세스들은 낮은 우선순위를 갖고 있는 것입니다. I/O 대기 시간(wa)이 많다면, I/O가 병목현상을 일으키고 있는 것입니다. 하드웨어 인터럽트(hi)와 소프트웨어 인터럽트(si) 시간은 각각 하드웨어와 소프트웨어의 인터럽트 처리에 소요된 CPU 시간입니다. 마지막으로, 가상머신에서 실행 중인 경우 가상머신의 CPU 자원을 호스트 시스템이 빼앗아 사용한 시간(st)을 표시합니다.