# AI Data preprocessing
## 인공지능 전처리 과정 

1. Json 파일의 shapes/label/points를 이용해 사진의 크기좌표를 구하고 잘라 데이터 라벨링된 사진만 나오도록 코딩
   
3. FFMPEG를 이용하여 xml파일에서 Alarms 항목(Start부터 duration동안)을 가져와 프레임 수 만큼 이미지로 변환
4. YoloV5 모델을 이용하여 데이터 라벨링한 yalm 파일을 가지고 학습, 검증, 예측모델 생성

