from django.shortcuts import render

from mailjet_rest import Client
import os

# for env variable
from dotenv import load_dotenv
load_dotenv()


email_template1 = """\
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        img{
            width: 15px;
            height : 15px;
        }
    </style>
</head>
<body>
    
            """
email_template2 = """\
           
</body>
</html>
"""

weather_emoji_map = {
    'cold' : 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/304/cold-face_1f976.png',
    'super_hot' : 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/304/fire_1f525.png',
    'normal' : 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/304/sun_2600-fe0f.png',
    'hot' : 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/whatsapp/314/fire_1f525.png'
}

def mail_het_send(subject, temp, reveiver_email):
    try:
        api_key = os.environ.get("mailjet_api_key")
        api_secret = os.environ.get("mailjet_api_secret")
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        # add this table_string to the email_template
        weather_type = 'normal'
        if temp<16:
            weather_type = 'cold'
        elif temp>16 and temp<23:
            weather_type = 'normal'
        elif temp>23 and temp<29:
            weather_type = 'hot'
        else:
            weather_type = 'super_hot'

        emoji_url = weather_emoji_map.get(weather_type)

        email_template = email_template1 + str(temp) + ' ' + "<img src={}>".format(emoji_url) + email_template2
        data = {
        'Messages': [
            {
            "From": {
                "Email": "arbazkhan.tata@gmail.com",
                "Name": "Arbaz - okmail"
            },
            "To": [
                {
                "Email": reveiver_email,
                "Name": " "
                }
            ],
            "Subject": subject,
            "HTMLPart": email_template,
            "CustomID": "AppGettingStartedTest"
            }
        ]
        }
        result = mailjet.send.create(data=data)
    except:
        print('failed to send email to the client')
        