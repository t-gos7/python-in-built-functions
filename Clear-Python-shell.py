'''
This is a system independent function to clear Python shell. 
@author: Tarit Goswami
@date: 20-03-2020
@language: Python 3.6
'''

def clear():
  '''Function to clear Python shell, independent of system'''
  yn = input('Everything you have written in this shell will be removed, Are you sure? Y/N\n  ')
  if yn == 'Y' or yn == 'y':
    from time import sleep
    if os.name == 'posix':
      from subprocess import call
      sleep(3)
      _ = call('clear', shell=True)
    elif os.name == 'nt':
      import os
      sleep(3)
      _ = os.system('CLS')
clear()
   
