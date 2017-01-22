# WORKSTATION
<b>Description:</b>
<p>Intellegent worktation using Open Source Electronic Devices</p>

Features of this project include:</br>
- Intellegent power management system</br>
- AI based user friendly UI with natural language support</br>
- Chatbox for access through intranet</br>
- Telegram bot for access through internet</br>
- Multi platform support</br>

<b>Languages used:</b>
- Arduino
- Python
- PHP
- Javascript
- HTML
- CSS

<b>Tools used:</b>
- <a href="https://www.arduino.cc/en/Main/Software/">Arduino IDE</a>
- <a href="https://wit.ai/">Wit.ai</a>
- <a href="https://www.python.org/">Python</a>
- <a href="https://github.com/wit-ai/pywit">Pywit</a>
- <a href="https://python-telegram-bot.org/">Python-telegram-api</a>
- <a href="https://www.apache.org/">Apache</a>, <a href="http://php.net/">Php5</a>
- <a href="https://www.mysql.com/">MySQL</a>, <a href="https://www.phpmyadmin.net/">phpMyAdmin</a>
- <a href="https://github.com/maniacbug/RF24">RF24 Library</a>
- <a href="https://www.raspberrypi.org/downloads/raspbian/">Raspbian</a>

<b>Team members:</b></br>

1. <a href="https://github.com/vu2swz">Abu Jose George</a></br>
2. Jayasanker Jayaprakash</br>
3. <a href="https://github.com/h3llcr0w">Mishel Jyothis Paul</a></br>
4. Rajiv Ambrose</br>

<b>Components used:</b>
- Arduino UNO
- Raspberry Pi 3
- NRF24L01+ tranceiver
- LM35 temperature sensor
- LDR
- Proximity sensor
- Relay module

## Installation:

<b>Installing Raspbian:</b>

  Follow <a href="https://www.raspberrypi.org/documentation/installation/installing-images/">this guide</a> to install and setup the Raspberry Pi.

<b>Installing Arduino IDE:</b>

   ```bash
   $ sudo apt-get update
   $ sudo apt-get install arduino
   ```

<b>Installing pywit:</b>

   Using `pip`:
   ```bash
   $ pip install wit
   ```
   From source:
   ```bash
   $ git clone https://github.com/wit-ai/pywit
   $ python setup.py install
   ```

<b>Installing Telegram Bot API:</b>

   Using `pip`:
   ```bash
   $ pip install python-telegram-bot --upgrade
   ```
   From source:
   ```bash
   $ git clone https://github.com/python-telegram-bot/python-telegram-bot
   $ cd python-telegram-bot
   $ python setup.py install
   ```

<b>Installing Apache2, PHP, MySQL, phpMyAdmin:</b>

  - Apache2:
     ```bash
     $ sudo apt-get update
     $ sudo apt-get install apache2
     ```

  - PHP:
     ```bash
     $ sudo apt-get update
     $ sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql
     ```

  - MySQL:
     ```bash
     $ sudo apt-get update
     $ sudo apt-get install mysql-server
     ```

  - phpMyAdmin:
     ```bash
     $ sudo apt-get update
     $ sudo apt-get install phpmyadmin php-mbstring php-gettext
     ```
     > [ Don't forget to add to apache configuration file. ]

## Setting up the workstation:

1. Clone the repository

    ```bash
    $ git clone https://github.com/vu2swz/WORKSTATION
    $ cd WORKSTATION
    ```
2. Copy the webserver files to apache webroot

    ```bash
    $ sudo mv /webserver /var/www/html/
    ```
3. Program the nodes using Arduino IDE with the given node.ino sketch. Vary the node id in the code for each device according to cabin number.

4. Program the server using Arduino IDE with the given server.ino sketch.

5. Connect the server to the network connected raspberry pi. Run the script to read from arduino as

    ```bash
    $ python ardread.py & >~/logs/bot/arduino
    ```
       OR

    ```bash
    $ sh arduino.sh
    ```
6. Run the telegram bot by running the script as

    ```bash
    $ sudo python /var/www/html/chatbox/telbot.py & > ~/logs/bot/telegram
    ```
       OR
    ```bash
    $ sh telegram.sh
    ```
