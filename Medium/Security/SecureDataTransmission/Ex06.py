# 6. Secure File Transfers (SFTP and SCP)
import paramiko

# Init SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('hostname', username='user', password='pass')

# Init SFTP
sftp = ssh.open_sftp()
sftp.put('/local/path/file.txt', '/remote/path/file.txt')
sftp.close()
ssh.close()