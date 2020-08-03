### Bu dökümantasyon python kullanarak docker-compose ile elasticsearch cluster çalıştırmak üzere hazırlanmıştır.

İlk olarak https://docs.docker.com/engine/install/ adresinden işletim sistemimize uygun olarak docker kurulumu yapmalıyız.

Ben ubuntu 18.04 versiyonunu kullandım, yani kurulum için:

# 1. Daha önce docker kullandıysak:
> $ sudo apt-get remove docker docker-engine docker.io containerd runc

komutunu çalıştırmalıyız, bu eski versiyonları kaldıracak.

# 2.Kaldırma işlemi tamamlandıktan sonra veya ilk defa kurulum için:

> $ sudo apt-get update
ve
> $ sudo apt-get install apt-transport-https \ ca-certificates \ curl gnupg-agent \ software-properties-common
  
komutlarını çalıştıracağız, bunlar ön gereksinimler, detaylı bilgi için kurulum sayfasını ziyaret edebilirsiniz.

# 3. Daha sonra GPG anahtarını ekleyeceğiz:
> $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 4. Anahtarınızın 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88 olduğundan emin olmak için:
> $ sudo apt-key fingerprint 0EBFCD88

komutunu çalıştıracağız.

# 5. Daha sonra:

> $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
   
komutunu çalıştırıp en son stabil repository'i kuracağız.

# 6. Daha sonra tekrar:
> $ sudo apt update 
ile paketleri güncelliyoruz.

# 7. Standart ubuntu repository yerine docker repository'sini kuracağımızdan emin oluyoruz:
> $ apt-cache policy docker-ce 

çıktı:
```
docker-ce:
  Installed: (none)
  Candidate: 18.03.1~ce~3-0~ubuntu
  Version table:
     18.03.1~ce~3-0~ubuntu 500
        500 https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
```
benzeri olacak.

# 8. Son olarak docker'ı kuracağız:

> $ sudo apt install docker-ce 

Docker kurulumunun başarılı olup olmadığını kontrol etmek için ise:

> $ sudo systemctl status docker 

### Şimdi docker-compose kurulumuna geçelim.

Docker'ın github sayfasından versiyonu kontrol edelim:
https://github.com/docker/compose/releases
# 1. Şu an kullanılan versiyon 1.26.2, siz kurduğunuzda daha yeni bir versiyon çıkmış ise, aşağıdaki kodda o kısmı güncelleyebilirsiniz:
> $ sudo curl -L https://github.com/docker/compose/releases/download/1.26.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

# 2. İzinleri düzenleyelim:
> $ sudo chmod +x /usr/local/bin/docker-compose

# 3. Kurulumun başarılı olup olmadığını kontrol edelim:
> $ docker-compose --version

### Docker-compose kurulumu bittikten sonra artık Elasticsearch'i docker-compose ile çalıştıralım:

# 1. https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html adresine giderek buradaki  adımları izleyelim:

ilk olarak bir docker-compose.yml dosyası oluşturacağız, içeriği belirtilen adreste veya oluşturduğum repository'de bulabilirsiniz.

# 2. Daha sonra docker-compose'u ayağa kaldıralım:

> $ docker-compose up 

Burada dikkat edilmesi gereken, eğer elasticsearch servisi zaten çalışmakta ise özellikle belirtilmemişse aynı zamanda docker-compose'un da kullandığı 9200 portunu kullanacak, bu yüzden önce elasticsearch servisini kapatmalıyız:

> $ sudo service elasticsearch stop

# 3. Eğer buraya kadar bir sorunla karşılaşılmadı ise bir "_cat/nodes" isteği atarak ağın çalışıp çalışmadığını ve hangi node'ların ayakta olduğuu görebiliriz.

> $ curl -X GET "localhost:9200/_cat/nodes?v&pretty"

### Artık python kullanarak elasticsearch ağına veri yükleme, silme, arama vb. gibi işlemleri yapabiliriz. Bunların detayları dosyalar üzerinde açıklanmıştır.
