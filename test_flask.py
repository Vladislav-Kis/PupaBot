from flask import Flask, request

app = Flask(__name__)

def printt(id):
    print(id, 'робит')

@app.route('/execute_function', methods=['POST'])
def execute_function():
    # Получаем данные из запроса (например, JSON)
    data = request.get_json()

    # Вызываем нужную функцию и передаем ей параметры
    result = printt(data['param'])

    return {'result': result}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # Запуск сервера на порту 5000