# 13. Automate Database Backups
import subprocess


def backup_mysql(user, password, db_name, output):
    cmd = f"mysqldump -u {user} -p {password} {db_name} > {output}"
    subprocess.run(cmd, shell=True)
