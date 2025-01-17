# SVO
SVO - это собственный формат файла для хранения промежуточного представления
изображения, полученного с помощью сингулярного разложения (SVD). Формат предназначен
для эффективного хранения и передачи сжатых изображений.

## Структура файла
1. Заголовок (5 байт)
* `SVO` в ASCII кодировке
2. Данные для красного канала
* Матрица U (размер зависит от размера изображения и параметров SVD)
* Матрица $`V^T`$ (размер зависит от размера изображения и параметров SVD)
3. Данные для зеленого канала
* Матрица U (размер зависит от размера изображения и параметров SVD)
* Диагональная матрица Σ (размер зависит от параметров SVD)
* Матрица $`V^T`$ (размер зависит от размера изображения и параметров SVD)
4. Данные для синего канала       
* Матрица U (размер зависит от размера изображения и параметров SVD)
* Диагональная матрица Σ (размер зависит от параметров SVD)
* Матрица V^T (размер зависит от размера изображения и параметров SVD)

# Эксперимент
Были использованы алгоритмы:
* numpy.linalg
* Степенной метод
* Блочный степенной метод

## Сравнение алгоритмов
### Изображение не высокого качества
Сожмём его с коэффициентом сжатия `0.05`

| исходное                                            | numpy                                                                | power                                                                 | block power                                                           |
|-----------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| ![mozhno.bmp](img%2Fmozhno.bmp) |![mozhnoNP.bmp](compress_img%2FmozhnoNP.bmp) |![mozhnoPower.bmp](compress_img%2FmozhnoPower.bmp) |![mozhnoBlock.bmp](compress_img%2FmozhnoBlock.bmp)

Сравнивая три сжатых изображения большой разницы не видно 

### Изображение с разными цветами
Его уже сожмём с коэффициентом сжатия `0.005`, так как при большем коэффициенте разницы почти не заметить

| исходное                                            | numpy                                                                | power                                                                 | block power                                                           |
|-----------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| ![rainbow.bmp](img%2Frainbow.bmp)|![rainbowNP.bmp](compress_img%2FrainbowNP.bmp)|![rainbowPower.bmp](compress_img%2FrainbowPower.bmp)|![rainbowBlock.bmp](compress_img%2FrainbowBlock.bmp)

Здесь же уже видно, что переход синего в фиолетовый на `Power` методе начинается правее чем в других методах.

### Изображение высокого качества
| исходное                                           | numpy                                                                | power                                                                 | block power                                                           |
|----------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
|![Sutener.bmp](img%2FSutener.bmp)|![SutenerNP.bmp](compress_img%2FSutenerNP.bmp)|![SutenerPower.bmp](compress_img%2FSutenerPower.bmp)|![SutenerBlock.bmp](compress_img%2FSutenerBlock.bmp)

Здесь при коэффициенте `0.05` разницы снова толком никакой нету

### Фигуры
| исходное                                           | numpy                                                                | power                                                                 | block power                                                           |
|----------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
|![shape.bmp](img%2Fshape.bmp)|![shapeNP.bmp](compress_img%2FshapeNP.bmp)|![shapePower.bmp](compress_img%2FshapePower.bmp)|![shapeBlock.bmp](compress_img%2FshapeBlock.bmp)

При сжатии с коэффициентом `0.03` сразу видна разница, в `power` методе, углы некоторых фигур слились с белым фоном

## Вывод
Все методы работают хорошо, но всё же лучший метод `Numpy` из-за скорости