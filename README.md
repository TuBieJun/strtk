# strtk： 处理str seq数据的工具
strtk由多个模块组成。  
## view
### 查看指定区间或位点或染色体的genotype
```
strtk view -s in_str_file -i index_file -r 1:1-10000
strtk view -s in_str_file -i index_file -r 1:10000
strtk view -s in_str_file -i index_file -r X
```
## stats
### 统计str 数据的位点个数、杂合率和call rate。可以选择指定区间
```
strtk stats -s in_str_file
strtk stats -s in_str_file -r 1:1-10000
```  
## com
### 比较两个str seq的一致性。 可以选择指定区间，是否过滤indel。
```
strtk com -s1 in_str_file1 -s2 in_str_file2
strtk com -s1 in_str_file1 -s2 in_str_file2 -i index_file -r X -f #只比较X染色体的snp位点
```
## str2vcf
### 将str file转为vcf格式。 可以选择指定区间， 是否过滤no call和indel。
```
strtk str2vcf -s in_str_file -f -n -i index_file -o out.vcf -I sampleid -r X:1-10000 
```