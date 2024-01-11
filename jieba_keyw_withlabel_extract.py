import jieba
jieba.load_userdict('D:\ontology_fire-protection_domain/merged_dict_2.txt') #加载最新的领域自定义字典
import jieba.posseg
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

# 从相关网页上获取信息，并形成txt文件语料；
def html_txt_corpus(web_url, txt_corpus):
    url = web_url
    html = request.urlopen(url).read().decode('utf8')

    raw = BeautifulSoup(html).get_text()
    tokens = sent_tokenize(raw)

    f = open(txt_corpus, 'w+', encoding='utf-8')
    for i in range(0, len(tokens)):
        f.writelines(tokens[i])
        f.write('\n')
    f.close

html_txt_corpus(web_url = "https://b.1190119.com/article-1074.htm",
                txt_corpus='D:\ontology_fire-protection_domain/html_result.txt')


# 使用jieba, 对语料进行自动化的分词和词性标注，并进行一定的数据处理，形成人工校正前的自定义字典
def cut_label_clean(initial_corpus, auto_result, cleaned_result):
    raw = open(initial_corpus, 'r', encoding='UTF-8').read()

    words = jieba.posseg.lcut(raw)
    f = open(auto_result, 'w+', encoding='utf-8')
    for pair in words:
        for word in pair:
            f.write(word)
            f.write('\t')
        f.write('\n')
    f.close

    words_new = []

    for pair in words:
        if pair.flag.startswith('n') or pair.flag.startswith('nr') or pair.flag.startswith(
                'nz') or pair.flag.startswith('f') or pair.flag.startswith('ns') or pair.flag.startswith(
                's') or pair.flag.startswith('nt') or pair.flag.startswith('an') or pair.flag.startswith('vn'):
            words_new.append(pair)

    words_new1 = []

    for pair in words_new:
        if not pair in words_new1:
            words_new1.append(pair)

    f = open(cleaned_result, 'w+', encoding='utf-8')
    for pair in words_new1:
        for word in pair:
            f.write(word)
            f.write('\t')
        f.write('\n')
    f.close


cut_label_clean(initial_corpus='D:\ontology_fire-protection_domain/html_result.txt',
               auto_result='D:\ontology_fire-protection_domain/auto_words.txt',
               cleaned_result='D:\ontology_fire-protection_domain/cleaned_words.txt') #用于人工校正


# 向领域自定义字典增加新词并更新
def merged_dict(dict_1, dict_2):
    f1 = open(dict_1, 'r', encoding='utf-8')
    eachline = f1.readlines()
    print(eachline)

    f2 = open(dict_2, 'r', encoding='utf-8')
    eachline2 = f2.readlines()
    print(eachline2)

    eachline = eachline + eachline2
    print(eachline)

    f1 = open(dict_1, 'w', encoding='utf-8')
    f1.writelines(eachline)
    f1.close()


merged_dict(dict_1='D:\ontology_fire-protection_domain/fire_protection_domain_dict.txt', #防火领域的主自定义字典
            dict_2='D:\ontology_fire-protection_domain/cleaned_words_人工校正.txt') #新输入形成的字典


# 调整领域自定义字典的词频
def justified_dict_freq(initial_dict, freq, justified_dict):
    f1 = open(initial_dict, 'r', encoding='utf-8')
    eachline = f1.readlines()
    print(eachline)
    for i in range(0, len(eachline)):
        eachline[i] = eachline[i].split('\t')
    print(eachline)
    for j in range(0, len(eachline)):
        eachline[j].insert(1, freq)
    print(eachline)
    for k in range(0, len(eachline)):
        eachline[k] = ' '.join(eachline[k])
    print(eachline)
    f1.close()

    f2 = open(justified_dict, 'w+', encoding='utf-8')
    f2.writelines(eachline)
    f2.close()


justified_dict_freq(initial_dict='D:\ontology_fire-protection_domain/fire_protection_domain_dict.txt', #防火领域的主自定义字典
               freq='70000',
               justified_dict='D:\ontology_fire-protection_domain/fire_protection_domain_dict_2.txt') #调整词频后的主自定义字典


#词性标注后的词抽取出现频率最高的前50个
#tags = jieba.analyse.extract_tags(words, topK=50)
#print(",".join(tags))
