---
layout: home
---
# 15.3 증분 백업 및 재난 복구 체계 (rsync)

하드디스크가 물리적으로 박살나거나 랜섬웨어에 감염될 것에 대비해 코드를 외부 저장소로 실시간 복사해야 합니다.

- **rsync**: 파일 시스템의 변경된 바이트(증분)만을 고속 전송하는 궁극의 유틸리티입니다.
  - 예: `rsync -avz --delete /var/www/ hojin@backup-server:/backup/web/`
- **Cron 연동**: 새벽 3시 등 접속자가 없는 시간대에 쉘 스크립트로 묶인 rsync가 자동 동작하도록 cron에 스케줄링합니다.