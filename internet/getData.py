import requests
from tqdm import tqdm
video_url="http://51.255.94.107/Hitou Meguri Kakure Yu Mao Hen 1 Raw.mp4"

if requests.head(video_url).status_code == 302 :
    video_url = requests.head(video_url).headers["Location"]
file_size = int(requests.head(video_url).headers["content-length"])

response = requests.get(video_url,stream=True)


with open("check3.mp4","wb") as file:
    pbar = tqdm(total=file_size, unit="B", unit_scale=True)
    for chunk in response.iter_content(chunk_size=1024):
        ff= file.write(chunk)
        pbar.update(len(chunk))
    pbar.close()
print('Done!')
