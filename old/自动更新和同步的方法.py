import ftputil
with ftputil.FTPHost('014.3vftp.com', 'wdc63', '2224005wdc') as ftp_host:
    print(ftp_host.listdir(ftp_host.curdir))
    # ftp_host.set_time_shift(-43200)
    try:
        ftp_host.mkdir('RPG')
    except:
        pass
    ftp_host.chdir('/RPG')
    print(ftp_host.listdir(ftp_host.curdir))

    if ftp_host.upload_if_newer('D:/MyRPG/data.dat','/RPG/data.dat'):
        pass
    else:
        ftp_host.download_if_newer('/RPG/data.dat','D:/MyRPG/data.dat')
    print(ftp_host.listdir(ftp_host.curdir))




