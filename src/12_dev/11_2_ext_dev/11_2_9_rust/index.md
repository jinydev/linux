---
layout: home
---

# Rust
리눅스에 러스트(Rust)를 설치하려면 다음과 같은 단계를 따르면 됩니다.

## Rustup 설치하기
Rust를 설치하기 위해 Rustup을 설치합니다. Rustup은 Rust 개발 환경을 쉽게 관리할 수 있도록 도와주는 도구입니다.

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## PATH 설정하기
Rustup은 Rust 개발 환경을 사용하기 위해 PATH를 설정해야 합니다. 설정 명령어는 Rustup 설치 시 출력되는 내용을 참고하여 실행합니다.  
```
source $HOME/.cargo/env
```

## 러스트 설치 확인하기
Rustup이 정상적으로 설치되었는지 확인하기 위해 rustc(러스트 컴파일러) 버전을 확인합니다.  

```
rustc --version
```

위와 같이 간단한 단계를 따르면 리눅스에서 러스트를 설치할 수 있습니다.
