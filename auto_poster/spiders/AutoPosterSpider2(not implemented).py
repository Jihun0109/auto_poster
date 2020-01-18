#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.utils.response import open_in_browser
from scrapy import Spider, Request, FormRequest
import re, requests, os, time
from scrapy.shell import inspect_response

class AutoPosterSpider(Spider):
	name = "autoposter2"

	start_urls = [
			#"http://gagusuri.kr/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
			"http://gagusoori.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write"
	]

	def start_requests(self):
		self.sitenum = 1
        
		self.subject = u'핸드폰 엿보기 | 핸드폰도청 | 배우자감시 | 카톡복구 | 코드미사일 | ㅋㅏ 톡 문 의: amxpc17'
		self.publisher = u'코드미사일'
		self.content = u'''
휴대폰도청 | 핸드폰도청 | 배우자감시 | 카톡복구 | 배우자감시 | 코드미사일
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

휴대폰도청 | 핸드폰도청 | 배우자감시 | 카톡복구 | 배우자감시 | 코드미사일

바람난애인
카톡복구
카카오톡해킹
핸드폰도청
실시간도청
외도증거
배우자외도증거
불륜증거
간통증거
통화도청
실시간화면감시
카톡내용확인
통화내용듣기
위치추적
스파이앱
복제폰
쌍둥이폰
핸드폰복제


핸드폰 엿보기 ㅋㅏ 톡 문 의: amxpc17
핸드폰 엿보기 ㅋㅏ 톡 문 의: amxpc17
핸드폰 엿보기 ㅋㅏ 톡 문 의: amxpc17
            
        '''
		yield Request(self.start_urls[0], self.parse)

	# http://seoulam.co.kr/
	def parse(self, response):
		print (response.url)