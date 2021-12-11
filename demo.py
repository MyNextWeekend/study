# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 12:26
# @Author  : hejinhu
class aaa:
    @classmethod
    def bbb(cls):
        print('这个是bbb')

    @staticmethod
    def ccc():
        print('这个是ccc')

    def __init__(self):
        print('这个是init')

    def ddd(self):
        print('这个是普通方法ddd')

    def __new__(cls, *args, **kwargs):
        print('这个是new')
        return super(cls, aaa).__new__(cls)


if __name__ == '__main__':
    aaa.bbb()
    aaa.ccc()
    aaa()
    aaa().ddd()
