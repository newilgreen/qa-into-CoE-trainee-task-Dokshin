import json
# json потребуется для манипуляций с входными и выходными фаилами
import sys 
# sys потребуется для прекращения работы программы после обнаружения ошибки

def new_test(ts):
    # функция new_test(ts) основная часть программы
    # она заполняет TestcaseStructure.json згначениями из Values.json
    # ts - это декодированый TestcaseStructure.json из формата json в dist
    first_chek_p(ts)
    params = ts['params']
    for i in range(len(params)):
        onei(params[i], 'TestcaseStructure.json')
        onev_ts(params[i])
        onet(params[i], 'TestcaseStructure.json')
        if 'values' in params[i]:
            value_chek(params[i]['values'], 'values', 'TestcaseStructure.json')
            values1 = params[i]['values'] 
            for z in range(len(values1)):
                onei(values1[z], 'TestcaseStructure.json')
                onet(values1[z], 'TestcaseStructure.json')
                if 'params' in values1[z]:
                    new_test(values1[z])
                    hard_case(vs,params,i,z)
                else:
                    hard_case(vs,params,i,z)
        else:
            easy_case(vs,params,i)

def easy_case(vs, params, i):
    # функция easy_case(vs, params, i) записывает значения value, если нет values
    # vs - это декодированый Values.json из формата json в dist
    # params - это основной элемент из TestcaseStructure.json
    # i - номер основного элемента  
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
        if flag == 1:
            break

def hard_case(vs, params, i, z):
    # функция hard_case(vs, params, i, z) записывает значения value, если есть values
    # vs - это декодированый Values.json из формата json в dist
    # params - это основной элемент из TestcaseStructure.json
    # i - номер основного элемента(params) 
    # z - номер элемента values
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
        if flag == 1:
            break


def validate(filename, error_str):
    # функция validate(filename, error_str) проводит проверку на возможность декодировать входной фаил
    # filename - входной фаил
    # error_str - словарь показывающий информацию об ошибке
    with open(filename) as file:
        try:
            return json.load(file) 
        except :
            print_error_file(error_str)


def print_error_file(error_str):
    # функция print_error_file(error_str) выводит фаил error.json, сообщающий об ошибке
    # error_str - словарь показывающий информацию об ошибке
    error_file = open('error.json', mode='w', encoding="utf-8")
    error_file.write(json.dumps(error_str, indent=2, ensure_ascii=False))
    sys.exit()


def print_new_file(dist):
    # функуция print_new_file(dist) записывает фаил StructureWithValues.json
    # dist - словарь который требуется записать в фаил 
    new_file = open('StructureWithValues.json', mode='w', encoding="utf-8")
    new_file.write(json.dumps(dist, indent=2, ensure_ascii=False))


def onei(dist, location):
    # функуция onei(dist) проверяет наличие ключевого параметра id
    # dist - словарь который требуется проверить 
    if 'id' not in dist:
        print_error_file(get_error(error_base, location, 1, 'id'))
    else:
        value_chek(dist['id'], "id", location)


def onev_ts(dist):
    # функуция onev(dist) проверяет наличие ключевого параметра value 
    # dist - словарь часть TestcaseStructure.json
    if 'value' not in dist:
        print_error_file(get_error(error_base, 'TestcaseStructure.json', 1, 'value'))


def onev_vs(dist):
    # функуция onev(dist) проверяет наличие ключевого параметра value 
    # dist - словарь часть Values.json
    if 'value' not in dist:
        print_error_file(get_error(error_base, 'Values.json', 1, 'value'))
    else:
        value_chek(dist['value'], 'value', 'Values.json')


def onet(dist, location):
    # функуция onet(dist) проверяет наличие ключевого параметра title 
    # dist - словарь который требуется проверить 
    if 'title' not in dist:
        print_error_file(get_error(error_base, 'TestcaseStructure.json', 1, 'title'))
    else:
        value_chek(dist['title'], 'title', location)


def first_chek_p(dist):
    # функуция first_chek_p(dist) проверяет наличие ключевого параметра 'params'
    # dist - 'TestcaseStructure.json' 
    if 'params' not in dist:
        print_error_file(get_error(error_base, 'TestcaseStructure.json', 1, 'params'))


def first_chek_v(dist):
    # функуция first_chek_v(dist) проверяет наличие ключевого параметра 'values'
    # dist - 'Values.json' 
    if 'values' not in dist:
        print_error_file(get_error(error_base, 'Values.json', 1, 'values'))
    else:
        for j in range(len(dist['values'])):
            onei(dist['values'][j], 'Values.json')
            onev_vs(dist['values'][j])


def value_value(value):
    # функуция value_value(value) проверяет пусты ли значение value в TestcaseStructure.json
    # value - проверяемое значение
    if value != "":
        print_error_file(get_error(error_base, 'TestcaseStructure.json', 2, 'value is not null'))


def value_chek(value, spf, location):
    # функуция value_chek(value) проверяет не пуст ли ключевой параметр(id,title,values)
    # value - проверяемое значение
    if value == "":
        print_error_file(get_error(error_base, location, 3, spf))


def get_error(error_base, location, i, spf):
    # функция get_error(error_base, location, i, spf) формерует сообщение об ошибке
    # на входе незаполенный словарь error_base
    # location = location
    # i = id
    # spf = specifically
    # на выходе заполенный словарь error_base в соотвествии с ошибкой 
    # в котором:
    #   id - идентификатор ошибки
    #   location - фаил в котором обнаружена ошибка
    #   title - тип ошибки
    #   specifically - уточнение
    #   message - сообщение об ошибке  
    error_base["error"]["id"] = i
    error_base["error"]["location"] = location
    if i == 0:
        error_base["error"]["title"] = "file defect"
        error_base["error"]["specifically"] = spf
        error_base["error"]["message"] = "Невозможно декодировать один из фаилов"
    elif i == 1:
        error_base["error"]["title"] = "value defect"
        error_base["error"]["specifically"] = spf
        error_base["error"]["message"] = "Ключевой параметр не обнаружен"
    elif i == 2:
        error_base["error"]["title"] = "value defect"
        error_base["error"]["specifically"] = spf
        error_base["error"]["message"] = "Поля value в TestcaseStructure должны быть пустыми"
    elif i == 3:
        error_base["error"]["title"] = "value defect"
        error_base["error"]["specifically"] = spf
        error_base["error"]["message"] = "Поле ключевого параметра является пустым"
    else:
        error_base["error"]["title"] = "???"
        error_base["error"]["specifically"] = "???"
        error_base["error"]["message"] = "???"

    return error_base


error_base = {"error" : {"id" : "", "title" : "", "specifically" : "", "location" : "", "message" : ""}}

validate('TestcaseStructure.json', get_error(error_base, 'TestcaseStructure.json', 0, 'file'))
validate('Values.json', get_error(error_base, 'Values.json', 0, 'file'))

ts = json.loads(open('TestcaseStructure.json' ,mode='r', encoding="utf-8").read())
vs = json.loads(open('Values.json' ,mode='r', encoding="utf-8").read())

first_chek_v(vs)

new_test(ts)
print_new_file(ts)
# dist = ts на входе это TestcaseStructure.json 
# с заполеными значениями Vaules из Values.json
