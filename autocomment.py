# -*- coding: utf-8 -*-
#
#  autocomment.py
#  
#  Copyright 2020 yogesh <yogeshlmc3@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import pyautogui
import time
# add your requied text here in comments
comments = ["be","ready","and","you","must","do","this","after","completing","100","comments","and","post","a","screenshot","in","this","post","okay","."]
# provides 5 seconds of time to select a post in which to comment after running the script
time.sleep(5)

for i in range(100):#(100 is the number of comments  to be done! change according as your desire.
    pyautogui.typewrite(comments[i%20])# 20 is the number of texts in the comment above, change accordingly how many texts do you have.
    pyautogui.typewrite("\n")
    time.sleep(2)# sleeps for 2 seconds before commenting next comment
