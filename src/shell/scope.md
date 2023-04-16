---
layout: home
---


# Variable Scope


![슬라이드35](./img/슬라이드35.PNG)

```
heejinlee@ubuntu:~/0703$ export outvar="variable outside"
```



```
#ex1.sh
#!/bin/sh
export middle="xx"
echo "outvar in sh1: " $outvar
echo “middle in sh1: " $middle

sh ex3.sh
exit 0
```



```
#ex2.sh
 #!/bin/sh
export middle="yy"
echo "outvar in sh2: " $outvar
echo “middle in sh2: " $middle

sh ex3.sh
exit 0

```



```
#ex3.sh
 
#!/bin/sh
echo ====3.sh start==========
echo $sdf
echo "middle : " $middle 


middle="changed middle in sh3"
echo middle  $middle 

echo "outvar in sh3: " $outvar

echo ======end 3.sh========
exit 0

```
