specialist = ['Корнеев Эрик Артемьевич', 'Еремина Мария Данииловна', 'Яковлева Полина Арсентьевна', 'Сафонов Марк Егорович', 'Судакова Дарья Степановна', 'Баранова Варвара Николаевна', 'Ларин Андрей Максимович', 'Калашников Лука Львович', 'Захаров Илья Иванович', 'Сорокин Александр Дмитриевич', 'Ильина Вероника Павловна', 'Петров Дмитрий Никитич', 'Климов Андрей Егорович', 'Александрова Анна Николаевна', 'Бондарев Роберт Никитич', 'Захарова Аделина Матвеевна', 'Волков Роберт Максимович', 'Носов Тимур Андреевич', 'Гончарова Кира Александровна', 'Зайцева Ксения Артёмовна', 'Миронов Александр Всеволодович', 'Симонов Даниил Фёдорович', 'Егорова Эвелина Фёдоровна', 'Королев Глеб Тимофеевич', 'Фетисова Виктория Данииловна', 'Иванова Милана Романовна', 'Лазарев Демид Максимович', 'Киселев Максим Георгиевич', 'Яшина Анна Никитична', 'Зиновьев Тимофей Артёмович', 'Быкова Виктория Данииловна', 'Овчинников Владимир Тимофеевич', 'Андреева Мирослава Марковна', 'Пономарева Малика Максимовна', 'Иванова Ульяна Георгиевна', 'Галкин Роман Артемьевич', 'Воронин Андрей Тимофеевич', 'Москвина Кира Владимировна', 'Иванова Ангелина Михайловна', 'Ларина Анна Григорьевна', 'Воронина Мария Михайловна', 'Руднев Егор Демидович', 'Данилова Виктория Сергеевна', 'Макаров Григорий Ярославович', 'Иванова Варвара Васильевна', 'Медведев Демид Егорович', 'Баранов Тимофей Романович', 'Спиридонова Алёна Сергеевна', 'Ульянов Владислав Викторович', 'Миронова Агата Дмитриевна', 'Соколова София Алексеевна', 'Смирнова Малика Евгеньевна', 'Калмыкова Виктория Ильинична', 'Мартынов Тимофей Даниилович', 'Рожкова Полина Юрьевна', 'Елизаров Иван Андреевич', 'Ларионова Аглая Матвеевна', 'Кузнецова Варвара Егоровна', 'Кузьмина Виктория Артёмовна', 'Жданова Дарья Николаевна']
specialist_dict = []

for i in range(len(specialist)):
    specialist_dict.append({'IndividualGUID': f'{i+1}', 'IndividualName': f'{specialist[i]}'})
