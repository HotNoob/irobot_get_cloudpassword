# irobot_get_cloudpassword
dumps local passwords from irobot's "cloud" for roomba robots so you can gain local mqtt access to your roomba

simplified minimalistic script to only retrive local password. 
original code from here: https://github.com/NickWaterton/Roomba980-Python/blob/master/roomba/getcloudpassword.py
which is apparently based on: https://github.com/koalazak/dorita980/blob/master/bin/getPasswordCloud.js


# setup
install requirements ( just python requests )
```
pip install -r requirements.txt
```

# usage
```
python get_cloud_password.py "your irobot login" "your irobot password"
```

# output
returns id, name, and password for all roomba's linked to account
