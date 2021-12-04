import time
from config import Config
'''1-正向最大匹配简单实现'''


# 加载普通词典
def load_dict(path):
    dic = {}
    max_length = 0
    with open(path, encoding='utf8') as f:  # 逐行获取字典信息
        for line in f:
            word = line.split()[0]  # 取出词部分
            dic[word] = 0
            max_length = max(max_length, len(word))  # 动态规划获得最长词长度
    return dic, max_length


# 朴素切分方法
# 先判断最大的数量的字符串在不在词典里，不在的话一个个减少继续判断，两次遍历
# 时间复杂度O(NM):N为字符串长度，M为最大词典词长度；
# 空间复杂度O(N):最坏的情况下每个字都切成一个词
def simple_cut(dic, max_length, input_str):
    res = []
    while input_str != '':
        forward = min(max_length, len(input_str))
        word = input_str[:forward]
        while word not in dic:
            if len(word) == 1:
                break
            word = word[:-1]
        res.append(word)
        input_str = input_str[len(word):]
    return res


'''2-前缀字典的正向最大匹配'''


# 加载前缀字典，0表示是前缀，1表示是真词
def load_prefix_dict(path):
    prefix_dic = {}
    with open(path, encoding='utf8') as f:
        for line in f:
            word = line.split()[0]
            for i in range(1, len(word)):
                if word[:i] not in prefix_dic:
                    prefix_dic[word[:i]] = 0
            prefix_dic[word] = 1
    return prefix_dic


# 前缀字典切分法
# 时间复杂度O(N):N为字符串长度，接近完全前向遍历
# 空间复杂度O(N):最坏的情况下每个字都切成一个词
def prefix_cut(prefix_dict, input_str):
    if input_str == '':
        return []
    words = []
    start, end = 0, 1
    candidate = input_str[0]
    while start < len(input_str) and end <= len(input_str):
        segment = input_str[start:end]
        if segment not in prefix_dict:  # 两种可能，一种是candidate不在前缀字典里，一种是candidate为1的真词才会跳进来更新词
            words.append(candidate)
            start += len(candidate)
            if start == len(input_str):
                break
            candidate = input_str[start]
            end = start + 1
        else:
            if prefix_dict[segment] == 1:  # 前向遍历
                candidate = segment
            end += 1
    if start != len(input_str):
        words.append(candidate)
    return words


# 主函数
def main1(cut_method, output_path, input_path=Config['input_path']):
    word_dic, max_word_length = load_dict(Config['dict_path'])
    output = open(output_path, 'w', encoding='utf8')
    start_time = time.time()
    with open(input_path, encoding='utf8') as f:
        for line in f:
            result = cut_method(word_dic, max_word_length, line.strip())
            output.write(' / '.join(result) + '\n')
    end_time = time.time()
    all_time = end_time - start_time
    output.write('总耗时:%f' % all_time)
    output.close()
    print('朴素分词耗时:', all_time)


# 主函数
def main2(cut_method, output_path, input_path=Config['input_path']):
    prefix_dict = load_prefix_dict(Config['dict_path'])
    output = open(output_path, 'w', encoding='utf8')
    start_time = time.time()
    with open(input_path, encoding='utf8') as f:
        for line in f:
            result = cut_method(prefix_dict, line.strip())
            output.write(' / '.join(result) + '\n')
    end_time = time.time()
    all_time = end_time - start_time
    output.write('总耗时:%f' % all_time)
    output.close()
    print('前缀分词耗时:', all_time)


if __name__ == '__main__':
    test_str = '今天吃北京烤鸭，明天吃烤全羊，后天吃小鸡炖蘑菇！'
    # 测试用例
    # word_dic, max_word_length = load_dict('./data/small_dict.txt')
    # result = simple_cut(word_dic,max_word_length, input_str)
    main1(simple_cut, Config['simple_cut_output_path'])

    # 测试用例
    # prefix_dict = load_prefix_dict('./data/small_dict.txt')
    # result = prefix_cut(prefix_dict, input_str)
    main2(prefix_cut, Config['prefix_cut_output_path'])
