# Итоговая проверочная работа I четверти факультета Разработчик

<hr>

## Задача
<hr>
<p>Написать программу, которая из имеющегося массива строк сформирует массив из строк,
длина которых меньше или равна 3 символам.</p>
<p>Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. </p>
В проекте должны быть:

* Блок-схема алгоритма
* Файл README.md
* Программа, решающая поставленную задачу.

## Решение
<hr>

1. Блок-схема содержится в файле diagram.drawio.pdf
2. Наличие файла README.md - есть.
3. Решение программы в файле task.py

### Описание решения

Т.к. в задании не упоминается конкретный язык программирования, для решения  задачи выбран Python версии 3.8.  

В начале выполнения программы у пользователя спрашивается, желает ли он самостоятельно ввести элементы массива или нет.

Если пользователь отвечает согласием, то ему предлагается ввести строки через пробел.

Если отказывается - программа изпользует заранее заданный массив.

Далее программа фильтрует полученный массив и возвращает новый массив, в котором длины элементов равны 3 символам и менее.

Далее программа завершает работу. 