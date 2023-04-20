#Redirection

---# 과제 Redirection

## Redirection이란?

<img src ="https://file.notion.so/f/s/52c83eba-a25f-42f8-a51a-eee022254483/img1.daumcdn.png?id=63396bdf-193d-43ca-a03c-b02bef49b351&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1681965176503&signature=8uaLMr4_jvE-2ThHbzfR1vgQiBvR36REZGMa4uqsfFE&downloadName=img1.daumcdn.png">

- stdin 표준 입력
- stdout 표준 출력
- stderr 표준 에러

→ 표준 입력 스트림(stdin)에서 읽어오고 stdout 표준 출력 스트림에 씀

→ 오류가 발생한 경우 stderr, 표준 에러 스트림에 씀

→ 명령의 결과를 모니터로 출력하지 않고 파일로 저장할 수 있는 방법이 없을까?

→ redirection을 사용하여 출력과 입력의 방향을 지정해줌

### 입출력 리다이렉션


<img src ="https://file.notion.so/f/s/ea1b24ac-21b8-46e5-8373-7cda04a46aa9/%EB%A6%AC%EB%8B%A4%EC%9D%B4%EB%A0%89%EC%85%98.jpg?id=67a1779f-57ef-4ea5-ae09-1d99d5cb6ea4&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1681965202081&signature=471N3GS674VqBLiepSkoSQd8fCxTgHYzUIRyX_2qhkc&downloadName=%EB%A6%AC%EB%8B%A4%EC%9D%B4%EB%A0%89%EC%85%98.jpg">

| 리다이렉션 기호 | 방향 | 의미 |
| --- | --- | --- |
| > | 표준 출력 | 명령 > 파일 : 명령의 결과를 파일로 저장 |
| >> | 표준 출력(추가) | 명령 >> 파일 : 명령의 결과를 기존 파일 데이터에 추가 |
| < | 표준 입력 | 명령 < 파일 : 파일의 데이터를 명령에 입력 |

### 표준 출력

- 표준 출력 변경 : cat 명령어 > , >> 사용
- cat 명령어: 원래 표준 입력인 키보드로부터 입력받은 내용을 표준 출력인 터미널로 보내는 명령어
- 하지만 다음과 같이 cat > 파일명 실행하고 파일의 내용을 작성한 후, ctrl + C를 눌러 종료하면 키보드로부터 입력받은 내용을 파일로 떨어뜨림

<img src ="https://file.notion.so/f/s/889876f3-e576-4b6a-ac2d-ea2b8e69efda/Untitled.png?id=6e19c399-fe98-4596-93ca-635dd7dfb8cd&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1681965220032&signature=PfSdI7aACF6iZF4-8DCxILa1ck8o4LGlr8mCHVxXtGg&downloadName=Untitled.png">

<img src ="https://file.notion.so/f/s/49ac2693-301f-498d-a779-dab46216caa3/Untitled.png?id=0ce700d7-4d8d-4a25-8e06-bd2e42ed8624&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1681965238753&signature=cgBtNh5oLP5-42WKddUDT8t4n2Fjd7rqqxeGdZUg3eE&downloadName=Untitled.png">

<img src ="https://file.notion.so/f/s/3783baea-44ea-499c-8c40-43314060821b/Untitled.png?id=cdde1558-8e50-41a4-826b-4cd5e3a07abb&table=block&spaceId=f7f5a27f-fb49-4dd8-8a47-1d1cb5901c61&expirationTimestamp=1681965247963&signature=Oq5TKtBST80rJg6-QuQVdkaxEMDX9kfPCT_ArANia18&downloadName=Untitled.png">

### 기타 리다이렉션 기호의 쓰임

- **명령 >& 파일명** : 명령이 실행된 표준 출력의 결과와 에러를 파일로 출력
- **명령 >>& 파일명** : 명령이 실행된 표준 출력의 결과와 에러를 파일로 덧붙여 출력
- **명령 >! 파일명** : 파일의 존재 유무와 상관없이 생성하고 명령이 실행된 표준 출력의 결과를 파일로 출력
- **명령 >&! 파일명** : 파일의 존재 유무와 상관없이 생성하고 명령이 실행된 표준 출력의 결과와 에러를 파일로 출력
- **명령 >>! 파일명** : 파일의 존재 유무와 상관없이 생성하고 파일에 덧붙여 출력
- **명령 >>&! 파일명** : 파일의 존재 유무와 상관없이 생성하고 명령이 실행된 표준 출력의 결과와 에러를 파일에 덧붙여 출력
- **명령A | 명령B** : 명령A의 출력을 명령B 입력으로 사용하여 실행
- **명령A |& 명령B** : 명령A의 출력과 에러를 명령 B의 입력으로 사용하여 실행