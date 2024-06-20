# basic-RPi-2024
부경대 2024 IoT 개발자과정 오픈하드웨어 플랫폼활용 리포지토리

- putty &rarr; pinout 입력하면 연결된 라즈베리파이 보여줌
- 라즈베리파이 파이썬 실행 방법 : python 실행파일명

## 1일차(24.06.20)
- 라즈베리파이 기초
    - 기초
        - 전류(암페어,A) : 전자의 흐름
        - 전압(볼트, V) : 전기 에너지의 압력, 전기장 안에서 전하가 갖는 전위 차 (높은곳 &rarr; 낮은곳)
        - 저항(옴, Ω) : 전기회로에서 전류가 흐르는 것을 방해하는 정도
    
    - 옴의 법칙
        - 전압(V) = 전류(I) * 저항(R)

    - 키르히호프 법칙
        - 전압법칙
        - 전류법칙

    - 전압의 차이가 있어야 전류가 흐름
    - 모든 전류는 Ground로 흐름
    - Ground(GND)
        - 전류를 모은다
        - 전압의 기준이 된다(기준전압)

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

    ![브레드보드](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi001.png)

- LED
    - 전압(Volt) : VCC &rarr; 전원이 공급되는 핀
        - 5V 연결 &rarr; 전류가 나와서 &rarr; LED를 거쳐 &rarr; GND (0V)
            - 전류는 GND로 흐르기 때문에 R, G, B를 GND에 연결하면 해당 LED의 상태가 ON/OFF 된다

- 스위치
    - 저항 : 전류의 흐름을 방해하는 역할
    - 플로팅 상태(Floating)
        - High(1)도 Low(0)도 아닌 그 중간의 전압상태
        - 플로팅 상태를 제거해주는 회로 = 풀업 / 풀다운 저항
        
    - 풀업 저항
        - vcc(1)에 연결된 저항  
            &rarr; 스위치를 누르지 않았을 때, 평상시 1(VCC에서 나온 전류)  
            &rarr; 스위치를 눌렀을 때, 0 (GND와 연결되면서 VCC와 INPUT에서 나온 전류가 모두 0V인 GND로 흐름 &rarr; LOW)  

            ![풀업 저항의 도식화]((https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi002.png))

    - 풀다운 저항
        - GND(0)에 연결된 저항  
            &rarr; 스위치를 누르지 않았을 때, 평상시 0 (0V인 GRN와 연결되어 전류가 흘러감)  
            &rarr; 스위치를 눌렀을 때, 1 (GND 앞의 저항보다 낮은 INPUT방향으로 전류가 흐름)  

            ![풀다운 저항의 도식화](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi003.png)

        | 구분 | 스위치 ON/OFF 여부 | 최종 입력결과 |
        | :---: | :---: | :---: |
        | 풀업 저항<br>(Pull - up) | OFF(0)<br>- - - - -<br>ON(1) | HIGH(1)<br>- - - - -<br>LOW(0) |
        | 풀다운 저항<br>(Pull - down) | OFF(0)<br>- - - - -<br>ON(1) | LOW(0)<br>- - - - -<br>HIGH(1) |

- 피에조 부저
    - 마이너스 연결 : GRD 연결
    - 플러스 : 주파수를 발생시킬 핀 연결

    ![피에조 주파수](https://raw.githubusercontent.com/HyungJuu/basic-RPi-2024/main/images/rpi004.png)
