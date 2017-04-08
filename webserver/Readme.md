#  Webserver Directory
- Basic webserver that provides chat with the wit.ai client and enables gpio functions
- off.php, on.php files are primarily used for testing purposes to ensure that php has sufficient permissions to control the gpio pins
- log.php is used to display the logs from arduino which are updated by the script ardread.py . The file has to be further modified with an improved front end displaying the current cabin status. The required data is available from the mySQL database.
- For controlling a gpio pin, the details such as the pin number and the state is sent by POST method to pin_out.php in the commands folder which in turn utilises the gpio_out.py script.
- The chatbox directory contains files required for the chatbot, both the webpage available over LAN and the Telegram Bot.
