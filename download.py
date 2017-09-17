# -*- coding: utf-8 -*-

import wx
import basewin
import re
import requests
import threading

thread_lock = threading.BoundedSemaphore(value=10)


class MainWindow(basewin.Download):#创建主窗口
    def __init__(self, parent):
        basewin.Download.__init__(self, parent)

    def dowmloadPic(self, html, keyword):
        pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
        i = 0
        # self.text_info.SetValue ('找到关键词:'+keyword+'的图片，现在开始下载图片...')
        for each in pic_url:
            # self.text_info.SetValue ('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
            try:
                pic = requests.get(each, timeout=5)
            except requests.exceptions.ConnectionError:
                # self.text_info.SetValue ('【错误】当前图片无法下载')
                continue
            string = 'pictures\\' + keyword + '_' + str(i + 1) + '.jpg'
            # resolve the problem of encode, make sure that chinese name could be store
            with open(string, 'wb') as f:
                f.write(pic.content)
            i += 1
            self.gauge_info.SetValue(i * 2)
            if i >= 50:
                self.text_info.SetValue('下载完成')
                break
                thread_lock.release()

    def button_click(self, event):
        keyword = self.text_search.GetValue()
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&ct=201326592&v=flip'
        result = requests.get(url)
        thread_lock.acquire()
        t = threading.Thread(target=self.dowmloadPic, args=(result.text, keyword))
        t.start()
        # self.dowmloadPic(result.text,keyword)


if __name__ == '__main__':
    app = wx.App()
    download_win = MainWindow(None)
    download_win.Show()
    app.MainLoop()
