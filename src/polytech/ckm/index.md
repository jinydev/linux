---
layout : home
---

# Ckm Report
# 소스트리 사용법
## Git GUI
Git을 좀더 편하게 사용하기 위해서는 Git GUI(Graphic User Interface)를 사용하는 것입니다.
#### Git GUI의 대표적인 종류 
- SourceTree
- Github Desktop
- Git Extensions
- GitKraken

#### 각 GUI 별 특징
##### 1. Soucetree
- bitbucket, trello, jira 등을 서비스하는 Atlassian에서 만든 어플리케이션 입니다.
- 장점
   - 안복잡함- 직관적인 UI
   - 한글됨- 이 점 때문에 한국 유저가 Git을 입문하기 쉬워 한국 한정 점유율이 높습니다.
   - 시각화- marge, branch등 시각화가 아주 잘 되있습니다.
- 단점
  - 느리다 - 줄수가 많은 파일을 미리 볼때 로딩이 꽤 걸립니다. 간단한 소스면 모르겠지만, Markdown, html 이나 mata, xml 처럼 줄이 쉽게 많아 질수 있는 경우면 굉장히 답답할것 입니다.

##### 2. Github Desktop
- Github를 서비스하고 코드편집기 Atom을 개발하는 Github에서 만든 어플리케이션 입니다. 
- 장점
  -  빠름-  멈춘다는 느낌이 없습니다.
  -  커밋정보- 변경점이 제일 확인하기 편합니다.
  -  오픈소스- 자유로 커스텀하고, 빌드 할 수 있습니다.
- 단점
  - 한글이 안된다 , 한글을 지원하지 않습니다.
  - 시각화 부족 - merge, branch의 시각화가 거의 없습니다

##### 3. Git Extension
- 정확히는 git의 확장기능들이 포함된 소프트웨어 입니다. 2008년부터 역사가 시작됬으며, 제일 강력하고 개발자 친화적인 소프트웨어 입니다.
- 장점
  - 시각화- marge, branch등 시각화가 아주 잘 되있습니다.
  - 오픈소스- 자유로 커스텀하고, 빌드 할 수 있습니다.
  - 빠르고,안정적- 무려 2009년 부터 개발됬습니다. 제일 빠르고, 가장 안정적입니다.
  - 우클릭- 어플리케이션이 아닌 Git repositry가 있는 폴더에서 우클릭을하면 git을 이용할 수 있습니다.
- 단점
  - 안예쁨- UI가 투박한 대신 제일빠르지만, 중요한것은 애니메이션이 없어서 버벅인다고 느낄 수 있습니다.
  - 비 직관적- 아이콘 보다는 텍스트, 직관적이기보다는 세부적입니다.


##### 4. GitKraken
- Git을 사용하는 개발자들을 위한 크로스 플랫폼 GUI Git 클라이언트입니다. GitKraken은 Git 작업을 시각적으로 표현하여 사용자가 Git의 작업을 더욱 쉽게 이해할 수 있도록 도와줍니다.
- 장점
  - 시각적 인터페이스: GitKraken은 Git 작업을 시각적으로 표현하여 Git의 작업을 더욱 쉽게 이해할 수 있습니다. 브랜치, 병합, 태그 등의 Git 작업을 시각화하여 보여주기 때문입니다.
  - 다양한 기능: GitKraken은 Git 작업을 위한 다양한 기능을 제공합니다. Git의 모든 기능을 지원하며, 코드 리뷰, 코드 스니펫 등의 기능도 제공합니다.
  - 다중 플랫폼 지원: Windows, macOS, Linux 운영체제에서 모두 지원됩니다.

- 단점
  - 무거운 애플리케이션: GitKraken은 다른 Git 클라이언트에 비해 무거운 애플리케이션입니다. 이는 GitKraken의 시각적 인터페이스를 지원하기 위해 많은 리소스를 사용하기 때문입니다.

### Source Tree 사용방법

##### Source Tree 설치 링크: https://www.sourcetreeapp.com/
   
   
   
##### 사용을 위한 용어 정리
- 저장소(Repository): 내가 Git 으로 관리할 폴더(디렉터리)이다
- 커밋(Commit): Git에서 버전을 기록하는 단위이다
- 커밋한다: Git에 하나의 버전을 기록한다
- 로컬(Local): 네트워크 없이 접속 가능한 것
- 로컬 컴퓨터 = 내가 바로 사용하고 있는 컴퓨터라고 할 수 있다
- 원격(Remote): 네트워크를 접속해서 사용해야 하는 것
- 클라우드(Google Drive 같은 것): Git 저장소를 올려서 공유하는 곳이다
   - (ex) GitHub, Bitbucket
- 푸시(Push): 로컬에 있는 저장소를 인터넷(Remote)에 올리는 것
  - 푸시를 하면 .git 폴더를 포함해서 나의 모든 파일과 변경 과정(커밋)들을 업로드 한다
- 복제(Clone): 인터넷에 있는(원격) 저장소를 로컬에 다운 받는 것
###### sourceTree를 사용하려면 github와 같은 원격 저장소가 필요하다. 따라서 github 아이디를 만든 후 new repository를 만들어준다.

## 
![Alt text](https://user-images.githubusercontent.com/91362374/232516968-b124b79d-d92a-4191-ab04-6fd73addb86a.png)

###### 우리는 github와 SourceTree를 연결하고 싶으므로 gitclone과 같은 작업을 수행하여야한다. 따라서 상단의 clone버튼을 눌러준다.
![Alt text](https://user-images.githubusercontent.com/91362374/232518880-d0e8d1de-3e72-44f2-bf87-a092a79f3e9c.png)
github repository 주소를 복사 붙여넣기 하게 되면 SourceTree에서 자동으로 git 저장소라는 것을 판별하여 알려주게 된다.
그 다음 자신의 컴퓨터에 저장될 로컬 저장소의 위치를 지정한 뒤 코드를 git clone해준다.

- 다음과 같은 텍스트 파일을 만들어줍니다
![testfile](https://user-images.githubusercontent.com/91362374/232520253-a6ce3d45-5b98-4126-8bcf-c86da6f2425f.png)
- 그 후 clone이 저장된 로컬디렉토리에 넣어준다
![storeclonefolder](https://user-images.githubusercontent.com/91362374/232520536-994b78e0-db9c-44fd-a88c-b360c032d036.png)
- 다음과 같은 화면이 나타난다
![unstage](https://user-images.githubusercontent.com/91362374/232520875-a58bfa73-6788-4c7b-9325-208497fa1a6f.png)


- 스테이지에 올라가지 않은 상태
> Workspace - 파일상태 (git의 파일 상태 분류법)
![unstage](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcFx5dh%2FbtqSIYvwXxl%2FxXfkOiLfMGka6VdukHU5mK%2Fimg.png)

![onStage](https://user-images.githubusercontent.com/91362374/232522538-37f30b04-fffd-491c-bfc0-72ab15914711.png)

![commitInsert](https://user-images.githubusercontent.com/91362374/232524560-b1ff9cdd-3674-4a9d-ae3b-304d672e9ee3.png)
- commit창을 누르게 되면 위와 같은 화면이 뜬다. 또한 commit을 하고 싶다면 commit message를 작성한 후 커밋 버튼을 누르면 된다.
![commitResult](https://user-images.githubusercontent.com/91362374/232524775-0362dff7-b58e-43b7-8b9e-86b2d69c2e3a.png)
- 커밋을 하게 되면 저장이 되게 되는데 이를 원격 저장소에 올리고 싶다면 push라는 과정을 거쳐야한다.
![push](https://user-images.githubusercontent.com/91362374/232525373-194fba93-63b1-4283-8475-b23fbc1b82ec.png)

- push버튼을 누르게 되면 commit한 과정 중 push하지 않았던 것들이 원격 저장소 github에 올라가게 된다.
![pushResult](https://user-images.githubusercontent.com/91362374/232525994-589c8b77-c9c1-49ab-878a-1cbdf53ba57b.png)

- 메뉴 모음
![menu](https://user-images.githubusercontent.com/91362374/232536839-93a563e1-68d1-4e73-8f0e-d75490fe6d09.png)
  - 커밋: 스테이징된 파일을 커밋
  - Pull: 원격 저장소의 변경 사항들을 전부 가져오기
  - Push: 지역 저장소의 변경 사항들을 전부 원격 저장소로 내보내기
  - 패치: 원격 저장소의 내용을 가져오기 전에 변경 사항이 있는지 확인
  - 브랜치: 브랜치의 생성과 삭제 등을 관리
  - 병합: 브랜치 병합
  - 스태시: 커밋하기 이전의 파일을 따로 보관합니다. 일종의 감추기기능인데, -  스태시를 이용하기 위해서는 파일이 추적(Tracked)상태여야합니다. 즉 한 번 이상은 커밋된 적이 있는 파일에 대해서만 사용이 가능합니다.
  - 태그: 특정한 위치에 태그를 답니다.
- 브랜치 베너를 통해 브랜치를 새로 만들 수 있다
![branchnew](https://user-images.githubusercontent.com/91362374/232529603-a9983d49-26a9-49ac-85fb-b382b9ebae96.png)
- 클릭을 통해 브랜치를 이동하여 작업 할 수 있다
![branchresult](https://user-images.githubusercontent.com/91362374/232530316-957b6a7c-cb34-4070-aebc-bcbf1ad601c9.png)

- Fetch
  - Pull은 변경 사항을 다운받고 내 로컬 저장소에 적용까지 한다.
정확히 말하자면 모든 커밋을 다운로드하고 자동으로 Merge까지 해준다. (뒤에서 함)
  - Fetch는 다운 받기만 하고 적용은 안 한다. 실제 파일은 변하지 않는다.
한번 확인하고 수동으로 Merge할 수 있기 때문에 보통 Fetch가 더 안정적이다.
  - 따라서, Pull = Fetch(다운만 함) + Merge(합침)
  - 실수를 할 수 있기 때문에 Fetch하고 Merge하는 것을 권장한다.
![fetch](https://user-images.githubusercontent.com/91362374/232531578-d4a14a2f-9456-4460-b81f-58fb13a76d98.png)

- Revert (되돌리기)
파일들을 이전 [커밋]인 상태로 되돌린 새로운 커밋을 만든다.
  - 이전 커밋을 수정하지 않고 그대로 남겨두기 때문에 안전하다.
  - Revert를 하고 난 다음에는 새로운 커밋이 생기기 때문에 바로 충돌 없이 Push할 수 있다.
  - git revert [커밋]
  - 바로 커밋해주는게 싫다면 git revert -n [커밋]
![revert](https://user-images.githubusercontent.com/91362374/232537886-11b60f2c-2d1f-4cd7-b884-85c280de4a5d.png)

