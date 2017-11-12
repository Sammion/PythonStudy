from xml.dom.minidom import parse
import xml.dom.minidom

doc = xml.dom.minidom.Document()

doc.appendChild(doc.createComment("This is a simple xml."))
# 创建根标签booklist
booklist = doc.createElement("booklist")
doc.appendChild(booklist)


# 组织根标签下面的各个子标签和属性。
def addBook(newbook):
    book = doc.createElement("book")
    book.setAttribute("id", newbook["id"])
    title = doc.createElement("title")
    title.appendChild(doc.createTextNode(newbook["title"]))
    book.appendChild(title)
    author = doc.createElement("author")
    name = doc.createElement("name")
    firstname = doc.createElement("firstname")
    firstname.appendChild(doc.createTextNode(newbook["firstname"]))
    lastname = doc.createElement("lastname")
    lastname.appendChild(doc.createTextNode(newbook["lastname"]))
    name.appendChild(firstname)
    name.appendChild(lastname)
    author.appendChild(name)
    book.appendChild(author)
    pubdate = doc.createElement("pubdate")
    pubdate.appendChild(doc.createTextNode(newbook["pubdate"]))
    book.appendChild(pubdate)
    booklist.appendChild(book)
# 向加doc中数据
addBook({"id": "1001", "title": "An apple", "firstname": "Peter", "lastname": "Zhang", "pubdate": "2012-1-12"})
addBook({"id": "1002", "title": "Love", "firstname": "Mike", "lastname": "Li", "pubdate": "2012-1-10"})
addBook({"id": "1003", "title": "Steve.Jobs", "firstname": "Tom", "lastname": "Wang", "pubdate": "2012-1-19"})
addBook({"id": "1004", "title": "Harry Potter", "firstname": "Peter", "lastname": "Chen", "pubdate": "2012-11-11"})
# 不能用file，要用open函数

with open("../data/book.xml", "w") as f:
    doc.writexml(f)
    # 避免直接写入文件而没有格式化
    # f.write(doc.toprettyxml(indent="\t", newl="\n", encoding="UTF-8"))
f.close()
