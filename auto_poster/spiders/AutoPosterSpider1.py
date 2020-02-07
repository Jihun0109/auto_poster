#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.utils.response import open_in_browser
from scrapy import Spider, Request, FormRequest
import re, requests, os, time
from scrapy.shell import inspect_response

from scrapy.exceptions import CloseSpider
import mysql.connector

class AutoPosterSpider(Spider):
	name = "autoposter1"

	start_urls = [
			"http://linelab.co.kr/community/community_list.php?table_type=free"
	]

	def __init__(self, post=1, *args, **kw):
		super(AutoPosterSpider, self).__init__(*args, **kw)
		
		self.db_conn = mysql.connector.connect(
			host = "localhost",
			user = "autoposter",
			passwd = "password",
			database = "admin"
		)

		my_db = self.db_conn.cursor(buffered=True)

		query = "SELECT * FROM autoposts WHERE id = '%s'" % post
		my_db.execute(query)
		records = my_db.fetchall()
		if my_db.rowcount:
			print (records[0])
		else:
			raise CloseSpider('There is not AutoPosts record in database')

		self.subject = records[0][1]
		self.publisher = records[0][2]
		self.content = records[0][3]
		self.password = records[0][-4]

	def start_requests(self):
		self.sitenum = 1
		
		yield Request(self.start_urls[0], self.parse)

		url = "http://gm-arte.or.kr/module/board/board_evn.php"
		formdata = {
			'evnMode' : 'write',
			'boardid': 'board7',
			'idx' : '',
			'category' : '',
			'usehtml': 'N',
			'name' : self.publisher,
			'pass' : self.password,
			'subject' : self.subject,			
			'contents1' : self.content,
			'contentArea' : ''
		}

		yield FormRequest(url, method="POST", formdata=formdata)

		url = "http://www.maeilcon.co.kr/module/board/board_evn.php"
		formdata['boardid'] = 'qna'
		yield FormRequest(url, method="POST", formdata=formdata)
	
		url = "http://www.claripi.com/module/board/board_evn.php"
		formdata['boardid'] = 'board'
		yield FormRequest(url, method="POST", formdata=formdata)

		url = "http://www.ljtec.co.kr/module/board/board_evn.php"
		yield FormRequest(url, method="POST", formdata=formdata)

		url = "https://www.badaroyacht.com/board/board_proc.php"
		formdata = {
			'SelBoard' : '10',
			'SelType' : '',
			'SelVal' : '',
			'PosPage' : '0',
			'CurPage' : '1',
			'PROC' : 'WRITE',
			'secret' : 'N',
			'title' : self.subject,
			'WriteName' : self.publisher,
			'content' : self.content,
			'PWD' : self.password
		}
		yield FormRequest(url, method="POST", formdata=formdata)


		url = "http://nosori.net/bbs.noticeBW"
		formdata = {
			'subject': self.subject,
			"name":self.publisher,
			"content":self.content,
			"password":self.password
		}
		yield FormRequest(url, method="POST", formdata=formdata)


		hdrs = {
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
		}
		url = "http://altaitalia.co.kr/admin/board/wizSave.php"
		formdata = {
			"dir":"board",
			"action":"wizWrite",
			"key":"wiz_freeBoard",
			"top":"6",
			"sub":"3",
			"sub2":"0",
			"sub3":"0",
			"sub4":"0",
			"s":"p_subject",
			"k":"",
			"idx":"",
			"reIdx":"",
			"reDepth":"",
			"mode":"Write",
			"inserter_name":self.publisher,
			"brd_pw":self.password,
			"subject":self.subject,
			"content":self.content,	
			"email":""
		}
		yield FormRequest(url, method="POST", formdata=formdata, headers=hdrs)

		url = "http://www.hwdental.kr/bbs/write_update.php"
		formdata = {
			"bo_table":"bbs2",
			"page":"1",
			"SubMain":"4",
			"SubNum":"2",
			"wr_check":"on",
			"wr_name":self.publisher,
			"wr_subject":self.subject,
			"wr_content":self.content
		}
		yield FormRequest(url, method="POST", formdata=formdata, headers=hdrs)

		url = "http://www.motaean.com/admode/module/board/board.action.controller.php"
		formdata = {
			"olym":"03_baby03",
			"code":"03_baby03",
			"mode":"write",
			"bid":"depa0307mon",
			"page":"1",
			"focus_info":"yes",
			"title":self.subject,
			"name" : self.publisher,
			"password":self.password,
			"email":"phpone@phone.phone",
			"tel1":"111",
			"tel2":"2223",
			"tel3":"3333",		
			"memo":self.content
		}
		yield FormRequest(url, method="POST", formdata=formdata, headers=hdrs)

		url = "http://www.sclab.co.kr/manager/module/board/board.action.controller.php"
		formdata['olym'] = "06_supp04"
		formdata['code'] = "06_supp04"
		formdata["bid]"]= "supp05"
		formdata["password"]= self.password
		formdata["file_check1"] = ""
		formdata["oldfile1"] = ""
		yield FormRequest(url, method="POST", formdata=formdata, headers=hdrs)

		url = "https://hwagang.or.kr/community/free.php?ptype=input&mode=insert&code=free&pos=&code_page=community"
		yield Request(url, self.parse_hwagang)


		# Old Famouse domains (good domains)
		
		url = "http://www.youngjuilbo.com/bbs/write.php"
		formdata = {
			"idxno": "",
			"table": "bbs_8",
			"mode": "input",
			"image": "" ,
			"prt_idxno": "" ,
			"sc_area": "" ,
			"sc_word": "" ,
			"total": "" ,
			"page": "" ,
			"email": "" ,
			"homepage": "",
			"write_mode": "A",
			"name": self.publisher,
			"password": self.password,
			"title": self.subject,
			"content" : self.content,
		}
		yield FormRequest(url, formdata=formdata)

		url = "http://www.ikpnews.net/bbs/write.php"
		formdata['table'] = 'bbs_1'
		yield FormRequest(url, formdata=formdata)

		url = "http://www.gjngj.kr/bbs/write.php"
		yield FormRequest(url, formdata=formdata)

		url = "http://www.jayoo.co.kr/bbs/write.php"
		formdata['table'] = 'bbs_1'
		yield FormRequest(url, formdata=formdata)
		
		url = "http://www.hanammail.com/bbs/write.php"	
		formdata['table'] = 'bbs_7'	
		yield FormRequest(url, formdata=formdata, headers=hdrs)

		url = "https://www.sisain.co.kr/bbs/write.php"
		formdata['table'] = 'bbs_10'	
		yield FormRequest(url, formdata=formdata, headers=hdrs)

		url = "http://www.cheongsongnews.co.kr/bbs/write.php"
		formdata['table'] = 'bbs_3'	
		yield FormRequest(url, formdata=formdata, headers=hdrs)

		url = "http://www.mind-journal.com/bbs/write.php"
		yield FormRequest(url, formdata=formdata, headers=hdrs)

		url = "http://atofrien.com/?page_id=192&board_name=review_text&mode=write&board_action=write"
		yield Request(url, self.parse_atofrien)

		url = "http://seasoningtech.co.kr/wp/?page_id=33&board_name=free&mode=write&board_action=write"
		yield Request(url, self.parse_seasoningtech)

		url = "http://www.smnews.co.kr/bbs/write.php"
		formdata['table'] = 'bbs_2'
		yield FormRequest(url, formdata=formdata, headers=hdrs)

		url = "http://www.kidok.com/bbs/write.php"
		formdata['table'] = 'bbs_25'
		yield FormRequest(url, formdata=formdata, headers=hdrs)

	def parse_atofrien(self, response):
		formdata = {
			"mb_nonce_value": response.xpath('//*[@name="mb_nonce_value"]/@value').extract_first(),
			"mb_nonce_time":response.xpath('//*[@name="mb_nonce_time"]/@value').extract_first(),
			"wp_nonce_value":response.xpath('//*[@name="wp_nonce_value"]/@value').extract_first(),
			"_wp_http_referer": "/?page_id=192&board_name=review_text&mode=write&board_action=write",
			"board_name": "review_text",
			"mode": "write",
			"upload_size":"",
			"search_field": "fn_title",
			"search_text":"",
			"board_page": "1",
			"board_action": "write",
			"editor_type": "S",
			"parent_pid": "0",
			"parent_user_pid": "0",
			"calendar_date":  "",
			"user_name":self.publisher,
			"passwd":"password",
			"title": self.subject,
			"data_type":"html",
			"content":self.content,
			"tag": u"핸드폰도청, 모바일도청, 위치추적, 배우자감시, 코드미사일",
			"file1" : "",
			"file2" : "",
			"kcaptcha_img":response.xpath('//input[@class="kcaptcha"]/@value').extract_first(),
		}

		url = "http://atofrien.com/wp/wp-admin/admin-ajax.php?action=mb_board&admin_page=false&hybrid_app="
		yield FormRequest(url, formdata=formdata, method="POST", dont_filter=True)

	def parse_seasoningtech(self, response):
		
		formdata = {
			"mb_nonce_value": response.xpath('//*[@name="mb_nonce_value"]/@value').extract_first(),
			"mb_nonce_time":response.xpath('//*[@name="mb_nonce_time"]/@value').extract_first(),
			"wp_nonce_value":response.xpath('//*[@name="wp_nonce_value"]/@value').extract_first(),
			"_wp_http_referer": "/wp/?page_id=33&board_name=free&mode=write&board_action=write",
			"board_name": "free",
			"mode": "write",
			"upload_size":"",
			"search_field": "fn_title",
			"search_text":"",
			"board_page": "1",
			"board_action": "write",
			"editor_type": "S",
			"parent_pid": "0",
			"parent_user_pid": "0",
			"calendar_date":  "",
			"user_name":self.publisher,
			"passwd":"password",
			"title": self.subject,
			"data_type":"html",
			"content":self.content,
			"tag": u"핸드폰도청, 모바일도청, 위치추적, 배우자감시, 코드미사일",
			"file1" : "",
			"file2" : "",
			"kcaptcha_img":"222",
		}

		url = "http://seasoningtech.co.kr/wp/wp-admin/admin-ajax.php?action=mb_board&admin_page=false&hybrid_app="
		yield FormRequest(url, formdata=formdata, method="POST", dont_filter=True)

	def parse_seoulam(self, response):
		formdata = {
                    "w":'',
                    "tb": 'qna',
                    "id": '',
                    "sca": '',
                    "sfl": '',
                    "stx": '',
                    'html': '', 
                    "return_url": "/customer/qna.php",
                    "subject": self.subject,
                    "name": self.publisher,
                    "password": self.password,
                    "content": self.content
                }

		url = "http://seoulam.co.kr/jboard/write_update.php?w="
		yield FormRequest(url, method="POST", formdata=formdata)

	def parse_hwagang(self, response):
		tmp_vcode = response.xpath('//*[@name="tmp_vcode"]/@value').extract_first()
		url = "https://hwagang.or.kr/community/free.php"
		formdata = {
			'ptype': 'save',
			'code' : 'free',
			'mode' : 'insert',
			'idx' : '',
			'page' : '',
			'prdcode' : '',
			'tmp_vcode' : tmp_vcode,
			'code_page' : 'community',
			'name' : self.publisher,
			'passwd':self.password,
			'subject': self.subject,
			'content':self.content,
			'agree2':'Y'
		}
		yield FormRequest(url, method="POST", formdata=formdata)


	def parse(self, response):
		url = "http://linelab.co.kr/community/community_write.php?table_type=free"
		yield Request(url, self.parse1)



	def parse1(self, response):
		url = "http://linelab.co.kr/board/board_ok.php"
		
		formdata = {
			"table":"free",
			"mode":"insert",
			"operation":"N",
			"name":self.publisher,
			"title":self.subject,
			"ir1": self.content,
			"password":self.password
		}

		print (formdata)

		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
		}
		yield FormRequest(url, method="POST", formdata=formdata)

		url = "http://ourwinners.net/winsite/m9_2_writeup.php"

		formdata = {
			"title": self.subject,
			"content": self.content
		}

		yield FormRequest(url, formdata=formdata)