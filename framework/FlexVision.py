import cv2, base64

from threading import Thread
from framework.FlexDebug import FlexDebug
from ultralytics import YOLO


debug = FlexDebug()


class FlexVision:
    """
    # FlexVision
    FlexFlow를 위한, 유연하고 빠른 비전 연산 라이브러리.
    """
    def __init__(self, model_path: str, device_index: int):
        """
        ## FlexVision 초기화
        - FlexVision을 사용하기 위하여, 새로운 클래스 인스턴스를 생성합니다.
        
        ---

        Args:
            model_path: 연산을 위한 모델의 경로를 정의합니다.
            device_index: 연산을 위한 캡쳐 장치의 번호를 정의합니다.
        """
        try:
            self.processing = False             # 연산 여부
            
            self.model_path = model_path        # 모델 경로
            self.device_index = device_index    # 캡쳐 장치 번호
            
            self.handler_func = None            # 핸들러 함수
            self.handler_args = None            # 핸들러 인자
            
            self.capture = None                 # 캡쳐 장치 객체
            self.ROI = None                     # 캡쳐 관심 영역
            
            self.model = None                   # 비전 모델
            self.prob = 0.75                    # 식별 정확도
            
            self.classes = None                 # 모델의 전체 클래스
            self.class_cache = [None, None]     # 연산 클래스 캐시
            self.best = None                    # 최상위 확률의 클래스와 값
            
            debug.success("FlexVision 라이브러리를 성공적으로 초기화했습니다!")
        except Exception as e:
            debug.err("FlexVision 라이브러리를 초기화하는데 실패했습니다!", e)
        
    def attach(self):
        """
        ## 캡쳐 장치 활성화
        - 캡쳐 장치를 활성화합니다.

        ---

        Returns:
            success: 성공적으로 캡쳐 장치와 연결되었는지 반환합니다.
        """
        try:
            self.capture = cv2.VideoCapture(self.device_index)
            debug.success(f"{self.device_index}번 캡쳐 장치에 성공적으로 연결했습니다!")
            return True
        except Exception as e:
            debug.err("캡쳐 장치에 연결을 실패하였습니다!", e)
            return False
           
    def detach(self):
        """
        ## 캡쳐 장치 비활성화
        - 캡쳐 장치를 비활성화합니다.

        ---

        Returns:
            success: 성공적으로 캡쳐 장치와 연결 해제되었는지 반환합니다.
        """
        try:
            self.capture.release()
            debug.success(f"{self.device_index}번 캡쳐 장치와 성공적으로 연결해제 했습니다!")
            return True
        except Exception as e:
            debug.err("캡쳐 장치를 연결 해제하는 도중 오류가 발생했습니다!", e)
            return False
        
    def load_model(self, method: str = "cpu"):
        """
        ## 모델 가져오기
        - 비전 연산을 위해, 모델 파일을 불러옵니다.

        ---
        
        Args:
            method: 어떤 장치를 사용하여, 연산할 지 선택합니다.
            `cpu`와 `cuda` 장치가 대표적으로 사용됩니다.
            
        ---

        Returns:
            success: 성공적으로 모델을 가져왔는지 반환합니다.
        """
        try:
            self.model = YOLO(self.model_path)
            self.model.to(method)
            debug.success(f"성공적으로 '{self.model_path}' 모델을 가져왔습니다!")
            return True
        except Exception as e:
            debug.err("모델을 가져오는 도중 오류가 발생했습니다!", e)
            return False

    def call_frame(self):
        """
        ## 프레임 가져오기
        - 현재 캡쳐 장치의 프레임을 반환합니다.
        프레임을 읽지 못한 경우에는, `None`을 반환합니다.

        ---

        Returns:
            frame: 현재 프레임을 반환합니다.
        """
        success, frame = self.capture.read()
        if success:
            return frame
        else:
            return None

    def show_frame(self, frame: cv2.typing.MatLike):
        """
        ## 프레임 보여주기
        - 현재 캡쳐 장치의 프레임과 ROI 영역을 함께 보여줍니다.

        ---

        Args:
            frame: 프레임을 인자로 받습니다.

        ---

        Returns:
            success: 성공적으로 프레임을 표시했는지 반환합니다.
        """
        try:
            frame = self.labeling_rect(frame, self.ROI_to_Boxed(), "ROI")
            cv2.imshow("FlexVision", frame)
            return True
        except Exception as e:
            debug.err("프레임을 표시하는 도중 오류가 발생했습니다!", e)
            return False
        
    def labeling_rect(self, frame: cv2.typing.MatLike, point: tuple, label: str):
        """
        ## 영역 라벨링
        - 주어진 평면 좌표 영역을 라벨링합니다.
        라벨링에 실패했을 경우 기존 프레임을 반환합니다.

        ---

        Args:
            frame: 라벨링할 프레임을 설정합니다.
            point: 라벨링 영역을 평면 좌표 영역으로 설정합니다.
            label: 라벨을 설정합니다.

        ---

        Returns:
            frame: 라벨링을 완료한, 프레임을 반환합니다.
        """
        try:
            frame = cv2.rectangle(frame, point[0], point[1], (0, 0, 255), 3)
            frame = cv2.putText(frame, label, (point[0][0], point[0][1] - 8), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
            return frame
        except Exception as e:
            debug.err("영역 라벨링 도중 오류가 발생했습니다!", e)
            return frame
    
    def labeling_dict(self, frame: cv2.typing.MatLike, dict_label: dict):
        """
        ## 딕셔너리 아이템 라벨링
        - 주어진 딕셔너리를 프레임에 라벨링합니다.
        라벨링에 실패했을 경우 기존 프레임을 반환합니다.

        ---

        Args:
            frame: 라벨링할 프레임을 설정합니다.
            dict_label: 딕셔너리 라벨을 설정합니다.

        ---

        Returns:
            frame: 라벨링을 완료한, 프레임을 반환합니다.
        """
        try: 
            for index, item in enumerate(dict_label.items()):
                frame = cv2.putText(frame, f"{item[0]} : {item[1]}", (16, 32 * (index + 1)), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
            return frame
        except Exception as e:
            debug.err("딕셔너리 아이템 라벨링 도중 오류가 발생했습니다!", e)
            return frame
    
    def call_handler(self):
        """
        ## 핸들러 호출
        - 등록 된, 핸들러의 함수를 인자와 함께 실행합니다.

        ---
        
        Returns:
            success: 성공적으로 핸들러를 실행했는지 반환합니다.
        """
        try:
            if self.handler_func != None:
                if self.handler_args != None:
                    self.handler_func(self.handler_args)
                else:
                    self.handler_func()
            debug.success("성공적으로 핸들러를 호출하였습니다!")
            return True
        except Exception as e:
            debug.err("핸들러 호출 도중 오류가 발생했습니다!", e)
            return False
    
    def detect_handler(self, function, args: tuple = None):
        """
        ## 핸들러 등록
        - 새로운 클래스를 감지하였을 때 인자와 함께 함수를 실행합니다.
        
        ---
        
        Args:
            function: 새로운 클래스 감지 시 실행되는 함수입니다.
            args: 함수에 전달되는 인자입니다. (기본값 : `()`)
            
        ---
        
        Returns:
            success: 핸들러 등록의 성공 여부를 반환합니다.
        """
        try:
            self.handler_func = function
            self.handler_args = args
            debug.success("성공적으로 핸들러를 등록하였습니다!")
            return True
        except Exception as e:
            debug.err("핸들러 등록 도중 오류가 발생했습니다!", e)
            return False
    
    def set_ROI(self, ROI: tuple = (0, 0, 0, 0)):
        """
        ## 관심 영역 설정
        - ROI 값을 사용하여, 관심 영역을 설정하거나,
        내장된 도구 사용하여, 관심 영역을 설정할 수 있습니다.
        
        ---
        
        Args:
            ROI: 설정 할 관심 영역 좌표 값입니다. (기본값 : `(0, 0, 0, 0)`)
            
        ---
        
        Returns:
            success: 관심 영역 설정 성공 여부를 반환합니다.
        """
        try:
            if ROI == (0, 0, 0, 0):
                self.ROI = cv2.selectROI("FlexVision - ROI Selector", self.call_frame())
                cv2.destroyAllWindows()
            else:
                self.ROI = ROI
            debug.success("성공적으로 관심 영역 설정하였습니다!")
            return True
        except Exception as e:
            debug.err("관심 영역 설정 도중 오류가 발생했습니다!", e)
            return False
    
    def ROI_to_Boxed(self):
        """
        ## 평면 좌표 영역으로 변환
        - 관심 영역을 평면 좌표 영역으로 변환하여, 반환합니다.
        변환에 실패했을 경우 `None`을 반환합니다.

        ---

        Returns:
            point: 평면 좌표 영역을 반환합니다.
        """
        try:
            return ((self.ROI[0], self.ROI[1]),
                    (self.ROI[2] + self.ROI[0], self.ROI[3] + self.ROI[1]))
        except Exception as e:
            debug.err("평면 좌표 변환 도중 오류가 발생했습니다!", e)
            return None
    
    def set_prob(self, prob: float = 0.75):
        """
        ## 모델 정확도 설정
        - 모델이 감지한 값이 설정 확률 이상이여야, 인식하게 설정합니다.

        ---

        Args:
            prob: 최대 인식 정확도 확률을 설정합니다. (기본값 : `0.75`)

        ---

        Returns:
            success: 모델 정확도 설정 성공 여부를 반환합니다.
        """
        try:
            self.prob = prob
            return True
        except Exception as e:
            debug.err("모델 정확도 설정 도중 오류가 발생했습니다!", e)
            return False
    
    def to_ROI(self, frame: cv2.typing.MatLike):
        """
        ## 관심 영역 프레임 반환
        - 전체 프레임을 인자로 받아, 설정한 관심영역으로 프레임을 변경 후 반환합니다.

        ---

        Args:
            frame: 전체 프레임을 인자로 받습니다.

        ---

        Returns:
            frame: 관심 영역 프레임을 반환합니다.
        """
        return frame[self.ROI[1]:self.ROI[1] + self.ROI[3],
                     self.ROI[0]:self.ROI[0] + self.ROI[2]]
        
    def frame_to_base64(self, frame: cv2.typing.MatLike):
        """
        ## 프레임을 base64로 변환
        - 프레임을 인자로 받아, base64로 인코딩하여, 반환합니다.
        
        ---

        Args:
            frame: 프레임을 인자로 받습니다.
            
        ---

        Returns:
            base64: 프레임을 base64로 인코딩하여, 반환합니다.
        """
        _, buffer = cv2.imencode('.jpg', frame)
        return base64.b64encode(buffer)
    
    def start(self, window: bool = False, dict_labal: dict = None, exit_key: str = 'q'):
        """
        ## 비전 연산 시작
        - 쓰레드를 시작하여, 비전 연산을 시작합니다.
        이미 실행된 연산이 있다면, 시작되지 않습니다.
        
        ---
        
        Args:
            window: 프레임을 윈도우 창으로 표시할 지 선택합니다. (기본 값 : `False`)
            dict_labal: 윈도우 창에 표시할 딕셔너리를 설정합니다. (기본 값 : `{}`)
            exit_key: 윈도우 창을 닫을 키를 지정합니다. (기본 값 : `q`)
            
        ---

        Returns:
            success: 성공적으로 비전 연산을 시작하였는지, 반환합니다.
        """
        try:
            if not self.processing:
                self.processing = True
                T = Thread(target=self.__start__, args=(window, dict_labal, exit_key))
                T.start()
            return True
        except Exception as e:
            debug.err("연산 작업 시작 도중 오류가 발생했습니다!", e)
            return False
    
    def __start__(self, window: bool, dict_label: dict, exit_key: str):
        """
        ## 비전 연산 시작
        - 비전 연산을 시작합니다.
        
        ---

        Args:
            window: 프레임을 윈도우 창으로 표시할 지 선택합니다.
            label: 윈도우 창에 표시할 딕셔너리를 설정합니다.
            exit_key: 윈도우 창을 닫을 키를 지정합니다.
        """
        while self.processing:
            frame = self.call_frame()
        
            ROI_area = self.to_ROI(frame)
            result = self.model(ROI_area, verbose=False)[0]
            
            self.classes    = result.names
            self.best       = (self.classes[result.probs.top1], float(result.probs.top1conf))
            
            if (self.best[1] >= self.prob and
                self.best[0] != self.class_cache[0]):
                    self.call_handler()
                
            self.class_cache = self.best
            
            if window:
                frame = self.labeling_dict(frame, dict_label)
                self.show_frame(frame)
            
            if cv2.waitKey(10) & 0xFF == ord(exit_key):
                break

        if window:
            cv2.destroyAllWindows()
 
    def stop(self):
        """
        ## 비전 연산 시작
        - 비전 연산을 중지합니다.
        """
        self.processing = False