#!/usr/bin/env python2
# coding: utf-8
from apesmit import Sitemap
'''
http://python-3.ru/page/generate-sitemap-xml-in-python
'''
# Ставим значение частоты изменении для всех ссылок
#sm = Sitemap(changefreq='weekly')
sm = Sitemap(changefreq='monthly')

# Добавляем обычную сссылку, указываем индивидульно приоритет
sm.add('http://blog.dtulyakov.ru/', priority=1.0)
# Добавляем ссылку с измененым параметром последнего изменения
#sm.add('http://python-3.ru/page/send-sms-python', lastmod='today')

#sm.add('http://python-3.ru/category/sqlite', changefreq='daily', priority=1.0, lastmod='2015-07-23')

# Создаем файл sitemap в текущею папку скрипта
out=open('sitemap.xml', 'w')
# записываем данные
sm.write(out)
# закрываем файл
out.close()