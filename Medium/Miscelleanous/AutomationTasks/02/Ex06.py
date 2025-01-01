# 06. Automate Backup Creation
import shutil


def create_backup(source_dir, backup_file):
    shutil.make_archive(backup_file, 'zip', source_dir)
