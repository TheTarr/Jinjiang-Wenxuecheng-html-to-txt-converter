from bs4 import BeautifulSoup

def convert(link):
    # Creating soup
    soup = BeautifulSoup(link.read())

    # Fetching the title
    title = soup.title.string
    txt_title = "./converted/" + title.replace(" —— 晋江文学城网友交流区", "") + ".txt"

    # Creating txt file
    write_file = open(txt_title, 'w')

    # Write the topic
    topic_chapter = str(soup.find("div", {"id": "topic"})).replace("<br/>", "\n").replace('<div id="topic">', "").replace('</div>', "").replace(u'\xa0', u' ').replace("\n\n\n", "\n")
    write_file.write(topic_chapter)

    # Find multiple chapters
    all_comment = soup.find_all("td", {"class": "read"})
    for i in range(1, len(all_comment)):
        uncleaned_str = str(all_comment[i])
        if len(uncleaned_str) > 400:
            cleaned_str = uncleaned_str.replace('<td class="read">', "").replace('</td>', "").replace("<br/>", "\n").replace(u'\xa0', u' ').replace("\n\n\n", "\n")
            write_file.write(cleaned_str)

    # Close the file
    write_file.close()

# TODO Importing file
file = str(input("请复制html文件目录，如”C:/Users/x5/Desktop/mutiple_chapter.html“："))
link = open(file)
convert(link)

# flag = 1
# while flag == 1:
#     file = str(input("请复制html文件目录，如”C:/Users/x5/Desktop/mutiple_chapter.html“："))
#     link = open(file)
#     convert(link)
#     flag = int(input("继续转化打1，退出程序打0："))
