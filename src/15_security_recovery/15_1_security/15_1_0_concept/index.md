---
layout: home
title: "15_1_security 기본 가이드"
---

[⬅️ 이전: 15_1_security](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../) &nbsp;|&nbsp; [다음 ➡️](../)

# 15.1 커널 보안, SELinux 및 방화벽

- **Root SSH 차단**: `/etc/ssh/sshd_config` 에서 `PermitRootLogin no` 로 설정하여 외부 직결을 차단합니다.
- **무차별 대입 방어**: Fail2Ban 과 같은 써드파티 툴이나 로컬 방화벽의 Rich Rule을 사용하여 IP를 영구 밴합니다.
- **SELinux**: 리눅스 커널 심층 보안 기법으로, 해커가 침투해도 컨텍스트가 없는 폴더는 읽을 수 없도록 격리합니다.

---


---

[⬅️ 이전: 15_1_security](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../) &nbsp;|&nbsp; [다음 ➡️](../)
