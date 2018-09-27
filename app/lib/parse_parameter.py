# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/7 下午4:22
# @File   : parse_parameter.py

globalmap = {
    'str_success':'$s:200'
}

reqmap = {

}

globaljson = {
    'ec':1,
    'em':'success',
    'data':{
        'list':[
            {
                'name':'a',
                'age':18
            },
            {
                'name': 'b',
                'age': 19
            },
            {
                'name': 'c',
                'age': 20
            }
        ]
    }
}

def parse_by_type(s):
    '''
    assert_type() used for declare the type of this parameter,
    the offical format like that
    [string,num:]parameter
    string is default, if parameter is int type or float type, [] need
    declare num type explicitly.
    if this parameter isnot correspond with the input format, it would deal
    with string type.
    '''
    if s.isnumeric():
        return int(s)
    else:
        try:
            float(s)
        except ValueError:
            pass
        else:
            return float(s)

    try:
        cut_index = s.index(':')
    except ValueError:
        return s
    else:
        s_start = s[:cut_index]
        s_end = s[cut_index+1:]

        if s_start in ('$string','$s'):
            return str(s[cut_index+1:])
        elif s_start in ('$num','$n'):
            try:
                input_class = type(eval(s_end))
            except SyntaxError:
                print('指定类型错误，\'{}\'不能转化成number类型。'.format(s_end))
            else:
                if input_class == int:
                    return int(s_end)
                elif input_class == float:
                    return float(s_end)
                else:
                    print('number类型只能支持整型和浮点型。')
        elif s_start in ('$global','$g'):
            if s_end in globalmap.keys():
                return parse_by_type(globalmap.get(s_end))
            else:
                return None
        elif s_start in ('$map','$m'):
            if s_end in reqmap.keys():
                return parse_by_type(reqmap.get(s_end))
        else:
            return s

def parse_by_json(result,result_extraction):

    if result_extraction[0] and result_extraction[0] == '$':
        result_extraction = result_extraction[1:]
    else:
        return result_extraction

    try:
        extraction_nodes = result_extraction.split('.')
    except TypeError as e:
        return None
    current_result = result

    for node in extraction_nodes:

        if node.isnumeric() and isinstance(current_result,list) and int(node) < len(current_result):
            current_result = current_result[int(node)]
        elif isinstance(current_result,dict) and node in current_result.keys():
            current_result = current_result.get(node)
        else:
            return None

    return current_result

def parse_by_star_order(result, star_extraction):
    '''
    :param result: 返回结果的json
    :param star_extraction: 用于排序断言，星号表达式提取
    :return: 星号表达式提取的list
    '''

    if star_extraction[0] and star_extraction[0] == '$':
        star_extraction = star_extraction[1:]
    else:
        return star_extraction

    try:
        extraction_nodes = star_extraction.split('.')
    except TypeError as e:
        return None
    current_result = result

    for node in extraction_nodes:

        if node.isnumeric() and isinstance(current_result,list) and int(node) < len(current_result):
            current_result = current_result[int(node)]
        elif isinstance(current_result,dict) and node in current_result.keys():
            current_result = current_result.get(node)
        elif node == '*' and isinstance(current_result, list):
            star_value = star_extraction[star_extraction.index('*.')+2:]
            if len(current_result) == 0:
                return []

            return [parse_by_json(current_result[index],'$'+star_value) for index in range(len(current_result))]

        else:
            return None

    return current_result

