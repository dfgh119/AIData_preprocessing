import ffmpeg
# import sys
import glob
import os 
import xml.etree.ElementTree as ET
import subprocess
import shlex
import datetime

file_path = './data/'
result_folder = f'{file_path}result'


if not os.path.isdir(result_folder):
        os.mkdir(result_folder)


#디렉토리 내에 mp4파일과 xml 파일만 찾음
xmlname = glob.glob(f'{file_path}*xml')


# sys.path.append(r'C:\Users\DIP아카데미센터-KDigital06\Desktop\wkit\ffmpeg-5.1-full_build\bin') 
for xml_file in xmlname :
    doc = ET.parse(xml_file)
    #root노드 가져오기
    root = doc.getroot()
    #xml 파일안에 Alarm 태그만 검색
    for Alarm in root.findall("./Library/Clip/Alarms/Alarm"):
        start = Alarm.find('StartTime').text
        AlarmDuration = Alarm.find('AlarmDuration').text
        AlarmDescription = Alarm.find('AlarmDescription').text
        Start_Frame = 0
        End_Frame = 0
        print(start,"에서부터 ",AlarmDuration,"동안", AlarmDescription)
     
    s = os.path.join(file_path,root.find("./Library/Clip/Header/Filename").text)
    s = xml_file[:-4]+'.mp4'
    if not os.path.isfile(s):
        print('not_found_file : %s'%(s))
        continue
    
    
    
    #./data/result output + basename(s)
    d = os.path.join(result_folder,"output"+os.path.basename(s))
    test_d = result_folder + "/output" + os.path.basename(s)



    #s == input location
    stream = ffmpeg.input(s) # video location
    stream = stream.trim(start = start, duration=AlarmDuration).filter('setpts', 'PTS-STARTPTS')
    stream = ffmpeg.output(stream, d)
    #d == ./data/result/output/xmlfile.mp4

    
    #result_folder = f'{file_path}result'
    ffmpeg.run(stream)
    
    editimage_result_folder = f'{result_folder}/'+ os.path.basename(s)[:-4]
    #./data/result/output/xmlfile[:-4](.mp4)

    if not os.path.isdir(editimage_result_folder):
        os.mkdir(editimage_result_folder)
    # 추출된 영상에서 1프레임당 한장씩 자르도록
    command = f"ffmpeg -ss 00:00:0 -i {test_d} -r 1 -f image2 {editimage_result_folder}/{os.path.basename(s)}-%d.jpg"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    for line in process.stdout:
        now = datetime.datetime.now()
        print(now, line)    




