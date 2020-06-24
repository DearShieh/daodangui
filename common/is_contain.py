'''
    python3报错
    暂未解决
'''
import json
from filecmp import cmp
from idna import unicode


class IsContain:
    '''
        判断一个字符串是否在另一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
    '''

    def is_contain(self, str_one, str_two):
        flag = None
        if isinstance(str_one, unicode):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
        # if isinstance(str_two, unicode):
        #     str_two = str_two.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag


    # 判断两个字典是否相等
    def is_equal(self, dict_one, dict_two):
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return cmp(dict_one, dict_two)
