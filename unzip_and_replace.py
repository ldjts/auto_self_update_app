import os
import shutil
from zipfile import ZipFile
import hashlib


def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            h.update(chunk)
    return h.hexdigest()


# 检查文件完整性
if hash_file("temp/MyApp_mac_Version-1.0.zip") == "3fc4ca36f14a42f4264afc9af46f3fd8c7ea83e3e28b49d11017b13580bdfe13":

    # upzip
    with ZipFile("temp/MyApp_mac_Version-2.0.zip", 'r') as zip_obj:
        zip_obj.extractall('temp')

    # 将root_src_dir目录下所有文件夹及文件移动至root_dst_dir,若有冲突则覆盖
    root_src_dir = 'temp/MyApp_mac_Version-2.0'
    root_dst_dir = 'app'
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file in files:
            src_file = os.path.join(src_dir, file)
            dst_file = os.path.join(dst_dir, file)
            if os.path.exists(dst_file):
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)

    # 删除temp中所有内容
    shutil.rmtree('temp')
    os.makedirs("temp")
