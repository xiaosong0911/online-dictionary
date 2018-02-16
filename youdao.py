import xml.etree.ElementTree as ET
def getEntry(word):
    content = requests.get('http://dict.youdao.com/fsearch?q='
            + word).content.decode('utf-8')
    tree = ET.ElementTree(ET.fromstring(content))

    ret = ''
    for node in tree.findall('.//return-phrase'):
        if node.text:
            ret += node.text + '\n'
    for node in tree.findall('.//phonetic-symbol'):
        if node.text:
            ret += '/' + node.text + '/' + '\n'
    for node in tree.findall('.//translation/content'):
        if node.text:
            ret += '\t'+ node.text + '\n'
    ret += '\n'
    ret += '[from internet]' + '\n'
    for node in tree.findall('.//yodao-web-dict/web-translation'):
        ret += '-' + node.find('key').text + '\n'
        for node in node.findall('trans/value'):
            if node.text:
                ret += '\t' + node.text + '\n'
    return ret
