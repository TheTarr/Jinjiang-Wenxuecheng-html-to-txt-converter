from bs4 import BeautifulSoup
import os


def convert(link):
    # Creating soup
    soup = BeautifulSoup(link.read())

    # Fetching the title
    title = soup.title.string
    txt_title = "./converted/" + title.replace(" —— 晋江文学城网友交流区", "") + ".txt"

    # Creating txt file
    write_file = open(txt_title, 'w')

    # Write the topic
    topic_chapter = str(soup.find("div", {"id": "topic"})).replace("<br/>", "\n").replace('<div id="topic">',
                                                                                          "").replace('</div>',
                                                                                                      "").replace(
        u'\xa0', u' ').replace("\n\n\n", "\n")
    write_file.write(topic_chapter)

    # Find multiple chapters
    all_comment = soup.find_all("td", {"class": "read"})
    for i in range(1, len(all_comment)):
        uncleaned_str = str(all_comment[i])
        if len(uncleaned_str) > 400:
            cleaned_str = uncleaned_str.replace('<td class="read">', "").replace('</td>', "").replace("<br/>",
                                                                                                      "\n").replace(
                u'\xa0', u' ').replace("\n\n\n", "\n")
            write_file.write(cleaned_str)

    # Close the file
    write_file.close()


# TODO Importing file
outer_flag = True
while outer_flag:
    print("按q退出程序")
    print("请选择转单个html文件，或转一个包含html文件的文件夹")
    print("转单个文件请输入s并回车，转文件夹请输入d并回车")
    choice = str(input("s/d/q："))
    if choice == "s":
        flag = True
        while flag:
            print("请输入文件目录，按q退出")
            file = str(input("如”C:/Users/x5/Desktop/mutiple_chapter.html“："))
            if file == "q":
                flag = False
            link = open(file)
            convert(link)
    elif choice == "d":
        print("请输入文件夹目录")
        file_dir = str(input("如”C:/Users/x5/Desktop/36大院pp球/："))
        for root, dirs, files in os.walk(file_dir):
            for i in files:
                file = file_dir + i
                try:
                    link = open(file)
                    convert(link)
                except:
                    print("unable to transform:" + i)
                    pass
    else:
        outer_flag = False
print("end")

