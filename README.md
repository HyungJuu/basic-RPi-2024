# basic-RPi-2024
부경대 2024 IoT 개발자과정 오픈하드웨어 플랫폼활용 리포지토리

- putty
    - 연결된 라즈베리파이 정보 >> pinout 
    - 라즈베리파이에서 파이썬 실행 방법 >> python 실행파일명

## 1일차(24.06.20)
- 라즈베리파이 기초
    - 기초
        - 전류(암페어,A) : 전자의 흐름
        - 전압(볼트, V) : 전기 에너지의 압력, 전기장 안에서 전하가 갖는 전위 차 (높은곳 &rarr; 낮은곳)
        - 저항(옴, Ω) : 전기회로에서 전류가 흐르는 것을 방해하는 정도
        <br><br>
        - 전압의 차이가 있어야 전류가 흐름
        - 모든 전류는 Ground로 흐름
    
        - GND(Ground) : 0V
            - 전류를 모은다
            - 전압의 기준이 된다(기준전압)
    
    - 옴의 법칙
        - 전압(V) = 전류(I) * 저항(R)

    - 키르히호프 법칙
        - 전압법칙(KVL) : 폐회로에서 모든 전압의 합은 0 이다
        - 전류법칙(KCL) : 한점으로 흘러들어오는 전류의 합은 흘러나가는 전류의 합과 같다

- Python
    - GPIO 설정함수
        - GPIO.setmode(GPIO.BOARD) - wPi
        - GPIO.setmode(GPIO.BCM) - BCM
        - GPIO.setup(channel, GPIO.mode)
            - channel : 핀번호
            - mode : IN/OUT
        - GPIO.cleanup()
    
    - GPIO 출력함수
        - GPIO.output(channel, state)
            - channel : 핀번호
            - state : HIGH/LOW or 1/0 or Ture/False
    
    - GPIO 입력함수
        - GPIO.input(channel)
            - channel : 핀번호
            - 반환값 : HIGH/LOW or 1/0 or Ture/False
    
    - 시간지연 함수
        - time.sleep(secs)

- 브레드보드(가로로 연결되어 있음)
    - (-) : GRD 연결
    - (+) : 핀 연결

    <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi001.png" width="400" alt="브레드보드">

    <!-- ![브레드보드](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi001.png?token=GHSAT0AAAAAACSM5LEPLWY2B73KWTTI4SL6ZTUY2AA) -->

- LED
    - VCC : 전압(Volt) &rarr; 전원이 공급되는 핀
        - 5V &rarr; LED &rarr; GND
            - 5V에 연결하면 전류가 나와서
            - 나온 전류가 LED를 거쳐
            - 그라운드로 흐른다
                - 5V의 전류가 GND(0V)와의 전압차로 흐르기 때문에 LED의 R, G, B를 GND에 연결하면 해당 LED의 상태가 ON/OFF 된다

    - 실습
        - LED : LED ON &rarr; led01.py
        - LED : 1초마다 LED 색상 변환 &rarr; led02.py

- 스위치(Switch)
    - 저항 : 전류의 흐름을 방해하는 역할
    - 플로팅 상태(Floating)
        - High(1)도 Low(0)도 아닌 그 중간의 전압상태
        - 플로팅 상태를 제거해주는 회로 = 풀업 / 풀다운 저항
        
    - 풀업 저항(Full-up)
        - vcc(1)에 연결된 저항  
            &rarr; 스위치를 누르지 않았을 때, 평상시 1(VCC에서 나온 전류)  
            &rarr; 스위치를 눌렀을 때, 0 (GND와 연결되면서 VCC와 INPUT에서 나온 전류가 모두 0V인 GND로 흐름 &rarr; LOW)  

            <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi002.png" width="500" alt="풀업 저항의 도식화">

            <!-- ![풀업 저항의 도식화](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi002.png?token=GHSAT0AAAAAACSM5LEPF2ZLAD74EHKQYYBGZTUY5DA) -->

    - 풀다운 저항(Full-down)
        - GND(0)에 연결된 저항  
            &rarr; 스위치를 누르지 않았을 때, 평상시 0 (0V인 GRN와 연결되어 전류가 흘러감)  
            &rarr; 스위치를 눌렀을 때, 1 (GND 앞의 저항보다 낮은 INPUT방향으로 전류가 흐름)  

            <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi003.png" width="500" alt="풀다운 저항의 도식화">

            <!-- ![풀다운 저항의 도식화](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi003.png) -->

        | 구분 | 스위치 ON/OFF 여부 | 최종 입력결과 |
        | :---: | :---: | :---: |
        | 풀업 저항<br>(Pull - up) | OFF(0)<br>- - - - -<br>ON(1) | HIGH(1)<br>- - - - -<br>LOW(0) |
        | 풀다운 저항<br>(Pull - down) | OFF(0)<br>- - - - -<br>ON(1) | LOW(0)<br>- - - - -<br>HIGH(1) |
    - 실습
        - 스위치 : 스위치 입력시 문자출력 &rarr; input01.py
        - 스위치 + LED : 스위치 입력마다 LED 색상 변환 &rarr; input02.py
        - 스위치(키보드) + LED : 키보드의 o/x 입력시 LED on/off &rarr; input03.py

- 인터룹트(interrupt) &rarr; inter01.py (에러)
    - 어떤 상황에서도 제일 우선적으로 실행되는 동작


- 피에조 부저
    - PWM(Pulse Width Modulation) : 디지털 신호를 아날로그 신호처럼 동작시키는 기능
    - Duty Cycle : 주기적으로 장치가 on/off되는 시간의 비율  
        &rarr; 5V의 duty cycle이 50%면 2.5V의 효과를 나타냄

    - 실습
        - 피에조 부저 : 디지털 음계 출력 &rarr; pwm01.py
        - 피에조부저 + 스위치(키보드) : 키보드(1~8)키로 디지털 음계 출력 &rarr; input04.py

            ```python
            # 디지털 음계 (Hz)
            piezoPin = 13
            melody = [262, 294, 330, 349, 392, 440, 494, 524]
            # 아날로그 출력을 위한 PWM 객체생성(440HZ 출력)
            Buzz = GPIO.PWM(piezoPin, 440) 

            try:
                while Ture:
                    a = input('키 입력 >> ')
                    if a == '1': # 입력한 키가 1이면
                        Buzz.start(50) # 부저음 시작. duty cycle: 50(%)
                        Buzz.ChangeFrequency(melody[0]) # 부저음을 melody[0]으로 변환(출력)
                        time.sleep(0.1) # 0.1초의 딜레이
                        Buzz.stop() # 부저음 종료
            ```

            <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi004.png" width="600" alt="피에조 주파수">

    <!-- ![피에조 주파수](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi004.png?token=GHSAT0AAAAAACSM5LEO226FIN546UIZBGKQZTUY5IQ) -->

## 2일차(24.06.21)
- 적외선 센서
    - 실습
        - 적외선센서 : 물체 감지 &rarr; pir01.py
        - 적외선센서 + LED : 현관문(or 화장실) 센서기능 &rarr; pir02.py

- 가상환경 env
    - 생성방법 : python -m venv env
    - 접속방법 : source ./env/bin/activate
        - 접속시 경로 앞에 (env) 붙음
        - 이후 실행은 똑같음
    - 종료방법 : deactivate

    ![가상환경](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi005.png)

- 연결상태 확인방법

    ```
    > sudo git clone https://github.com/WiringPi/WiringPi
    > cd WiringPi/
    > sudo ./build
    > gpio -v
    > gpio readall
    <!-- led에 불이 계속 들어올 경우, 해당 핀의 V 상태 확인 후 코드상에서 Ture로 초기화 -->
    ```

    ![연결상태](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi006.png)

- 초음파센서
    - time.time() : 현재시간
    - 실습
        - 초음파센서 : 거리감지 &rarr; ultra01.py
        - 초음파센서 + 피에조부저 + LED : 차량 후방감지센서 기능 &rarr; ultra02.py

## 3일차(24.06.24)
- 1채널 릴레이(Relay) 모듈
    - 전자석의 원리로, 전류가 흐르면 자기장을 형성해 자석을 끌어 당겼다가, 흐르지 않으면 자석을 놓는 원리 &rarr; 스위치 역할(자동)
    - 낮은 전압으로 높은 전압을 제어하는데 많이 사용

    - 실습
        - 릴레이모듈(NO 연결) + LED &rarr; relay01.py

            ![연결상태](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi007.png)


- 스텝모터
    - 펄스모양의 전압에 의해 일정 각도(스텝 수)만큼 회전하는 모터
    - 회전각도는 입력 펄스신호의 수에 비례
    - 회전속도 : 입력 펄스신호의 주파수에 비례

        ![스텝모터 드라이버](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi009.png)

    - 실습
        - 스텝모터 &rarr; step01.py

- 웹서버
    - 실습
        - flask01.py
        - flask02.py

            ![flask02.py 실행결과](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi008.png)

        - 라우터 + LED &rarr; flask03.py
            - 기억할 것❗❗
                ```
                - LED에 연결된 VCC = 5V (+)
                - 핀은 (-)에 연결된다
                - 실행시 LED의 불이 꺼져있는 상태로 실행하려면..
                - LED에 연결된 전원(+)과의 전압차를 0으로 만들어야 한다 -> 1(+)
                - LED를 키고싶으면 전압차를 만들어준다 -> 0(-)
                ```
                ```python
                GPIO.output(led, 1) # 전압차 x -> OFF
                GPIO.output(led, 0) # 전압차 o -> ON
                ```
        - 앞의 파일 변형 &rarr; flask04.py
        - flask05.py
        - 192.168.5.3:10011/?이름=user&주소=부산 : get방식 &rarr; flask06.py
            - ? 를 기준으로 key=value 형태로 입력
            - 연결은 & 연산자 사용

                ![실행결과](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi008.png)

- 모듈설치
    ```
    > pip install flask
    ```
- 시스템 패키지 포함된 가상환경 생성
    ``` 
    > python -m venv --system-site-packages env
    ```

## 4일차
- 웹서버
    - 실습
        - HTML
