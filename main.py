from pathlib import Path
import os

import convert_image
import convert_to_print
import config


work_dir = os.getcwd()


def get_image_paths():
    os.chdir(work_dir + '\\images')

    paths = []  # список адресов файлов
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.bmp', '.png')):
                paths.append(os.path.join(root, file))
    return paths


def get_names(paths):
    names = []
    folder = os.getcwd()
    for file_path in paths:
        full_name = file_path[len(folder) + 1:]
        name = Path(full_name).stem
        names.append(name)
    return names


def main_menu(names):
    while True:
        print(f'Выберите изображение(введите число от 1 до {len(names)}): ')
        for i in range(len(names)):
            print(f'{i + 1}. {names[i]}')
        try:
            image_num = int(input('Номер изображения: '))
            if not (0 < image_num <= len(names)):
                config.clr_scr()
                print('Такого числа не предложено!!')
            else:
                return image_num
        except ValueError:
            config.clr_scr()
            print('Это не число, бл!!')
            continue


def result(name):
    print(f'''Ваше изображение сохранено в файл "{name}.txt" на рабочий стол.
    Желаете отправить его в документ Docx для печати?''')
    state = input('Да/Нет(y/n): ').lower()
    if state in ['да', 'y']:
        return True
    return False


def main():
    paths = get_image_paths()
    names = get_names(paths)

    if names:
        image_num = main_menu(names) - 1
        config.clr_scr()

        needed_path = paths[image_num]
        name = names[image_num]

        os.chdir(work_dir)
        txt = convert_image.main(needed_path, name)

        if result(name):
            convert_to_print.create_docx(txt, name)
            input('Вы прекрасны! ))')
    else:
        print('ВНИМАНИЕ!!!\nВ папке "images" не найдено ни одного изображения.')


if __name__ == '__main__':
    main()
