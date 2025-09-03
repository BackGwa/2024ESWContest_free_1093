<div align="center">

<br>

![FlexFlow_Banner](./res/Banner.png)

<br>

스마트팩토리 구축을 위한, 솔루션인 FlexFlow를 소개합니다!<br>
FlexFlow는 어디에서나, 유연하고 빠르게 작동하며, 누구나 쉽게 사용할 수 있는 프레임워크로<br>
미리 설계 된 하드웨어부터 커스텀 하드웨어 지원까지 진정한 오픈소스 스마트팩토리 구축 플랫폼 입니다.<br>

구축 시 문제가 발생하거나, 질문이 있으시면, <a href="https://github.com/BackGwa/FlexFlow/issues">Issue</a>를 남겨주세요. 최대한 도움을 드리겠습니다!<br>
시연 영상은 [이 곳](https://youtu.be/waabn6HJMFI)에서 시청하실 수 있습니다!

<br><br>

## 🚨 알아두세요!

현재 FlexFlow 프로젝트는 초기 상태이며, 사전에 설계 된 INSIDE X 하드웨어를 바탕으로 제작되고 있습니다.<br>
현재는 다른 플랫폼에 적용하기에는 불안정한 상태입니다.

<br><br>

## 📝 라이선스 📝
해당 레포지토리는 디렉토리 및 파일 별로 라이선스가 각각 다르게 부여됩니다.<br>
**라이선스 분쟁이 발생할 경우, 언제나 라이선스 유형이 변경될 수 있습니다!**

<br>

### FlexFlow 라이선스 유형
FlexFlow의 기본 프레임워크 라이선스 유형입니다.

|디렉토리|파일|설명|라이선스 유형|
|:---:|:---:|:---:|:---:|
|`FlexHMI/Core/`|`*`|FlexHMI 코어 유저 인터페이스|<a href="./MIT">MIT</a>|
|`FlexHMI/Share/`|`*`|FlexHMI 인터페이스 공유 콘텐츠|<a href="./MIT">MIT</a>|
|`FlexHMI/Share/scripts/`|`paho_mqtt.js`|MQTT 통신 라이브러리|<a href="./EDL1">EDL1</a>|
|`FlexHMI/SystemUI/`|`*`|FlexHMI 시스템 유저 인터페이스|<a href="./MIT">MIT</a>|
|`FlexHMI/ControlUI/`|`*`|FlexHMI 컨트롤 유저 인터페이스|<a href="./MIT">MIT</a>|
|`framework/`|`FlexVision.py`|FlexFlow 비전 연산 프레임워크|<a href="./AGPL3">AGPL3</a>|
|`framework/`|`FlexDebug.py`|FlexFlow 프레임워크 디버거|<a href="./MIT">MIT</a>|
|`framework/`|`FlexMQTT.py`|MQTT 통신 프레임워크|<a href="./EDL1">EDL1</a> <a href="./EPL2">EPL2</a>|
|`Tools/`|`*`|FlexFlow 구축을 위한 유용한 도구|<a href="./MIT">MIT</a>|
|`res/`|`*`|마크다운 문서 리소스|-|

<br>

### INSIDE X 라이선스 유형
FLexFlow의 예제 중 하나인 미니 스마트팩토리 INSIDE X의 라이선스 유형입니다.

|디렉토리|파일|설명|라이선스 유형|
|:---:|:---:|:---:|:---:|
|`Jetson/Frontend/`|`*`|INSIDE X 컨트롤 유저 인터페이스|<a href="./MIT">MIT</a>|
|`Jetson/Backend/`|`*`|INSIDE X 백엔드 서버|`프레임워크 종속`|
|`Models/`|`*`|Classify 비전 모델|-|
|`PCB/`|`*`|입/출력 통합 컨트롤러 보드 설계 파일|<a href="./MIT">MIT</a>|
|`CAD/`|`*`|INSIDE X 인벤터 설계 파일|<a href="./MIT">MIT</a>|
|`Program/`|`*`|PLC 및 슬레이브 디바이스 프로그램|<a href="./MIT">MIT</a>|

</div>
