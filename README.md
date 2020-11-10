[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# EgoPy
Ego Cep'te uygulaması artık Python'da

## Çalıştırmadan önce :
```
pip3 install -r requirements.txt
```

## Kullanım :
```
KULLANIM: python ego.py [SEÇENEKLER]

	SEÇENEKLER:
     --kartsorgu, -k\t\tVerilen kart numarasının bakiyesini yazdır ve çık
	 --durak, -d\t\t\tVerilen durakğa yakalşan otobüsleri listele ve çık
	 --hat, -ht\t\t\tVerilen hattın bilgilerini yazdır ve çık
```


# Docker

## Çalıştırmadan önce :
```
# Docker imajı oluşturma
docker build -t calganaygun/egopy .
```

## Kullanım :
```
KULLANIM: docker run -it calganaygun/egopy [SEÇENEKLER]

	SEÇENEKLER:
     --kartsorgu, -k\t\tVerilen kart numarasının bakiyesini yazdır ve çık
	 --durak, -d\t\t\tVerilen durakğa yakalşan otobüsleri listele ve çık
	 --hat, -ht\t\t\tVerilen hattın bilgilerini yazdır ve çık
```
## Ekran :

![Ego Py](https://raw.githubusercontent.com/alpkeskin/EgoPy/main/EgoPySS.png)

