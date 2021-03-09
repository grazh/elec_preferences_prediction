## Влияние академических результатов студентов на выбор курса Эконометрика-2
### Выполнили

* [grazh](https://github.com/grazh)
* [supervo1d](https://github.com/superVo1d)

### Цель проекта
- исследовать влияние академических результатов студента на выбор им курса «Эконометрика-2».

### Краткое описание
Имея в своем распоряжении данные о всех предметах, мы решили ограничиться лишь обязательными для всех студентов математическими дисциплинами, успешность прохождения которых может влиять на выбор студентом курса «Эконометрика-2». Помимо этого, были выбраны переменные отвечающие за номер группы и количество пересдач, как параметры, отражающие общее отношение к учебе студента на протяжении всего времени обучения.
В файле students_data.xlsx имеются следующие данные о 253 студентах третьего курса экономического факультета: birth — год рождения студента, contract — бинарная переменная, равная единице для студентов обучающихся на платной основе и нулю для бюджетников, group — номер группы, retest — количество пересдач студента по всем пройденным дисциплинам за всё время обучения, linal1 — оценка студента по курсу «Линейная алгебра-1», terver — оценка студента по курсу «Теория вероятностей», matstat — оценка студента по курсу «Математическая статистика», ecm1— оценка студента по курсу «Эконометрика-1», и ecm2 — бинарная переменная, равная единице для студентов записанных на курс «Эконометрика-2» и нулю для остальных.
Все данные о студентах предоставлены администрацией экономического факультета МГУ в условиях строгой конфиденциальности.
Начнем с предварительного анализа данных. В табл. 1 представлены описательные статистики для анализируемых переменных.