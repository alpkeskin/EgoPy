#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from prettytable import PrettyTable

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--durak', type=str, help="Durak bilgilerini görebilirsiniz.")
	parser.add_argument('-k', '--kartsorgu', type=str, help="Kart sorgulama yapabilirsiniz.")
	parser.add_argument('-ht', '--hat', type=str, help="Hat bilgilerini görebilirsiniz.")
	return parser.parse_args()

def getJSON(servis,data):
	endPoints = {
		"drk" : f'http://88.255.141.70/mobil/iphonenew/durak.asp?Fnc=DurakAra&Query={data}&Type=true',
		"krt" : f'http://88.255.141.70/mobil/iphonenew/ankarakart.asp?Fnc=AnkaraKartAra&Query={data}',
		"hatt" : f'http://88.255.141.70/mobil/iphonenew/hat.asp?Fnc=HatAra&Query={data}&Type=false'
	}
	
	headers = {
    	'User-Agent': 'otobushatlari/2.0.19 CFNetwork/1120 Darwin/19.0.0'
	}
	return requests.get(endPoints[servis], headers=headers).json()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
			print(f'''{bcolors.FAIL}
                            __  __            _    __    
 ___ ___ ____    ___  __ __/ /_/ /  ___  ___ ( )__/ /__ _
/ -_) _ `/ _ \  / _ \/ // / __/ _ \/ _ \/ _ \|/ _  / _ `/
\__/\_, /\___/ / .__/\_, /\__/_//_/\___/_//_/ \_,_/\_,_/ 
   /___/      /_/   /___/                                

			{bcolors.ENDC}''')

def main():
	args = parse_args()
	drk = args.durak
	krt = args.kartsorgu
	hatt = args.hat


	if drk is not None:
		banner()
		print(f"{bcolors.OKGREEN}Sorgulanan durak no: {bcolors.ENDC}"+drk)
		data = getJSON('drk',drk)
		if data['status'] == 'false':
			print(f"{bcolors.FAIL}{data['error']}{bcolors.ENDC}")
			exit()
		z = PrettyTable()
		z.field_names = [f"{bcolors.WARNING}Hat No{bcolors.ENDC}",f"{bcolors.WARNING}Hat Adı{bcolors.ENDC}",f"{bcolors.WARNING}Plaka{bcolors.ENDC}",f"{bcolors.WARNING}Süre{bcolors.ENDC}"]
		for s in range(len(data)-1):
			z.add_row([str(data['data'][s]['hatkod']),str(data['data'][s]['hatad']),str(data['data'][s]['plaka']),str(data['data'][s]['sure'])])
		print(z)
	elif krt is not None:
		banner()
		print(f"{bcolors.OKGREEN}Sorgulanan kart no: {bcolors.ENDC}"+krt)
		data = getJSON('krt',krt)
		if data['data'][0]['message'] != 'Sorgulama Başarılı':
			print(f"{bcolors.FAIL}{data['data'][0]['message']}{bcolors.ENDC}")
			exit()
		kart = int(krt)
		baki = float(data['data'][0]['bakiye'])
		x = PrettyTable()
		x.field_names = [f"{bcolors.WARNING}Bakiye [₺]{bcolors.ENDC}"]
		x.add_row([baki])
		print(x)
	elif hatt is not None:
		banner()
		print(f"{bcolors.OKGREEN}Sorgulanan hat no: {bcolors.ENDC}"+hatt)
		data = getJSON('hatt',hatt)
		if len(data['data']) == 0:
			print(f"{bcolors.FAIL}Hatalı Hat Girildi veya Aktif Otobüs Yok.{bcolors.ENDC}")
			exit()		
		y = PrettyTable()
		y.field_names = [f"{bcolors.WARNING}Hat No{bcolors.ENDC}",f"{bcolors.WARNING}Hat Adı{bcolors.ENDC}",f"{bcolors.WARNING}Açıklama{bcolors.ENDC}"]
		for s in range(len(data)):
			y.add_row([str(data['data'][s]['kod']),str(data['data'][s]['ad']),str(data['data'][s]['aciklama'])])
		print(y)
	else:
		banner()
		print("""KULLANIM: python ego.py [SEÇENEKLER]

		SEÇENEKLER:
		 --kartsorgu, -k\t\tVerilen kart numarasının bakiyesini yazdır ve çık
		 --durak, -d\t\t\tVerilen durakğa yakalşan otobüsleri listele ve çık
		 --hat, -ht\t\t\tVerilen hattın bilgilerini yazdır ve çık
		""")

main()
#https://github.com/alpkeskin
