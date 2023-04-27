#Redirection

---# 과제 Redirection

## Redirection이란?

<img src ="https://file.notion.so/f/s/52c83eba-a25f-42f8-a51a-eee022254483/img1.daumcdn.png?id=a0b3eab3-6656-4061-b58f-6922526b35eb&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660298281&signature=VcMbspAf5BY_MXrpeod9ZmcgmZ8YoR_TE3lv8cUSVt8&downloadName=img1.daumcdn.png">

- stdin 표준 입력
- stdout 표준 출력
- stderr 표준 에러

→ 표준 입력 스트림(stdin)에서 읽어오고 stdout 표준 출력 스트림에 씀

→ 오류가 발생한 경우 stderr, 표준 에러 스트림에 씀

→ 명령의 결과를 모니터로 출력하지 않고 파일로 저장할 수 있는 방법이 없을까?

→ redirection을 사용하여 출력과 입력의 방향을 지정해줌

### 입출력 리다이렉션


<img src ="https://file.notion.so/f/s/ea1b24ac-21b8-46e5-8373-7cda04a46aa9/%EB%A6%AC%EB%8B%A4%EC%9D%B4%EB%A0%89%EC%85%98.jpg?id=895d5516-0abc-4724-945e-d9233d70aa33&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660314971&signature=FWUNXHy5dXOqAdturVal0sJBvlFax0f2omb0eDwz778&downloadName=%EB%A6%AC%EB%8B%A4%EC%9D%B4%EB%A0%89%EC%85%98.jpg">

| 리다이렉션 기호 | 방향 | 의미 |
| --- | --- | --- |
| > | 표준 출력 | 명령 > 파일 : 명령의 결과를 파일로 저장 |
| >> | 표준 출력(추가) | 명령 >> 파일 : 명령의 결과를 기존 파일 데이터에 추가 |
| < | 표준 입력 | 명령 < 파일 : 파일의 데이터를 명령에 입력 |

### 표준 출력

- 표준 출력 변경 : cat 명령어 > , >> 사용
- cat 명령어: 원래 표준 입력인 키보드로부터 입력받은 내용을 표준 출력인 터미널로 보내는 명령어
- 하지만 다음과 같이 cat > 파일명 실행하고 파일의 내용을 작성한 후, ctrl + C를 눌러 종료하면 키보드로부터 입력받은 내용을 파일로 떨어뜨림

<img src ="https://file.notion.so/f/s/889876f3-e576-4b6a-ac2d-ea2b8e69efda/Untitled.png?id=ed720c41-bc17-4cd1-a048-63dc5cc8e8e9&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660328086&signature=nx87QjMzthtgF2CaNJNlUAhoG5GPRTfICcR86HDAVHo&downloadName=Untitled.png">

<img src ="https://file.notion.so/f/s/49ac2693-301f-498d-a779-dab46216caa3/Untitled.png?id=0cbb1708-8a71-4107-aca8-0a628062b593&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660341948&signature=Y7LJmA5XMcUSNjBRtXvS4fp_eCeBvtlhuKDCBfwphCA&downloadName=Untitled.png">

<img src ="https://file.notion.so/f/s/3783baea-44ea-499c-8c40-43314060821b/Untitled.png?id=75549ea9-c52a-4f82-a13c-addd297e66a9&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1682660351058&signature=isjP8HMUOdkZNqelhnjntmSM_FyjfxXs7ZOBG6fT1Ls&downloadName=Untitled.png">

### 기타 리다이렉션 기호의 쓰임

- **명령 >& 파일명** : 명령이 실행된 표준 출력의 결과와 에러를 파일로 출력
- **명령 >>& 파일명** : 명령이 실행된 표준 출력의 결과와 에러를 파일로 덧붙여 출력
- **명령 >! 파일명** : 파일의 존재 유무와 상관없이 생성하고 명령이 실행된 표준 출력의 결과를 파일로 출력
- **명령 >&! 파일명** : 파일의 존재 유무와 상관없이 생성하고 명령이 실행된 표준 출력의 결과와 에러를 파일로 출력
- **명령 >>! 파일명** : 파일의 존재 유무와 상관없이 생성하고 파일에 덧붙여 출력
- **명령 >>&! 파일명** : 파일의 존재 유무와 상관없이 생성하고 명령이 실행된 표준 출력의 결과와 에러를 파일에 덧붙여 출력
- **명령A | 명령B** : 명령A의 출력을 명령B 입력으로 사용하여 실행
- **명령A |& 명령B** : 명령A의 출력과 에러를 명령 B의 입력으로 사용하여 실행