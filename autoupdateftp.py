#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 16:59
# @Author  : Shijun Gong
# @Version    : 0.1.0
# @File    : autoupdateftp.py
# @Software: PyCharm

def read_conf():
    ftp_host = ''
    ftp_name = ''
    ftp_pwd = ''
    ftp_path = ''
    root_dir = ''
    keep_update_dirs = ''
    exclude_dirs = ''
    try:
        with open('updateftp.conf', 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line == '':
                    continue
                if line[0] == '#':
                    continue
                if line.split('=')[0].strip() == 'ftp_host':
                    ftp_host = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'username':
                    ftp_name = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'password':
                    ftp_pwd = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'ftp_path':
                    ftp_path = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'update_dirs':
                    keep_update_dirs = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'exclude_dirs':
                    exclude_dirs = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'root_dir':
                    root_dir = line.split('=')[1].strip()
                else:
                    print('user.conf is a error format. \n')
                    exit(0)
    except IOError as e:
        print('cannot read user.conf file--' + str(e) + ', please create user.conf file. \n')
    if ftp_host == '' or ftp_name == '' or ftp_pwd == '' or root_dir == '' or keep_update_dirs == '':
        print('user.conf is a error format. \n')
        exit(0)
    else:
        return ftp_host, ftp_name, ftp_pwd, ftp_path, keep_update_dirs, exclude_dirs, root_dir


def get_mtime(file_path):
    """" return a datetime data structure """
    from os.path import getmtime
    from time import localtime
    from time import mktime
    from datetime import datetime

    tl = localtime(getmtime(file_path))
    dt = datetime.fromtimestamp(mktime(tl))
    return dt

def autoupdateftp():
    ftp_host, ftp_name, ftp_pwd, ftp_path, keep_update_dirs, exclude_dirs, root_dir = read_conf()
    from ftputil import FTPHost
    from ftputil.error import FTPError
    from ftputil.error import TemporaryError
    try:
        ftp_s = FTPHost(ftp_host, ftp_name, ftp_pwd)
    except FTPError as e:
        print('cannot connect ftp sever ---- ' + str(e))
        exit(0)
    if ftp_path != '/':
        ftp_s.chdir(ftp_path)
    try:
        ftp_s.keep_alive()
    except TemporaryError as e:
        print('Program execute exception ---- ' + str(e))
        exit(0)
    import os
    if keep_update_dirs == '/':
        if exclude_dirs != '':
            download_file(ftp_s, keep_update_dirs, root_dir, exclude_dirs)
        else:
            download_file(ftp_s, keep_update_dirs, root_dir)
    else:
        sdirs = keep_update_dirs.split(',')
        for dir in sdirs:
            download_file(ftp_s, dir.strip(), root_dir+os.sep+dir.strip())

    ftp_s.close()


def download_file(ftp_s, sdir, tdir, edir=''):
    names = ftp_s.listdir(sdir)
    if edir != '':
        names = set(names) - set(edir.split(','))
    for name in names:
        name_c = name.encode('ISO 8859-1').decode('gbk')
        if sdir == '/':
            sdir_a = sdir + name
        else:
            sdir_a = sdir + '/' + name
        print('Scanning the '+ sdir + '/' + name_c + ' ...')
        if ftp_s.path.isdir(sdir_a):
            import os
            if not os.path.exists(tdir+os.sep+name_c):
                os.makedirs(tdir+os.sep+name_c)
            ftp_s.keep_alive()
            download_file(ftp_s, sdir_a, tdir+os.sep+name_c)
        else:
            import os
            ftp_s.download_if_newer(sdir_a, tdir+os.sep+name_c, ftp_s.keep_alive())

if __name__ == "__main__":
    print('Starting to update ftp file, Please wait for ... ')
    autoupdateftp()
    print('Update Finished.')