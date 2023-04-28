---
layout: home
---
# IP
---
## IP주소

- 네트워크 통신을 할 때 3계층에서 필요
- 3계층에서는 3계층 장비인 라우터가 이해하는 논리주소인 IP 주소를 사용
- 3계층 주소의 특징
    - 사용자가 변경 가능한 논리 주소
    - 그룹을 의미하는 네트워크 주소와 호스트 주소로 나뉨

### IP 주소 체계

<img src="https://file.notion.so/f/s/2595dd64-5ab7-4433-ac78-33e7f6258463/images_satoshi25_post_551623c4-e2bb-4d35-b8ea-c988cad396a0_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.25.51.png?id=0d8eca94-1266-4724-91ca-22ce98893960&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670491203&signature=dRX_F_fRZGojvSXcV05fck0ycHigZ5zAJwphSluUWIY&downloadName=images_satoshi25_post_551623c4-e2bb-4d35-b8ea-c988cad396a0_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-13+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+12.25.51.png">

1. 주로 IP 주소는 32 비트인 IPv4 주소를 사용
2. IPv4, IPv6 두 체계가 사용
3. IPv4는 8비트 단위를 하나의 옥텟이라고 부름
4. 각 옥텟은 점으로 구분, 10진수로 표기
5. 하나의 옥텟은 8비트이기 때문에 00000000 ~ 11111111 → 0 ~ 255까지 사용 가능
6. IP 주소는 네트워크 주소와 호스트 주소 두 부분으로 나뉨
- 네트워크 주소
    - 호스트들을 모은 네트워크를 지칭하는 주소
    - 네트워크 주소가 동일한 네트워크를 로컬 네트워크라고 함
- 호스트 주소
    - 하나의 네트워크 내에 존재하는 호스트를 구분하기 위한 주소
    - 로컬 네트워크를 구성하는 하나의 네트워크

### classful과 classless

**classful IP**

<img src="https://file.notion.so/f/s/bb498081-b168-42f6-9512-5db9f5b2b18e/images_satoshi25_post_28c51f34-7bb1-41f3-8c88-7ca1f33d18ae_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.31.22.png?id=6efb4d72-7e31-42c3-b6b3-fb625000da02&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670507735&signature=6dsguemBlLpb62vuPIaaGfClXVdDl48JLFiSQkkNRp4&downloadName=images_satoshi25_post_28c51f34-7bb1-41f3-8c88-7ca1f33d18ae_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-21+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.31.22.png">

1. IP 주소는 네트워크 주소와 호스트 주소를 나누는 구분자가 이동할 수 있어서 네트워크의 크기가 달라질 수 있음
2. 네트워크의 크기에 따라 필요한 호스트 IP 개수를 할당할 수 있는 클래스 개념을 도입
3. 크게 A,B,C클래스로 나뉘고 규모에 따라 나뉘게 됨

**class**

1. A class
    1. 1개의 옥텟이 네트워크 주소를 나타냄
    2. 3개의 옥텟이 호스트 주소를 나타냄
    3. 첫번째 .이 나누는 구분자가 됨
    4. 그렇게 255.0.0.0 ~ 255.255.255.255까지 정해진 네트워크 주소에 호스트 주소 16,777,216개의 주소를 가질 수 있음
2. B class
    1. 2개의 옥텟이 네트워크 주소를 나타냄
    2. 2개의 옥텟이 호스트 주소를 나타냄
    3. 두번째 .이 나누는 구분자가 됨
    4. 그렇게 255.255.0.0 ~ 255.255.255.525까지 정해진 네트워크 주소에 호스트 주소 65.536개의 주소를 가질 수 있음
3. C class
    1. 3개의 옥텟이 네트워크 주소를 나타냄
    2. 1개의 옥텟이 호스트 주소를 나타냄
    3. 세번째 .이 나누는 구분자가 됨
    4. 그렇게 255.255.255.0 ~ 255.255.255.255까지 정해진 네트워크 주소에 호스트 주소 256개의 주소를 가질 수 있음

**IPv4의 한계로 IPv6 등장**

- IPv4의 가장 큰 문제: 기하급수적으로 늘어나는 IP 주소 요구
- 43억개 중 5억개 정도는 예약되어있는 IP, 37억개를 나눠 사용해야 함
- 부족한 개수를 보안하기 위해 방안 등장
1. 클래스리스, CIDR (Classless Inter-Domain Routing) 기반의 주소체계
2. NAT과 사설 IP
3. IPv6

**classful IP의 한계로 classless IP 등장**

- 각 클래스에서 모든 IP를 다 사용하지 않아서 낭비되는 IP가 많음
- 네트워크 주소에 사용하지 않는 호스트를 다른곳에서 사용할 수 없었기 대문에 옥텟 단위의 3단계로 나누는 클래스로는 개선이 어려웠음
- 그렇게 class 개념을 버리고 현재 사용하고 있는 classless 주소 체계를 사용
- classless는 classful처럼 옥텟만으로 네트워크 주소와 호스트 주소를 나눌 수 없음
- 낭비를 줄이기 위해서 비트 단위로 쪼개 사용하는 방법
- 네트워크와 호스트 주소를 나누는 구분자로 서브넷 마스크를 사용
    
    <img src="https://file.notion.so/f/s/076e6b6e-acce-4467-9e25-ec6d9799807f/images_satoshi25_post_f2cd319d-ea4b-4234-8ef3-43f35b7c0caa_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.31.18.png?id=be6ebf58-0de5-4ad1-a0ac-1a81dd58fe98&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670524346&signature=ucbtb-nFf5Hq34_ETPb4mJPd27FY3E5dBmCwbQOlfvM&downloadName=images_satoshi25_post_f2cd319d-ea4b-4234-8ef3-43f35b7c0caa_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-13+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.31.18.png">
    
- 클래스리스 기반의 IP 네트워크에서는 네트워크를 표현할 때 서브넷 마스크가 반드시 있어야 함
- 서브넷 마스크를 이용하여 네트워크 주소를 구할 때는 0과 1의 And 연산을 이용
- 호스트 주소의 각 옥텟을 8비트로 나타낸 주소와 서브넷 마스크를 8비트로 나타낸 주소 각각의 비트를 & 연산을 통해 네트워크 주소를 알 수 있음

**서브넷 마스크 표현 방법**

- 1로 나타낸 부분의 비트 수를 표시하여 나타냄
- 이전의 A 클래스를 비트 단위로 표현하면 /8로 표현
- B클래스는 /16으로 표현
- C클래스는 /24로 표현
- A 클래스 → 11111111.00000000.00000000.00000000
- B 클래스 → 11111111.11111111.00000000.00000000
- C 클래스 → 11111111.11111111.11111111.00000000

### 서브네팅

- 클래스의 기준을 무시하고 클래스풀 단위의 네트워크보다 더 쪼개 사용하는 것
- 부여된 주소를 다시 분할하는 방법
- 서브네팅으로 서브넷을 나누어 사용할 수 있음

**네트워크 사용자의 서브네팅**

- IP 와 서브넷 마스크 둘 다 이용하는 방법
    
    <img src="https://file.notion.so/f/s/9ce9a6e7-b72f-4ddb-a917-33a115b3273c/images_satoshi25_post_137246c6-2a39-4737-93b8-c3ced92052b2_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.40.51.png?id=cd7bfa9a-66a7-465c-8bf0-de2c2287cd5c&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670558631&signature=bPAhJV5YIsdvFWWUEoHo7WtTW5YjkF-CknVXDkS-uEk&downloadName=images_satoshi25_post_137246c6-2a39-4737-93b8-c3ced92052b2_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-21+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.40.51.png">
    
    IP와 서브넷 마스크 각각의 옥텟을 2진수 주소 변환
    
    <img src="https://file.notion.so/f/s/b87489aa-7752-4536-b506-9e936089c54f/images_satoshi25_post_dc463221-a076-4a10-91e8-a7014abced51_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.41.22.png?id=dc7d5c2f-bf7f-484d-a10e-5a1f57f6cdb8&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670567621&signature=khfICc7Iye5igHuKWmbrRCPoZ9gEKtOWL7RMu6kaFwI&downloadName=images_satoshi25_post_dc463221-a076-4a10-91e8-a7014abced51_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-21+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.41.22.png">
    
    - 3번 : 2진수로 바꾼 IP와 서브넷 마스크를 &&로 연산 (네트워크 주소)
    - 4번: 네트워크 주소에 서브넷 마스크의 0부분과 같은 부분을 1로 바꿈 (브로드 캐스트 주소)
        
    <img src="https://file.notion.so/f/s/59711741-9529-4383-9553-b8e2de0e208b/images_satoshi25_post_765dccbe-fbe0-4279-a09e-e05d427ce32c_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.41.40.png?id=a9dcf2c3-0c67-46e7-b29c-9753a8636db4&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670584026&signature=-gp1vFkpF0SxgfKALMAokOdt_WhMqm4Ru_m2wfva41c&downloadName=images_satoshi25_post_765dccbe-fbe0-4279-a09e-e05d427ce32c_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-21+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.41.40.png">
        
    - 5번: 네트워크주소의 마지막 숫자에 1을 더한 주소가 이용할 수 있는 첫번째 주소가 됨
    - 6번: 브로드 캐스트 마지막 숫자에 1을 뺀 주소가 이용할 수 있는 마지막 주소가 됨
        
    <img src="https://file.notion.so/f/s/d44708f5-5df5-4de0-8ad5-511900657abb/images_satoshi25_post_d77c2d53-f472-4380-b906-fd78b0a2291b_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.41.52.png?id=e1a90e84-e495-49e1-b77f-2b07a11f7f13&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670600620&signature=b9TSakPDFRNPIzeksIJWN-WmqPqfRloLNN_EL7Vigu0&downloadName=images_satoshi25_post_d77c2d53-f472-4380-b906-fd78b0a2291b_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-21+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.41.52.png">
        
        - 7번: 각각 구해진 주소를 10진수로 변환하면 우리가 사용하는 IP 주소가 됨
- 서브넷 마스크만 이용하는 방법
    
    <img src="https://file.notion.so/f/s/bab7cd1a-3629-4a63-9cb0-8ac53e4bda03/images_satoshi25_post_3a9361a6-5485-4861-a7ac-60dc186682a6_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-09-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.58.34.png?id=d3804a65-1714-4058-b1e6-cd1082fc6484&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682670613659&signature=EtBgjPzttiOBBB4_sjfUNtWQL4De76iaq7fIEukZaTc&downloadName=images_satoshi25_post_3a9361a6-5485-4861-a7ac-60dc186682a6_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2021-09-21+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.58.34.png">
    
    - 1번: 서브넷 마스크를 2진수로 변환
    - 2번: 서브넷 마스크의 0부분만을 가져옴
    - 3번: 0 부분이 몇을 표현할 수 있는지 수를 구함
    - 4번: 각 자리마다 0부터 구해진 수만큼 그룹을 나눔
    - 5번: IP 주소가 이 그룹중에 어디에 있는지 찾음
    - 6번: 그룹의 가장 앞에 있는 주소가 네트워크 주소가 됨
    - 7번: 네트워크 주소에서 1을 더한 값이 사용할 수 있는 첫번째 주소가 됨
    - 8번: 그룹의 가장 뒤에 있는 주소가 브로드 캐스트 주소가 됨
    - 9번: 브로드 캐스트 주소에서 1을 뺀 값이 사용할 수 있는 마지막 주소가 됨