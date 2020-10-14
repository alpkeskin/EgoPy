#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
from prettytable import PrettyTable

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--durak', type=str, help="Durak bilgilerini görebilirsiniz.")
	parser.add_argument('-k', '--kartsorgu', type=str, help="Kart sorgulama yapabilirsiniz.")
	parser.add_argument('-ht', '--hat', type=str, help="Hat bilgilerini görebilirsiniz.")
	return parser.parse_args()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def remo():
    if os.path.exists("html.json"):
        os.remove("html.json")

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
		url = ('http://88.255.141.70/mobil/iphonenew/durak.asp?Fnc=DurakAra&Query='+drk+'&Type=true')
		print(f"{bcolors.OKGREEN}Sorgulanan durak no: {bcolors.ENDC}"+drk)
		headers = {
    		'User-Agent': 'otobushatlari/2.0.19 CFNetwork/1120 Darwin/19.0.0'
		}
		response = requests.get(url, headers=headers)
		html = response.content
		soup=BeautifulSoup(html,"html.parser")
		with open("html.json","w") as file :
			file.write(str(soup))
		f = open('html.json')
		data = json.load(f)
		z = PrettyTable()
		z.field_names = [f"{bcolors.WARNING}Hat No{bcolors.ENDC}",f"{bcolors.WARNING}Hat Adı{bcolors.ENDC}",f"{bcolors.WARNING}Plaka{bcolors.ENDC}",f"{bcolors.WARNING}Süre{bcolors.ENDC}"]
		for s in range(len(data)-1):
			z.add_row([str(data['data'][s]['hatkod']),str(data['data'][s]['hatad']),str(data['data'][s]['plaka']),str(data['data'][s]['sure'])])
		print(z)
		remo()	
	elif krt is not None:
		banner()
		url = ('http://88.255.141.70/mobil/iphonenew/ankarakart.asp?Fnc=AnkaraKartAra&Query='+krt)
		print(f"{bcolors.OKGREEN}Sorgulanan kart no: {bcolors.ENDC}"+krt)
		headers = {
    		'User-Agent': 'otobushatlari/2.0.19 CFNetwork/1120 Darwin/19.0.0'
		}
		response = requests.get(url, headers=headers)
		html = response.content
		soup=BeautifulSoup(html,"html.parser")
		with open("html.json","w") as file :
			file.write(str(soup))
		f = open('html.json')
		data = json.load(f)
		kart = int(krt)
		baki = float(data['data'][0]['bakiye'])
		x = PrettyTable()
		x.field_names = [f"{bcolors.WARNING}Bakiye [₺]{bcolors.ENDC}"]
		x.add_row([baki])
		print(x)
		remo()
	elif hatt is not None:
		banner()
		url = ('http://88.255.141.70/mobil/iphonenew/hat.asp?Fnc=HatAra&Query='+hatt+'&Type=false')
		print(f"{bcolors.OKGREEN}Sorgulanan hat no: {bcolors.ENDC}"+hatt)
		headers = {
    		'User-Agent': 'otobushatlari/2.0.19 CFNetwork/1120 Darwin/19.0.0'
		}
		y = PrettyTable()
		y.field_names = [f"{bcolors.WARNING}Hat No{bcolors.ENDC}",f"{bcolors.WARNING}Hat Adı{bcolors.ENDC}",f"{bcolors.WARNING}Açıklama{bcolors.ENDC}"]
		response = requests.get(url, headers=headers)
		html = response.content
		soup=BeautifulSoup(html,"html.parser")
		with open("html.json","w") as file :
			file.write(str(soup))
		f = open('html.json')
		data = json.load(f)
		for s in range(len(data)):
			y.add_row([str(data['data'][s]['kod']),str(data['data'][s]['ad']),str(data['data'][s]['aciklama'])])
		print(y)
		remo()

main()
#https://github.com/alpkeskin
