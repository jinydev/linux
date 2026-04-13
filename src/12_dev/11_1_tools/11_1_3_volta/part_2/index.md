---
layout: home
title: "volta로 노드 설치하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# volta로 노드 설치하기

## volta로 노드 설치하기
volta를 이용하면 시스템에 쉽게 nodejs를 설치할 수 있습니다. 다음과 같이 명령을 입력합니다.

```
# install Node
volta install node
```

> volta는 최신의 안정화된 LTS 버젼의 nodejs를 설치합니다. 만일, 다른 버젼을 설치하고자 할때에는 `@버젼`을 붙여서 명령을 실행하면 됩니다.
> ```
> # current 버젼설치
> volta install node@19
> ```

nodejs가 잘 설치가 되었는지 실행을 해봅니다.

```
# start using Node
node -v
```

> volta는 윈도우에서도 사용이 가능합니다.

volta를 이용하면 node pakage manager인 npm도 같이 설치가 됩니다.

```
hojin@hojin3:~$ npm -v
9.5.0
```

---

[⬅️ 이전: 형상관리 git](../11_1_2_git/) &nbsp;|&nbsp; [🏠 분류 목차](../../../) &nbsp;|&nbsp; [다음: VSCode Remote연결 ➡️](../11_1_4_vscode/remote/)


---

[⬅️ 이전](../)
