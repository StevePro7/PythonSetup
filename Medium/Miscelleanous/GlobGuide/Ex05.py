# 5. Filtering by File Size or Date
import os
import datetime
import glob

files = [f for f in glob.glob("*.txt") if datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(f)) < datetime.timedelta(days=7)]
print(files)