from bs4 import BeautifulSoup
import os
import glob

base_file = r'D:\E-Learning\Mastering Redux\9781789535839'


def get_vide_and_title(htmlFile=''):
    temp_file = base_file + '\Package\index.html'
    data_soup = BeautifulSoup(open(temp_file), "html.parser")
    # nameBlock = [name for name in
    #              (div.find('h1') for div in data_soup.find_all("div", {"class": "chapter"}))]
    div_block = data_soup.find_all("div", {"class": "chapter"})

    nameList = []
    fileList = []
    for chapterList in div_block:
        for title in chapterList.find_all('h1'):
            name = (title.get_text().replace('?', '').replace('/', '-')
                    .replace('"', '').replace(':', '-').replace('>', '').replace('<', '').replace('*', '')
                    .replace('\t', ' ')
                    .strip('\t\n\r'))
            nameList.append(name)
    for chapterList in div_block:
        for fileName in chapterList.find_all('a'):
            file = (fileName['href'][7:])
            fileList.append(file)

    kk = dict(zip(fileList, nameList))
    current_file_list = changeName()
    video_path = base_file + '\Package\\videos'
    video_path = video_path.replace('\\', '/')
    # old_file = os.path.join(video_path, "a.txt")
    # print(old_file)
    for item in current_file_list:
        if item in kk.keys():
            old_file = os.path.join(video_path, item)
            new_file = os.path.join(video_path, '{}.mp4'.format(kk[item]))
            os.rename(old_file, new_file)
        # print(old_file)

        # if item in kk.keys:
        #     os.rename(item, kk[item])


def changeName():
    video_path = base_file + '\Package\\videos\*.mp4'
    video_path = video_path.replace('\\', '/')
    file_name = [os.path.basename(x) for x in glob.glob(video_path)]
    return file_name


if __name__ == "__main__":
    get_vide_and_title()
