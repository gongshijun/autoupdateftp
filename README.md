**autoupdateftp** uses for auto download file from ftp sever. Incremental downloads are implemented. What's more, it can maintain downloading the specified file directory.

***updateftp.conf***
```
#ftp attribute  
ftp_host = your ftp host  
username = ftp sever login username  
password = ftp sever login password  
#ftp_path used for setting the root directory 
#in the ftp sever, '/' represents the root 
#directory is the ftp sever root directory  
ftp_path = /  
#update_dirs used for setting auto-update directory 
#below in the root directory of the ftp sever,   
#format: data1, data2, '/' represents to update all.  
update_dirs = /  
#exclude_dirs used for setting ignore the directory 
#below in the root directory of the ftp sever 
#when download file from ftp sever. format: data1, data2, default is none.  
#What's more, if you want to set the exclude_dirs, 
#the update_dire = / is a requirement.  
exclude_dirs = Trader_LL  
#root_dir used for setting the root directory of saving data 
#from the ftp sever  
root_dir = data  
```
***Dependencies***  
**autoupdateftp** was developed on Windows 7. In principal, **autoupdateftp** should work with any Windows
distribution as long as the following software dependencies are satisfied.

1. Python [version 3.6.1 or higher]
2. Ftputil python Libtaries [version 3.3.1 or higher]
```
pip install ftputil
```

***run autoupdateftp***
```
python autoupdateftp
````