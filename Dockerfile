FROM nikolaik/python-nodejs:python3.9-nodejs17
RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y
COPY . /innexia
WORKDIR /innexia
RUN chmod 777 /innexia
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt
CMD python3 main.py

# എന്താടാ മോനെ അടിച്ചു അടിച്ചു മാറ്റാൻ വന്നതാണോ? നാണം വേണം കേട്ടോ കുറച്ച് 😜😹.
# എന്തായാലും എടുത്തു bug ആരികും മുഴുവൻ നോക്കി ഒക്കെ add ആക്ക് കേട്ടോ 🤭
