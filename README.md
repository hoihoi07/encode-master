#### The_Encoder_Bot
[![Readme](https://github-readme-stats.vercel.app/api/pin/?username=tellybots&repo=The-Encoder-Bot&theme=cobalt)](h&bg_color=24378)
<p align="center" > <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Wolfy024/Renamer-Bot?style=plastic">
 <a> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr-raw/Wolfy024/Renamer-Bot?color=blue&label=Open%20PRs"> <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed-raw/Wolfy024/Renamer-Bot?color=blue&label=Closed%20PRs"> </a> </p>

<p align="center" > <img alt="GitHub forks" src="https://img.shields.io/github/forks/Wolfy024/Renamer-Bot?label=%F0%9F%8D%B4Forks&logoColor=blue&style=social">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/wolfy024/Renamer-Bot?label=%E2%AD%90%EF%B8%8FStars&logoColor=blue&style=social"> </p>


#### Configuration
Add values in environment variables or add them in [config.env.example](/VideoEncoder/config.env.example) and rename file to `config.env`.

**Basics**
- `API_ID` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` - Get it by creating a bot on [https://t.me/BotFather](https://t.me/BotFather)

**Authorization**
- `SUDO_USERS` - Chat identifier of the sudo user. For multiple users use space as seperator.

**Encode Settings**
- `RESOLUTION` - [Click Here](https://weeb-zone.blogspot.com/p/encode-telegram-bot-guide.html)
- `PRESET` - [Click Here](https://weeb-zone.blogspot.com/p/encode-telegram-bot-guide.html)
- `TUNE` - [Click Here](https://weeb-zone.blogspot.com/p/encode-telegram-bot-guide.html)
- `AUDIO` - [Click Here](https://weeb-zone.blogspot.com/p/encode-telegram-bot-guide.html)
- `CRF` - [Click Here](https://weeb-zone.blogspot.com/p/encode-telegram-bot-guide.html)

**Optional**
- `DOC_THUMB` - (Optional) Thumbnail for document
- `UPLOAD_AS_DOC` - (Optional) Uploads Video as doc if `1` else `0`.
- `DOWNLOAD_DIR` - (Optional) Temporary download directory to keep downloaded files.
- `ENCODE_DIR` - (Optional) Temporary encode directory to keep encoded files.

#### Configuring Encoding Format
To change the ffmpeg profile edit them in [ffmpeg.py](/VideoEncoder/utils/ffmpeg.py)

#### Deployment
With python3.7 or later.
```
pip3 install --no-cache-dir -r requirements.txt
bash run.sh
```

#### Credits

- [ShannonScott](https://gist.github.com/ShannonScott) for [transcode_h265.py](https://gist.github.com/ShannonScott/6d807fc59bfa0356eee64fad66f9d9a8)
- [viperadnan-git](https://github.com/viperadnan-git/video-encoder-bot) for queue etc.
- [weebtime](https://github.com/WeebTime) For His Video Encoder Bot For Me Adding It on Heroku
- [AbirHasan2005](https://github.com/AbirHasan2005) For His Database

#### Copyright & License
- Copyright &copy; 2021 &mdash; [WeebTime](https://github.com/WeebTime)
- Licensed under the terms of the [GNU AFFERO GENERAL PUBLIC LICENSE](./LICENSE)


#### Deploy on Heroku

<p align="">
    <a href="https://heroku.com/deploy?template=https://github.com/Tellybots/The-Encoder-Bot">
    <img src="https://github.com/nikhileashy/justfor_testing/blob/main/herokudeploy-01-cropped.svg" alt="herokudeploy-01" border="0" height="100" width="240"></a>
</p>


#### Support 
<a href="https://t.me/Tellybots_support"><img src="https://img.shields.io/badge/Support_Group-2cb6e0?style=for-the-badge&logo=telegram&logoColor=white"></a> <a href="https://t.me/tellybots_4u"><img src="https://img.shields.io/badge/Updates_Channel-2cb6e0?style=for-the-badge&logo=telegram&logoColor=white"></a>

#### Database

<p align="left">
  <a href="https://github.com/pyrogram/pyrogram">
    <img alt="Pyrogram" src ="https://i.imgur.com/BOgY9ai.png" width="104.75" height="32"/>
  </a>
</p>

<p align="left">
  <a href="https://docs.mongodb.com">
    <img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?&style=for-the-badge&logo=mongodb&logoColor=white"/>
  </a>
</p>
