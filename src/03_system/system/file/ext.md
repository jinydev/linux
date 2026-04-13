---
layout: home
---

# 파일 시스템의 종류
리눅스에서 지원하는 파일 시스템은 다양합니다. 여기에는 일부 주요 파일 시스템을 소개하겠습니다.
이외에도 FAT, VFAT, ISO9660, UDF, NFS 등 다양한 파일 시스템을 지원합니다.

## ext2 (Second Extended File System)
ext2는 리눅스에서 처음 사용되었던 파일 시스템입니다. ext2는 대부분의 리눅스 배포판에서 기본 파일 시스템으로 사용되었습니다.

## ext3 (Third Extended File System)
ext3는 ext2의 업그레이드 버전으로, journaling 파일 시스템입니다. ext3는 파일 시스템의 안정성과 복구성을 향상시켰으며, 대부분의 리눅스 배포판에서 기본 파일 시스템으로 사용됩니다.

## ext4 (Fourth Extended File System)
ext4는 ext3의 후속 버전으로, 더 많은 기능과 성능 개선을 제공합니다. ext4는 대용량 파일과 디렉토리를 지원하며, 빠른 검색과 접근 속도를 제공합니다.

## XFS
XFS는 높은 처리량과 대용량 파일을 처리할 수 있는 파일 시스템입니다. XFS는 SGI에서 개발되었으며, 리눅스 커널에 통합되어 있습니다.

## Btrfs (B-tree File System)
Btrfs는 복사본-on-쓰기 (Copy-on-Write) 방식을 사용하는 파일 시스템으로, 스냅샷, 압축, RAID, 트랜잭션 등의 기능을 제공합니다. Btrfs는 리눅스 커널에 통합되어 있으며, 일부 리눅스 배포판에서는 기본 파일 시스템으로 사용됩니다.

## NTFS (New Technology File System)
NTFS는 마이크로소프트에서 개발한 파일 시스템으로, 윈도우 운영체제에서 기본 파일 시스템으로 사용됩니다. 리눅스에서는 NTFS-3G 드라이버를 사용하여 NTFS 파일 시스템을 지원합니다.

