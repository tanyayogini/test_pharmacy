import json


def convert(filename, model, ready_filename):
    """Функция конвертирует json в файл со структурой, подходящий для загрузки в базу данных"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    result = []
    for product in data:
        result.append({"model": model, "fields": product})

        result.append({"model": model, "fields": product})

    with open(ready_filename, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))

if __name__=='__main__':
    convert('tovar.json', 'products.product', 'tovar_ready.json')
    convert('client_tovar.json', 'products.productclient', 'tovar_client_ready.json')
