1. 포그라운드와 백그라운드 처리
    
    <img src = "https://file.notion.so/f/s/d4999fed-38a6-4d95-98a1-624949603048/img1.daumcdn.png?id=7288e450-ad48-48f7-935f-dca55c91993e&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660373800&signature=5VqRk6DK6YZYofkS7waj-MfV04K1UDUTmCqe0MK-97U&downloadName=img1.daumcdn.png">
    
    1. 포그라운드
        1. 사용자가 명령을 입력하고 실행 결과를 바로 확인할 수 있는 프로세스
        2. 포그라운드에서 실행 중인 프로세스가 완료되기 전에는 다른 명령을 입력할 수 없음
    2. 백그라운드(Background)
        1. 사용자가 실행한 명령을 백그라운드에서 실행하는 프로세스
        2. 백그라운드에서 실행 중인 프로세스는 사용자가 다른 명령을 입력할 수 있으며, 실행 결과는 나중에 확인할 수 있음
        3. 백그라운드에서 실행할 때는 명령어 뒤에 & 기호를 붙여주면 작업 번호와 PID를 출력한 후 명령을 실행한 다음 명령을 입력받을 수 있는 대기 상태가 됨
        4. 키보드의 입력 없이 프로세스를 장시간 실행해야하는 경우에 사용하는 방법
        5. 시스템 부팅 시에 동작하는 대부분의 프로세스들은 이러한 백그라운드 방식으로 동작
        6. 백그라운드로 동작하는 프로세스는 kill 명령어를 사용하여 종료 가능
2. 프로세스 스케줄러
    
    <img src ="https://file.notion.so/f/s/eea8ac68-282d-4d9b-8bd4-f9334709827f/image.png?id=87857aff-85ef-4876-9a60-421333da8f77&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660393015&signature=xZLUaZ-qt82PN7tBO16v3H6RF3tfdMDUqj5vibPlS44&downloadName=image.png">
    
    1. 프로세스 스케줄러(Process Scheduler)는 CPU 자원을 여러 프로세스가 공유하면서 프로세스를 스케줄링하는 역할
    2. 스케줄링 방식에는 라운드 로빈(Round Robin), 우선순위(Priority), 멀티레벨 큐(Multi-Level Queue) 등이 있음
        
        <img src="https://file.notion.so/f/s/578dfe40-57ef-4cd1-8466-f97b290f25cb/image.png?id=a4b06230-481e-46c3-938c-930c435d3995&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660414110&signature=6gcthivw2HAejxhfCLaA1gphsFb6duz1NN-OmGo7LZQ&downloadName=image.png">
        
        <img src="https://file.notion.so/f/s/8af21792-7024-4703-b11a-f3711937a0d6/image.png?id=728bc2ec-fcac-4390-84a2-9b148efd0720&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660424312&signature=MT8a7MkBx1kEWBCR5CIitI9MxB7OPAL_l4lXh4nQWzU&downloadName=image.png">
        
        <img src="https://file.notion.so/f/s/c528175f-6f98-4663-927d-532784f70a82/image.png?id=0d5afa20-d8ff-46cb-82c0-e1ac2107be4e&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660433534&signature=U6weMfnnb0fFCRjl8wrJmXmVXWAN9enqrctWlO61b90&downloadName=image.png">
        
        - 운영체제는 스케줄링 큐에서 대기하는 각 프로세스들의 우선순위를 고려하여 자원을 배분
            - 스케줄링 큐: 프로세스들이 대기하는 공간 , 반드시 선입선출 방식은 아님
            
3. 시작 프로그램 처리
    1. 리눅스에서 시작 프로그램(Startup Program)은 시스템 부팅 시 자동으로 실행되는 프로그램을 말함
    2. 시작 프로그램은 시스템 설정 파일에 등록되어 있으며, 설정 파일을 수정하여 시작 프로그램을 추가하거나 삭제할 수 있음
    3.  대표적인 시작 프로그램 설정 파일
        - /etc/rc.local
        - /etc/init.d/
        - /etc/systemd/system/

시작 프로그램을 추가하거나 삭제할 때는 해당 설정 파일을 수정하여 등록 또는 삭제합니다. 등록된 시작 프로그램은 시스템 부팅 시 자동으로 실행됩니다.