#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.utils.response import open_in_browser
from scrapy import Spider, Request, FormRequest
import re, requests, os, time
from scrapy.shell import inspect_response
def download(url, destfilename):
	if not os.path.exists(destfilename):
		print ("Downloading from %s to %s..." % (url, destfilename))
		try:
			r = requests.get(url, stream=True)
			with open(destfilename, 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						f.write(chunk)
						f.flush()
		except:
			print ("Error downloading file.")

# https://sites.google.com/site/twinphonesale
class AutoPosterSpider(Spider):
	name = "autoposter"

	start_urls = [
			"http://seoulam.co.kr/customer/qna.php?page=list&tb=qna&sca=&sfl=&stx=&pg=",
			#'http://www.youngjuilbo.com/bbs/writeForm.html?mode=input&table=bbs_8&category='			
	]

	def start_requests(self):
		self.sitenum = 1
        
		self.subject = u'핸드폰도청 | 배우자감시 | 코드미사일 | 자녀핸드폰감시'
		self.publisher = u'코드미사일'
		self.content = u'''
휴대폰도청 | 핸드폰도청 | 배우자감시 | 카톡복구 | 위치추적 | 불륜증거 | 핸드폰엿보기 |코드미사일
요즘 귀가가 늦어지는 남편..
외출이 많아지는 아내..
밤에 전화를 받지않는 애인..
결혼을 앞둔 신랑 신부..

간단한 방법으로 위치를 알수있습니다.

혼자 고민하지말고 연락주세요!!!

바람난사람 증거잡기/외도 증거 수집방법/
카카오톡복원 카카오톡해킹방법/
실시간도청으로 상대방 거짓말 잡아내는방법/
위치추적/실시간으로 위치추적하는 방법/
통화내용듣기로 증거수집하는방법/
상대방 카카오톡 실시간 확인하는방법/
쌍둥이폰. 복제폰이 궁금하신분/
스파이앱 판매합니다/

ㅋㅏ 톡 문 의: amxpc17

휴대폰도청 | 핸드폰도청 | 배우자감시 | 카톡복구 | 위치추적 | 불륜증거 | 핸드폰엿보기 |코드미사일

핸드폰도청어플 도청앱 핸드폰도청장치 판매합니다.


핸드폰 엿보기 ㅋㅏ 톡 문 의: amxpc17
핸드폰 엿보기 ㅋㅏ 톡 문 의: amxpc17
핸드폰 엿보기 ㅋㅏ 톡 문 의: amxpc17

핸드폰도청앱 메리크리스마스 조국 리버풀 레스터 황정음 정미애 송가인 천문 보이스퀸 나쁜상사 외모지상주의 소명 권덕진판사 다우지수 리니지2m 인벤  뉴스 결혼이야기
이승우 해피투게더4 웬디 맛남의 광장 99억의 여자 황희찬
            
        '''

		yield Request(self.start_urls[0], self.parse)

	# http://seoulam.co.kr/
	def parse(self, response):
		
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
                    "password": "password",
                    "content": self.content
                }

		url = "http://seoulam.co.kr/jboard/write_update.php?w="
		yield FormRequest(url, self.parse_post, method="POST", formdata=formdata)

	# youngjuilbo.com
	def parse_post(self, response):
		
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
			"password": "password123",
			"title": self.subject,
			"content" : self.content,
		}
		
		url = "http://www.youngjuilbo.com/bbs/write.php"

		yield FormRequest(url, self.parse_youngjuilbo, formdata=formdata)

		formdata['table'] = 'bbs_1'

		url = "http://www.ikpnews.net/bbs/write.php"

		yield FormRequest(url, self.parse_ikpnews, formdata=formdata)

		url = "http://atofrien.com/?page_id=192&board_name=review_text&mode=write&board_action=write"

		yield Request(url, self.parse_atofrien)

		url = "http://seasoningtech.co.kr/wp/?page_id=33&board_name=free&mode=write&board_action=write"

		yield Request(url, self.parse_seasoningtech)

		
	def parse_youngjuilbo(self, response):
		pass
	def parse_ikpnews(self, response):
		pass

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