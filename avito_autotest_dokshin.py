import json
import sys 

def new_test(ts):
    for params in ts:
        params = ts['params']
        value_chek(params)
        for i in range(len(params)):
            one(params[i])
            onep(params[i])
            if 'values' in params[i]:
                values1 = params[i]['values'] 
                value_chek(values1)
                for z in range(len(values1)):
                    if 'params' in values1[z]:
                        new_test(values1[z])
                        hard_case(vs,params,i,z)
                    else:
                        hard_case(vs,params,i,z)
            else:
                easy_case(vs,params,i)

def easy_case(vs, params, i):
    for values2 in vs:
        values2 = vs['values']
        flag = 0
        for j in range(len(values2)):
            for id in values2[j]:
                if values2[j]['id'] == params[i]['id']:
                    value_value(params[i]['value'])
                    params[i]['value'] = values2[j]['value']
                    flag = 1
                    break
            if flag == 1:
                break

def hard_case(vs, params, i, z):
    for values2 in vs:
        values2 = vs['values']
        flag = 0
        for j in range(len(values2)):
            for id in values2[j]:
                if values2[j]['value'] == params[i]['values'][z]['id']:
                    value_value(params[i]['value'])
                    params[i]['value'] = params[i]['values'][z]['title']
                    flag = 1
                    break
            if flag == 1:
                break

def validate(filename, error_str):
    with open(filename) as file:
        try:
            return json.load(file) 
        except:
            print_error_file(error_str)  

def print_error_file(error_str):
    error_file = open('error.json', mode='w', encoding="utf-8")
    error_file.write(json.dumps(error_str, indent=2, ensure_ascii=False))
    sys.exit()

def print_new_file(dist):
    new_file = open('StructureWithValues.json', mode='w', encoding="utf-8")
    new_file.write(json.dumps(dist, indent=2, ensure_ascii=False))

def one(dist):
    if 'id' not in dist or 'value' not in dist:
        print_error_file(error_str2)
    else:
        value_chek(dist['id'])

def onep(dist):
    if 'title' not in dist:
        print_error_file(error_str2)
    else:
        value_chek(dist['title'])

def value_value(value):
    if value != "":
        print_error_file(error_str3)

def value_chek(value):
    if value == "":
        print_error_file(error_str4)

error_str1 = """
{
    "error": {
        "message": "Входные файлы некорректны, невозможно декодировать один из фаилов"
    }
}"""
error_str1 = json.loads(error_str1)

error_str2 = """
{
    "error": {
        "message": "Входные файлы некорректны, ключевой параметр не обнаружен"
    }
}"""
error_str2 = json.loads(error_str2)

error_str3 = """
{
    "error": {
        "message": "Входные файлы некорректны, поля value в TestcaseStructure должны быть пустыми "
    }
}"""
error_str3 = json.loads(error_str3)

error_str4 = """
{
    "error": {
        "message": "Входные файлы некорректны, поля ключевого параметра является пустым"
    }
}"""
error_str4 = json.loads(error_str4)

error_str5 = """
{
    "error": {
        "message": "Входной файл не найден"
    }
}"""
error_str5 = json.loads(error_str5)

validate('TestcaseStructure.json', error_str1)
validate('Values.json', error_str1)

ts = json.loads(open('TestcaseStructure.json' ,mode='r', encoding="utf-8").read())
vs = json.loads(open('Values.json' ,mode='r', encoding="utf-8").read())

value_chek(vs['values'])
for j in range(len(vs['values'])):
    one(vs['values'][j])

new_test(ts) 
print_new_file(ts)
