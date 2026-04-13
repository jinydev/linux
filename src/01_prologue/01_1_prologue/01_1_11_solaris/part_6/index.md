---
layout: home
title: "Solaris 관리 도구"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# Solaris 관리 도구

## Solaris 관리 도구

### 1. 시스템 관리 도구

Solaris는 다양한 시스템 관리 도구를 제공합니다.

#### 명령어 기반 도구

**시스템 모니터링:**
```bash
# 시스템 정보 확인
prtconf
prtdiag
psrinfo

# 성능 모니터링
mpstat
iostat
vmstat

# 프로세스 관리
prstat
pgrep
pkill
```

**파일 시스템 관리:**
```bash
# ZFS 관리
zpool create pool_name device
zfs create pool_name/dataset
zfs snapshot pool_name/dataset@snapshot

# 파일 시스템 확인
df
du
ls -la
```

### 2. 그래픽 관리 도구

Solaris는 그래픽 기반 관리 도구도 제공합니다.

#### GUI 도구

**Solaris Management Console:**
- **시스템 관리**: 통합 시스템 관리 인터페이스
- **사용자 관리**: 사용자 및 그룹 관리
- **서비스 관리**: 시스템 서비스 관리
- **보안 관리**: 보안 설정 및 관리

**Oracle Enterprise Manager:**
- **모니터링**: 실시간 시스템 모니터링
- **성능 분석**: 성능 분석 및 최적화
- **자동화**: 시스템 관리 자동화
- **보고서**: 상세한 시스템 보고서


---

[⬅️ 이전](../)
