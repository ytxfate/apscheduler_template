try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# ========================================================== #
# 每个element对象都具有以下属性：
# 1. tag：string对象，表示数据代表的种类。
# 2. attrib：dictionary对象，表示附有的属性。
# 3. text：string对象，表示element的内容。
# 4. tail：string对象，表示element闭合之后的尾迹。
# <tag attrib1=1>text</tag>tail
# ========================================================== #

''' temp.xml 文件内容如下
<?xml version="1.0" encoding="utf-8"?>

<root_tag root_attrib="root_attrib1"> 
  <son_tag son_attrib="son_attrib1">son_text</son_tag>son_tail
</root_tag>
'''
with open('temp.xml', 'r', encoding='utf-8') as f:
    xml_str = f.read()
    root = ET.fromstring(xml_str)
    print("root:")
    print("    root.tag    ==> " + root.tag)
    print("    root.attrib ==> " + str(root.attrib))
    print('son :')
    for son in root:
        print("    son.tag     ==> " + son.tag)
        print("    son.attrib  ==> " + str(son.attrib))
        print("    son.text    ==> " + son.text)
        print("    son.tail    ==> " + son.tail)
