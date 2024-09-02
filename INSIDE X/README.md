<div align="center">

<br>

![INSIDE X](../res/INSIDE_X.png)

<br>

FlexFlow를 적용한, 통합형 스마트팩토리 구축 디바이스 INSIDE X를 소개합니다.<br>
FlexFlow의 유연하고, 빠른 프레임워크를 사용하는 것 뿐만 아니라.<br>
PLC, AI, IoT 등 모든 기능이 통합 된 INSIDE X의 아름다운 매력에 빠져보세요!

<br><br>

## ⚒️ 환경 및 라이브러리 ⚒️

### Jetson Orin NX (8GB)

|소프트웨어|라이브러리|버전|설명|
|:---:|:---:|:---:|:---:|
|Ubuntu|JetPack 6|20.04|운영체제 및 환경|
|Apache HTTP Server|-|2.4.58|웹 서버|
|mosquitto|-|2.0.18|MQTT 브로커|
|Python|-|3.10.12|백엔드 서버|
|+|ultralytics|8.0.239|AI 연산|
|+|torch|<a href='https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048'>2.1.0 (JetPack 6)</a>|AI 연산 및 GPU 가속|
|+|paho-mqtt|1.6.1|MQTT 통신|


### Raspberry Pi 4 (4GB)

|소프트웨어|라이브러리|버전|설명|
|:---:|:---:|:---:|:---:|
|Raspberry Pi OS Lite (64-bit)|-|Kernal 6.1|운영체제 및 환경|
|Python|-|3.10.6|기본 Python|
|mosquitto|-|2.0.18|MQTT 브로커|
|<a href="https://github.com/thiagoralves/OpenPLC_v3">OpenPLC v3 Runtime</a>|-|<a href='https://github.com/thiagoralves/OpenPLC_v3/tree/6a1a89fe3f8cb878b47327985be104d731febb8f'>6a1a89f</a>|PLC 구현 소프트웨어|


### Arduino Nano (Slave Device)

|라이브러리|버전|설명|
|:---:|:---:|:---:|
|Stepper|1.1.3|스테퍼 모터 제어|

</div>