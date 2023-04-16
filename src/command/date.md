---
layout: home
---


## Date 관련

```bash
#date 형식
#!/bin/sh

echo “date test”
echo “date : $(date +%Y%m%d)”
echo “date : $(date +%Y)년 $(date +%m)월 $(date +%d)일”
Echo “date : $(date +%H)시 $(date+%M)분 $(date+%S)초 입니다.”


echo `date`
d_date=`date +%Y%m%d`
echo $d_date

```