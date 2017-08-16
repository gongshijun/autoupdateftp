**autoupdateftp** uses for auto download file from ftp sever. Incremental downloads are implemented. What's more, it can maintain downloading the specified file directory.

***updateftp.conf***  
```
#ftp attribute  
ftp_host = your ftp host  
username = ftp sever login username  
password = ftp sever login password  
#ftp_path used for setting the root directory, '/' represents the root directory is the ftp sever root directory  
ftp_path = /  
#update_dirs used for setting auto-update directory below in the root directory, format: 'data1, data2', '/' represents to update all.  
update_dirs = /  
#root_dir used for setting the root directory of saving data in ftp sever  
root_dir = data
```

***Dependencies***  
**autoupdateftp** was developed on Windows 7. In principal, **autoupdateftp** should work with any Linux
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