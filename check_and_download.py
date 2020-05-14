import urllib.request


PROJECT_URL = "https://github.com/ldjts/auto_self_update_app"
current_version = "Version-0.0"


print(f"当前版本{current_version}")
print("检查更新")
start_url = PROJECT_URL + "/releases/latest"
req = urllib.request.Request(start_url)
res = urllib.request.urlopen(req)
final_url = res.geturl()
version = final_url.split("/")[-1]
if version != current_version:
    print(f"发现新版本{version}")
    download_url = PROJECT_URL + f"/releases/download/{version}/MyApp_mac_{version}.zip"
    print(f"正在下载新版本，地址：{download_url}")
    urllib.request.urlretrieve(download_url, f'temp/MyApp_mac_{version}.zip')
    print("下载完毕")
else:
    print("暂无新版本")
