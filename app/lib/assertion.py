# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/12 下午11:29
# @File   : assertion.py

from app.lib import parse_parameter

result = {
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

'''
等于/不等于   assertEqual/assertNotEqual
大于/小于     assertGreater/assertLess
大于等于/小于等于   assertGE/assertLE
值介于 assertBetween
空/非空    assertIsNone/assertIsNotNone
长度等于/长度不等于  assertLenE/assertLenNE
长度大于/长度小于   assertLenG/assertLenL
长度大于等于/长度小于等于   assertLenGE/assertLenLE
长度介于    assertLenBetween
值在集合中   assertIn
计算表达式eval   assertEval
结果根据某字段升序或者降序   assertOrderAsc/assertOrderDesc
'''

def _assertEqual(actual, expected):

     ret = dict()
     if actual == expected:
         ret['result'] = True
         return ret
     else:
         ret['result'] = False
         ret['msg'] = 'actual {}{} != excepted {}{}'.format(type(actual),actual,type(expected),expected)
         return ret

def _assertNotEqual(actual, expected):
    ret = dict()
    if actual != expected:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {}{} == excepted {}{}'.format(type(actual), actual, type(expected), expected)
        return ret

def _assertGreater(actual, expected):
    ret = dict()
    if actual > expected:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {}{} <= excepted {}{}'.format(type(actual), actual, type(expected), expected)
        return ret

def _assertLess(actual, expected):
    ret = dict()
    if actual < expected:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {}{} >= excepted {}{}'.format(type(actual), actual, type(expected), expected)
        return ret

def _assertGE(actual, expected):
    ret = dict()
    if actual >= expected:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {}{} < excepted {}{}'.format(type(actual), actual, type(expected), expected)
        return ret

def _assertLE(actual, expected):
    ret = dict()
    if actual <= expected:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {}{} > excepted {}{}'.format(type(actual), actual, type(expected), expected)
        return ret

def _assertBetween(actual, expected_min, expected_max):
    ret = dict()
    if actual >= expected_min and actual <= expected_max:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {} not between excepted [{}{}]'.format(actual, expected_min, expected_max)
        return ret

def _assertIsNone(acutal):

    ret = dict()

    if acutal == () or acutal == [] or acutal == {}:
        ret['result'] = True
        return ret
    else:
        ret['result'] = False
        ret['msg'] = 'actual {} is not None.'.format(acutal)
        return ret

def _assertIsNotNone(acutal):

    ret = dict()

    if acutal == () or acutal == [] or acutal == {}:
        ret['result'] = False
        ret['msg'] = 'actual {} is None.'.format(acutal)
        return ret
    else:
        ret['result'] = True
        return ret

def _assertOrderAsc(actual_list):

    ret = dict()
    if len(actual_list) <= 1:
        ret['result'] = True
        return ret

    for index in range(len(actual_list)-1):
        try:
            if actual_list[index+1] >= actual_list[index]:
                continue
            else:
                ret['result'] = False
                ret['msg'] = 'excepted index({}) {} >= index({}) {}'.format(
                    index+1,actual_list[index+1],index,actual_list[index]
                )
                return ret
        except Exception:
            ret['result'] = False
            ret['msg'] = 'excepted index({}) {} >= index({}) {}'.format(
                index + 1, actual_list[index + 1], index, actual_list[index]
            )
    ret['result'] = True
    return ret

def _assertOrderDesc(actual_list):

    ret = dict()

    if len(actual_list) <= 1:
        ret['result'] = True
        return ret
    else:
        for index in range(len(actual_list)-1):
            try:
                if actual_list[index+1] <= actual_list[index]:
                    continue
                else:
                    ret['result'] = False
                    ret['msg'] = 'excepted index({}) {} <= index({}) {}'.format(
                        index+1,actual_list[index+1],index,actual_list[index]
                    )
                    return ret
            except Exception:
                ret['result'] = False
                ret['msg'] = 'excepted index({}) {} <= index({}) {}'.format(
                    index + 1, actual_list[index + 1], index, actual_list[index]
                )
        ret['result'] = True
        return ret

def _assertLenE(actual_list,length):

    ret = dict()

    if len(actual_list) == length:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} != excepted length {}'.format(len(actual_list),length)
    return ret

def _assertLenNE(actual_list,length):

    ret = dict()

    if len(actual_list) != length:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} == excepted length {}'.format(len(actual_list),length)
    return ret

def _assertLenG(actual_list,length):

    ret = dict()

    if len(actual_list) > length:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} <= excepted length {}'.format(len(actual_list),length)
    return ret

def _assertLenL(actual_list,length):

    ret = dict()

    if len(actual_list) < length:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} >= excepted length {}'.format(len(actual_list),length)
    return ret

def _assertLenGE(actual_list,length):

    ret = dict()

    if len(actual_list) >= length:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} < excepted length {}'.format(len(actual_list),length)
    return ret

def _assertLenLE(actual_list,length):

    ret = dict()

    if len(actual_list) <= length:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} > excepted length {}'.format(len(actual_list),length)
    return ret

def _assertLenBetween(actual_list,minLen,maxLen):

    ret = dict()

    if len(actual_list) >= minLen and len(actual_list) <= maxLen:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual length {} not between {} and {}'.format(len(actual_list),minLen,maxLen)
    return ret

def _assertIn(actual, excepted_list):

    ret = dict()

    parse_type_list = [ parse_parameter.parse_by_type(x) for x in excepted_list ]

    if actual in parse_type_list:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual {} not in list {}'.format(actual,excepted_list)

    return ret

def _assertEval(result, actual, excepted_eval_extraction):

    ret = dict()

    calcu_eval_result = parse_eval(result,excepted_eval_extraction)

    if actual == calcu_eval_result:
        ret['result'] = True
    else:
        ret['result'] = False
        ret['msg'] = 'actual {}{} != excepted {}{}'.format(type(actual),actual,type(calcu_eval_result),calcu_eval_result)
    return ret

def assertResult(result, type , actual ,excepted=None):
    '''
    :param result: 接口返回的json类型的结果
    :param type: 断言类型
    :param actual: 结果提取表达式
    :param excepted: 预期结果：可以为None,number,string,dict
    :return:  返回结果为dict类型，ret['result']为True说明成功，为False说明失败，失败时ret['msg']为失败原因
    '''

    if type == 'assertEqual':
        return _assertEqual(parse_parameter.parse_by_json(result, actual),
                           parse_parameter.parse_by_type(excepted))

    elif type == 'assertNotEqual':
        return _assertNotEqual(parse_parameter.parse_by_json(result, actual),
                            parse_parameter.parse_by_type(excepted))

    elif type == 'assertGreater':
        return _assertGreater(parse_parameter.parse_by_json(result, actual),
                               parse_parameter.parse_by_type(excepted))

    elif type == 'assertLess':
        return _assertLess(parse_parameter.parse_by_json(result, actual),
                               parse_parameter.parse_by_type(excepted))

    elif type == 'assertGE':
        return _assertGE(parse_parameter.parse_by_json(result, actual),
                           parse_parameter.parse_by_type(excepted))

    elif type == 'assertLE':
        return _assertLE(parse_parameter.parse_by_json(result, actual),
                           parse_parameter.parse_by_type(excepted))

    elif type == 'assertBetween':
        return _assertBetween(parse_parameter.parse_by_json(result, actual),
                              parse_parameter.parse_by_type(excepted['min']),
                              parse_parameter.parse_by_type(excepted['max']))

    elif type == 'assertIsNone':
        return _assertIsNone(parse_parameter.parse_by_json(result, actual))

    elif type == 'assertIsNotNone':
        return _assertIsNotNone(parse_parameter.parse_by_json(result, actual))

    elif type == 'assertOrderAsc':
        return _assertOrderAsc(parse_parameter.parse_by_star_order(result,actual))

    elif type == 'assertOrderDesc':
        return _assertOrderDesc(parse_parameter.parse_by_star_order(result,actual))

    elif type == 'assertLenE':
        return _assertLenE(parse_parameter.parse_by_json(result,actual),
                           parse_parameter.parse_by_type(excepted))

    elif type == 'assertLenNE':
        return _assertLenNE(parse_parameter.parse_by_json(result,actual),
                            parse_parameter.parse_by_type(excepted))

    elif type == 'assertLenG':
        return _assertLenG(parse_parameter.parse_by_json(result,actual),
                           parse_parameter.parse_by_type(excepted))

    elif type == 'assertLenL':
        return _assertLenL(parse_parameter.parse_by_json(result,actual),
                           parse_parameter.parse_by_type(excepted))

    elif type == 'assertLenGE':
        return _assertLenGE(parse_parameter.parse_by_json(result,actual),
                            parse_parameter.parse_by_type(excepted))

    elif type == 'assertLenLE':
        return _assertLenLE(parse_parameter.parse_by_json(result,actual),
                            parse_parameter.parse_by_type(excepted))

    elif type == 'assertLenBetween':
        return _assertLenBetween(parse_parameter.parse_by_json(result,actual),
                                 parse_parameter.parse_by_type(excepted['min']),
                                 parse_parameter.parse_by_type(excepted['max']))

    elif type == 'assertIn':
        return _assertIn(parse_parameter.parse_by_json(result,actual),excepted)

    elif type == 'assertEval':
        return _assertEval(result,parse_parameter.parse_by_json(result,actual),
                           excepted)

    else:
        ret = {}
        ret['result'] = False
        ret['msg'] = '断言类型不支持'
        return ret

def parse_eval(result, eval_extraction):
    '''
    :param result: 返回结果json
    :param eval_extraction: 断言计算表达式，可以指定精度格式，$[num]f，num>0
    :return: 指定f,返回指定精度的浮点数，不指定默认返回四舍五入的整数，计算表达式错误或者精度类型格式错误返回None
    '''
    float_precision = 0

    if eval_extraction[0] and eval_extraction[0] == '$' and 'f:' in eval_extraction:

        split_index = eval_extraction.index('f:')

        float_precision = eval_extraction[1:split_index]

        eval_extraction = eval_extraction[split_index + 2:]

        if float_precision.isnumeric() and int(float_precision) > 0:
            float_precision = int(float_precision)
        else:
            return None

    import re
    eval_list = re.split(r"(\+|\-|\*|/|\(|\)|%)",eval_extraction)

    for index in range(0,len(eval_list)):
        if eval_list[index] not in {'+','-','*','/','(',')',''} and not eval_list[index].isnumeric():
            eval_list[index] = parse_parameter.parse_by_json(result,eval_list[index])

    print(eval_list)
    calcu_string = ''
    for i in eval_list:

        if i == None:
            return None

        calcu_string += str(i)

    try:
        result = eval(calcu_string)
    except SyntaxError as e:
        return None
    except TypeError:
        return None

    if float_precision <= 0:
        return int(result)
    else:
        print(float_precision)
        format = "%."+str(float_precision)+"f"
        result = format %result
        return float(result)








