---
layout: home
---

# IMAGES

**이미지의 유래**

해당파일이나 데이터가 비트맵 형태로 저장되어 있어 그림, 사진 또는 그래픽으로 나타낼 수 있다는 것에서 유래

## 여러가지 이미지

이미지란, 컴퓨터 파일이나 디스크 상의 데이터의 비트맵 표현이나, 다른 형식의 데이터를 일반적으로 그림, 사진 또는 그래픽으로 표현한 것

소프트웨어에서 이미지는 주로 디스크 이미지, 래스터 이미지, 벡터 이미지 등의 형식으로 사용

### **디스크 이미지**

- 디스크 또는 파티션의 정확한 복사본
- 디스크 이미지는 보통 **운영 체제 설치**를 위한 CD, DVD 또는 USB 드라이브 이미지로 사용되며, **소프트웨어 배포를 위해 사용**
    
    모든 데이터를 비트맵 형태로 복제한 이미지. → 물리적 디스크나 드라이브에서 부팅이 가능하며, 운영체제나 소프트웨어 패키지 등의 모든 데이터를 포함
    
    디스크 유틸리티나 복원 소프트웨어 등에서 사용
    
    ![Untitled](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxA1eoOxp_K5woOlymGQRAbQz_TiGf3cpY2oPeKLs0Q&s)
    

**ISO 이미지**

- ISO 이미지는 **광학 디스크**의 데이터를 비트맵 형태로 저장한 이미지
    
    모든 CD나 DVVD는 ISO 형식의 파일로 만들 수 있음
    
    운영 체제 설치 또는 소프트웨어 배포 등에 사용
    
    ![Untitled](https://t1.daumcdn.net/cfile/tistory/2460133E575B1AE702)
    

**래스터 이미지**

- 래스터 이미지는 픽셀 단위로 정보를 저장하며, 주로 디지털 카메라에서 생성되는 사진 등의 이미지 파일 형식으로 사용
    
    ![Untitled](https://blog.wishket.com/wp-content/uploads/2021/03/1-25.png)
    

**벡터 이미지**

- 벡터 이미지는 수학적인 수식을 사용하여 그림을 표현하는 방식으로, 주로 로고, 아이콘 등에 사용
    
    ![Untitled](https://blog.wishket.com/wp-content/uploads/2021/03/8-16.png)
    

### 가상 디스크 이미지 VDI(Virtual Disk Image)

가상 하드 디스크 또는 가상 시스템과 관련된 논리 디스크의 이미지

실제 하드 디스크 일부의 복제본으로 이미지 파일을 컨테이너로 취급하여 데이터를 읽고 쓸 수 있으며, 다른 시스템으로 가져갈 수 있고, 호환되는 가상 시스템에서 작동

- 가상화 환경(가상머신 등)에서 하나이상의 가상 머신에 할당된 디스크 공간 / 드라이브의 복제본을 작성하는데 사용
- 가상머신은 하나 이상의 가상 디스크 이미지를 사용하여, 운영체제와 애플리케이션을 실행하고 데이터를 저장
- 가상 디스크 이미지는 파일 형태로 저장되며, 가상 머신이나 가상화 소프트웨어에서 인식할 수 있는 형식으로 변환됨 (VMDK, VHD, VHDX 등)
    
    
    ![Untitled](https://upload.wikimedia.org/wikipedia/commons/d/d5/Virtualbox_logo.png)
    

### 도커 이미지

애플리케이션 실행에 필요한 소프트웨어 패키지와 라이브러리 등을 비트맵 형태로 저장한 파일

- 애플리케이션 실행에 필요한 모든 요소(소스 코드, 라이브러리, 종속성, 도구 등)를 포함하는 
**변경불가** 파일
- 런타임 환경을 위한 일종의 템플릿
- 컨테이너에서 실행될 때, 호스트 운영체제의 커널을 공유하여 가상화 기술을 사용하지 않음
- 개발 환경에서 도커 이미지를 생성하여 운영 환경에서 사용하여 두 환경의 차이를 최소화 가능
- 여러 애플리케이션을 실행하는 환경에서도 이미지를 사용하여 각 애플리케이션을 독립적으로 관리 할 수 있음
    
    ![Untitled](https://t1.daumcdn.net/cfile/tistory/9981E6375B8CF0802A)