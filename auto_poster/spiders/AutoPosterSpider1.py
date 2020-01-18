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
			user = "root",
			passwd = "",
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

	# http://seoulam.co.kr/
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


		url = "http://10ripo.com/"

		formdata = {
			"r":"home",
			"a":"write",
			"c":"5",
			"cuid":"5",
			"m":"bbs",
			"bid":"guest",
			"uid":"",
			"reply":"",
			"nlist":"/",
			"pcode": "20191207191012",
			"upfiles" : "",
			"name": self.publisher,
			"pw":self.password,
			"subject":self.subject,
			"html":"",
			'content': self.content,
			"tag":"",
			"trackback":"",
			"backtype":"type"
		}

		yield FormRequest(url, method="POST", formdata=formdata)


		url = "http://ourwinners.net/winsite/m9_2_writeup.php"

		formdata = {
			"title": self.subject,
			"content": self.content
		}

		yield FormRequest(url, formdata=formdata)