---
layout: home
---
## Bios란

**B**asic **I**nput/**O**utput **S**ystem의 약자로 운영체제의 가장 기본 소프트웨어이자 입출력을 처리하는 펌웨어

- 전원이 켜지면 실행이 시작되는 최초의 프로그램
- 하드웨어 부품을 초기화하고 검사하는 역할
    - *부트로더* 또는 대용량 저장장치에 저장된 운영체제를 RAM으로 읽어오는 기능 수행
    
    *부트로더*: os가 시동되기 전에 미리 실행되면서 커널이 올바르게 시동되기위해 필요한 모든 관련 작업을 마무리하고 최종적으로 운영체제를 시동시키기 위한 목적을 가진 프로그램
- 넓은 의미로는 하드웨어와 가장 낮은 수준에서 입출력을 담당하는 프로그램
- 바이오스 포스트(POST) 과정의 첫 단계
    
    ![Boot](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/POST_P5KPL.jpg/1280px-POST_P5KPL.jpg)
    

### 부팅

PC가 켜진 후에 OS가 실행되기 전까지 수행되는 일련의 작업 과정

![Boot](https://t1.daumcdn.net/cfile/tistory/263A093457EA1A2B09)

ROM에 있는 BIOS 로드 → BIOS가 부팅 순서대로 부트로더들을  로드 → 선택한 디바이스의 부트로더 로드 → 커널을 메모리에 로드하고 OS를 읽기

### CMOS

Complementary Metal-Oxide-Semiconductor의 약자로 BIOS가 사용하는 설정 정보를 저장하는 작은 메모리 칩

- BIOS가 컴퓨터의 하드웨어 구성 및 부팅 설정 정보가 저장되어 있는 CMOS 메모리에 접근하여 정보 사용
- 64 ~128바이트의 용량으로 **비휘발성** 메모리로 구성 → 전원이 꺼져도 저장된 설정 정보가 유지

![CMOS](https://www.howtogeek.com/wp-content/uploads/2022/05/cmos-battery-backup.jpg?width=1198&trim=1,1&bg-color=000&pad=1,1)

![CMOS](https://www.informit.com/content/images/0789724537/elementLinks/03fig06.gif)

![CMOS](https://www.computerhope.com/cdn/bios/bios4.gif)

### 부트로더

운영체제(이하 OS)가 시동되기 이전에 **미리 실행**되면서 커널이 올바르게 시동되기 위해 필요한 모든 관련 작업을 마무리하고 **최종적으로 운영 체제를 시동**시키기 위한 목적을 가진 프로그램

**부트로더의 위치**

저장 매체의 가장 앞 부분에 존재(MBR:Master Boot Record)

- 하드 디스크의 첫 번째 섹터는 부팅 가능한 유일한 영역.

![BootLoader](https://t1.daumcdn.net/cfile/tistory/2113154557EA1A2C3A)

---

## 정리

![BIOS](https://t1.daumcdn.net/cfile/tistory/2634E53857EA1A2C25)

1. **POST**(Power-On Self-Test) 진행: BiOS는 시스템이 부팅될 때 하드웨어를 초기화하면서 하드웨어 구성 요소의 상태 및 설정을 확인(CMOS)
    1. 하드웨어의 오작동이 있다면 경고메시지 출력
    2. CPU속도, 메모리 용량, 그래픽카드 등의 요소들의 설정
2. 부팅할 디바이스를 선택
    1. 부팅 디바이스를 올바르게 선택하지 않으면 부팅할 운영체제를 찾지 못한다
3. 부트로더 실행
    1. 선택한 부트 디바이스에서 부트로더를 찾아 실행
4. 운영체제부팅
    1. 부트로더가 프로그램을 로드하고 준비되면, OS 제어권을 부팅로더에게 넘겨줌