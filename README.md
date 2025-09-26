 Weather MCP Server
 
 Türkçe 🇹🇷

Bu proje, [Claude Desktop](https://claude.ai) için **MCP (Model Context Protocol) sunucusu** olarak geliştirilmiştir.  
OpenWeatherMap API kullanarak gerçek zamanlı hava durumu bilgisini getirir.  

Özellikler
- Şehir adı girerek hava durumunu öğrenme  
- Sıcaklık, hava koşulları, nem ve rüzgar bilgisi  
- Claude MCP entegrasyonu ile kolay kullanım  

 Kurulum
1. Bu projeyi klonlayınız:
   ```bash
   git clone https://github.com/irem864/weather-mcp.git
   cd weather-mcp
Sanal ortam oluşturup ve bağımlılıkları yükleyiniz:

bash kodu kopyalayınız :  python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
OpenWeatherMap üzerinden API anahtarı alınız.

Claude Desktop config.json dosyasına MCP sunucusunu ekleyiniz.

 Çalıştırma adımı
bash kodu kopyalayınız:  python server.py
Not
API anahtarınızı .env dosyasında saklamayı unutmayınız.

Claude Desktop üzerinden istediğiniz şehri sorarak hava durumunu öğrenebilirsiniz.

English 🇬🇧
This project is an MCP (Model Context Protocol) server for Claude Desktop.
It fetches real-time weather data using the OpenWeatherMap API.

 Features
Get weather information by city name

Temperature, conditions, humidity, and wind details

Easy integration with Claude MCP

 Installation
Clone this repo:

bash kodu kopyalayınız:  git clone https://github.com/irem864/weather-mcp.git
cd weather-mcp
Create virtual environment and install dependencies:

bash kodu kopyalayınız : python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
Get your API key from OpenWeatherMap.

Add this MCP server to your Claude Desktop config.json.

 Run
bash kodu kopyalayınız: python server.py
 Notes
Don’t forget to keep your API key in a .env file.

You can simply ask Claude Desktop about the weather in any city.

 Developed with  by irem864

yaml
Kodu kopyalayınız

