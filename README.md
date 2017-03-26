# Doorbell Dash
- An Internet of Things device implementing Raspberry Pi, Amazon Dash Buttons, Python/Django, Twilio and Imgur API's. 
- A Wi-Fi enabled doorbell using an Amazon Dash button, that when pressed, takes a photo with the Raspberry Pi camera and sends a photo text message to your phone via Twilio and Imgur. 

## What you'll need
* Amazon Dash Button ($1 - $5)
* Raspberry Pi
* Pi-camera
* Twilio account for texting service (free)
* Imgur account for images (free)

## Installation
* $ pip3 install scapy-python3
* $ pip install twilio
* $ pip install pyimgur

## Usage
* You must run script as root user / SUDO

## 'Hack' Amazon Dash Button
* Open the Amazon Shopping app on your PHONE.
* From the menu, GOTO 'Your Account'
* Scroll down, choose 'Set up a new device'
* Choose 'Dash Button'
* Connect your button to your local wifi network
* Do NOT choose a product to order, just exit the app.

## Discover the Dash Button's MAC address
- Push button for 3 seconds until it pulses blue
- Connect your computer wifi to "Amazon ConfigureMe"
- In a web browser, go to: http://192.168.0.1/
- Make note of the MAC address of your Dash Button.

## Setup Twilio Account
* To receive SMS notifications, you need to sign up for Twilio
* Signup for a free Twilio account
* As part of the signup process, you need to verify a phone number. Use the cell phone number that you want to send messages to.
* After you verify your phone number, Twilio will assign you a local phone number. This is the phone number that will be sending the text messages.
* Click "get started", then "Go to Your Account".
* When you login to your account, you will see an Account SID and Auth Token field. Click on the lock icon in front of the Auth Token field. Make note of these two values. You will need them for the Python code.

## Twilio Notes
* Twilio service prepends “Sent from a Twilio Trial account” to trial account messages.
* The service is free as long as you are sending 250 messages or less per month.

## General Notes:
* !! RENAME ExampleCreds.py to creds.py. Put in all the information you received from Imgur and Twilio here. This will store all personal information (phone numbers, API tokens, etc).  This is not in the project, as it is in the gitignore.
* Address Resolution Protoco or ARP is used for mapping a network address to a physical address. EXAMPLE:  IP Address to a MAC address
* Problems with Raspberry Pi and camera communicating? Check to make sure your Pi detects the camera: $ vcgencmd get_camera

## Update Raspberry Pi
* It's a good idea to update your Pi to make sure the packages you install are up to date.
* $ sudo apt-get update
* $ sudo apt-get dist-upgrade

## If you run into errors updating your Pi, you may need to change your python version system-wide.  
* $ python --version
* $ update-alternatives --list python
* $ sudo update-alternatives --config python

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Credits
* Nick Chemsak

## License
[MIT License](https://github.com/nchemsak/doorbell_dash_angularJS/blob/master/LICENSE)


