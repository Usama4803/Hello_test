import shutil

total, used, free = shutil.disk_usage("/")
print(f"Used: {used // (2**30)} GB")
