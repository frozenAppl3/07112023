# First use the following commands
# sudo apt update
# sudo apt install vsftpd
# sudo systemctl start vsftpd
# sudo systemctl enable vsftpd
# This will setup the FTP server
# After the above steps, you can use the following code

from ftplib import FTP

ftp_server = 'ftp.example.com'
ftp_username = 'your_username'
ftp_password = 'your_password'

ftp = FTP(ftp_server)
ftp.login(ftp_username, ftp_password)


ftp.retrlines('LIST')

remote_directory = '/path/to/remote/directory'
ftp.cwd(remote_directory)

local_file_path = 'local_file.txt'
remote_file_name = 'remote_file.txt'
with open(local_file_path, 'rb') as local_file:
	ftp.storbinary(f'STOR {remote_file_name}', local_file)

downloaded_file_path = 'downloaded_file.txt'
with open(downloaded_file_path, 'wb') as local_file:
	ftp.retrbinary(f'RETR {remote_file_name}', local_file.write)

ftp.quit()
