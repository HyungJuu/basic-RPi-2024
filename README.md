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

    <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi001.png?token=GHSAT0AAAAAACSM5LEPLWY2B73KWTTI4SL6ZTUY2AA" width="400" alt="브레드보드">

    <!-- ![브레드보드](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi001.png?token=GHSAT0AAAAAACSM5LEPLWY2B73KWTTI4SL6ZTUY2AA) -->

- LED &rarr; led01.py, led02.py
    - VCC : 전압(Volt) &rarr; 전원이 공급되는 핀
        - 5V &rarr; LED &rarr; GND
            - 5V에 연결하면 전류가 나와서
            - 나온 전류가 LED를 거쳐
            - 그라운드로 흐른다
                - 5V의 전류가 GND(0V)와의 전압차로 흐르기 때문에 LED의 R, G, B를 GND에 연결하면 해당 LED의 상태가 ON/OFF 된다

- 스위치(Switch) &rarr; input01.py ~ input04.py
    - 저항 : 전류의 흐름을 방해하는 역할
    - 플로팅 상태(Floating)
        - High(1)도 Low(0)도 아닌 그 중간의 전압상태
        - 플로팅 상태를 제거해주는 회로 = 풀업 / 풀다운 저항
        
    - 풀업 저항(Full-up)
        - vcc(1)에 연결된 저항  
            &rarr; 스위치를 누르지 않았을 때, 평상시 1(VCC에서 나온 전류)  
            &rarr; 스위치를 눌렀을 때, 0 (GND와 연결되면서 VCC와 INPUT에서 나온 전류가 모두 0V인 GND로 흐름 &rarr; LOW)  

            <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi002.png?token=GHSAT0AAAAAACSM5LEPF2ZLAD74EHKQYYBGZTUY5DA" width="500" alt="풀업 저항의 도식화">

            <!-- ![풀업 저항의 도식화](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi002.png?token=GHSAT0AAAAAACSM5LEPF2ZLAD74EHKQYYBGZTUY5DA) -->

    - 풀다운 저항(Full-down)
        - GND(0)에 연결된 저항  
            &rarr; 스위치를 누르지 않았을 때, 평상시 0 (0V인 GRN와 연결되어 전류가 흘러감)  
            &rarr; 스위치를 눌렀을 때, 1 (GND 앞의 저항보다 낮은 INPUT방향으로 전류가 흐름)  

            <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi003.png?token=GHSAT0AAAAAACSM5LEP54OQWD44PFNF4LPOZTUY5GQ" width="500" alt="풀다운 저항의 도식화">

            <!-- ![풀다운 저항의 도식화](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi003.png) -->

        | 구분 | 스위치 ON/OFF 여부 | 최종 입력결과 |
        | :---: | :---: | :---: |
        | 풀업 저항<br>(Pull - up) | OFF(0)<br>- - - - -<br>ON(1) | HIGH(1)<br>- - - - -<br>LOW(0) |
        | 풀다운 저항<br>(Pull - down) | OFF(0)<br>- - - - -<br>ON(1) | LOW(0)<br>- - - - -<br>HIGH(1) |

- 인터룹트(interrupt) &rarr; inter01.py (에러)
    - 어떤 상황에서도 제일 우선적으로 실행되는 동작


- 피에조 부저 &rarr; pwm01.py, input04.py
    - 마이너스 연결 : GRD 연결
    - 플러스 : 주파수를 발생시킬 핀 연결
    
    <img src="https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi004.png?token=GHSAT0AAAAAACSM5LEO226FIN546UIZBGKQZTUY5IQ" width="600" alt="피에조 주파수">

    <!-- ![피에조 주파수](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi004.png?token=GHSAT0AAAAAACSM5LEO226FIN546UIZBGKQZTUY5IQ) -->

## 2일차(24.06.21)
- 적외선 센서 &rarr; pir01.py, pir02.py

- 가상환경 env
    - 생성방법 : python -m venv env
    - 접속방법 : source ./env/bin/activate
        - 접속시 경로 앞에 (env) 붙음
        - 이후 실행은 똑같음
    - 종료방법 : deactivate

    ![가상환경](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi005.png?token=GHSAT0AAAAAACSM5LEOLIWKBZAQDB5PNLIIZTU6BKQ)

- 연결상태 확인방법

    ```
    > sudo git clone https://github.com/WiringPi/WiringPi
    > cd WiringPi/
    > sudo ./build
    > gpio -v
    > gpio readall
    <!-- led에 불이 계속 들어올 경우, 해당 핀의 V 상태 확인 후 코드상에서 Ture로 초기화 -->
    ```

- 초음파센서 &rarr; ultra01.py
    - time.time() : 현재시간