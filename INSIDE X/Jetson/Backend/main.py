from os import system as query
from time import sleep as delay
from threading import Thread

from framework.FlexVision import FlexVision
from framework.FlexMQTT import FlexMQTT


# 클래스 인스턴스 생성
vision = FlexVision("../../Models/StelraCMF/StelraCMF.pt", 0)
mqtt = FlexMQTT("127.0.0.1", 2006, "asm", "jetson01")

# 카운터 딕셔너리 선언
count = {"red" : 0, "green" : 0, "yellow" : 0, "white" : 0}

# 토픽 딕셔너리 선언
TOPIC = {
    "red"    : mqtt.topic(mqtt.MEMORY, "1x0"),
    "green"  : mqtt.topic(mqtt.MEMORY, "1x1"),
    "yellow" : mqtt.topic(mqtt.MEMORY, "1x2"),
    "white"  : mqtt.topic(mqtt.MEMORY, "1x3"),
    "image"  : mqtt.topic(mqtt.MEMORY, "2x0")
}


# 프로그램 초기화
def init():
    vision.load_model(method="cuda")
    vision.set_ROI((210, 302, 154, 152))
    vision.set_prob(0.6)
    vision.detect_handler(count_update)
    
    mqtt.start()


# 메인 프로그램
def main():
    if vision.attach():
        # 비전 연산 시작
        vision.start(window=True, dict_labal=count)
        
        # 이미지 업데이트 쓰레드 시작
        T = Thread(target=image_update)
        T.start()
        
        # 웹 HMI 실행
        query("firefox --kiosk '127.0.0.1/FlexHMI/Core'")


# 카운터 업데이트
def count_update():
    value = vision.best
    if value[0] != "none":
        count[value[0]] += 1
        mqtt.publish(TOPIC[value[0]], count[value[0]])
  
        
# 이미지 업데이트 
def image_update():
    while True:
        frame = vision.to_ROI(vision.call_frame())
        data = vision.frame_to_base64(frame)
        mqtt.publish(TOPIC['image'], data, False)
        delay(0.05)


if __name__ == '__main__':
    init()
    main()