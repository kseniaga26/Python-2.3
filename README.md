# Python-2.3

##Решение задания 2.3.1 находится в файле two_one.

##Решение задания 2.3.2 находится в файле two_one и test.

- Результаты прохождения тестов: 

![image](https://user-images.githubusercontent.com/114469025/207554243-60a53956-73f3-4114-b434-0970d5460533.png)
![image](https://user-images.githubusercontent.com/114469025/207554510-0625a6ff-5f8d-4135-8051-3506b4cb1cc1.png)

![image](https://user-images.githubusercontent.com/114469025/207557402-1060e848-1d1b-4032-8f8a-1d58b3b32752.png)

##Решение задания 2.3.3

В файле two_two создано 3 метода для форматирования даты:

![image](https://user-images.githubusercontent.com/114469025/209449657-cdd8b46c-f18f-4140-a776-1bd8e535c9fd.png)

- Результаты профилизатора для первой функции get_data_1 (35516 ms):

![get_date_1](https://user-images.githubusercontent.com/103308669/206710817-ddc30c0d-37d1-4b11-a7d2-c332b0dbf676.png)

- Результаты профилизатора для второй функции get_data_2 (1053 ms):

![get_date_2](https://user-images.githubusercontent.com/103308669/206710874-7cc4824a-a950-4cbc-a4e3-57e1433792f2.png)

- Результаты профилизатора для третьей функции get_data_3 (295 ms):

![get_date_3](https://user-images.githubusercontent.com/103308669/206710909-425bc5a2-c648-46a6-a438-c426166a5cf8.png)

Последняя функция тратит намного меньше времени, чем первые две. В сравнении с get_data_1 и get_data_2, время уменьшилось в несколько десятков тысяч ms.
Для сокращения времени работы программы необходимо оставить последнюю функцию.

