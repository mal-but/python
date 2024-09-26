import os
from google.cloud import texttospeech

# 환경 변수 설정으로 인증 정보 제공
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\조현태\OneDrive\바탕 화면\Google TTS\malbut-da37fdfe40df.json"

# TTS 클라이언트 초기화
client = texttospeech.TextToSpeechClient()

# 변환할 텍스트 설정
text_to_convert = input("여기에 변환할 텍스트를 입력하세요. : ")
synthesis_input = texttospeech.SynthesisInput(text=text_to_convert)

# 음성 설정
voice = texttospeech.VoiceSelectionParams(
    language_code="ko-KR",  # 한국어 선택
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# 오디오 설정
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# 파일 이름을 입력받음
file_name = input("저장할 파일 이름을 입력하세요 (확장자 없이 입력): ") + ".mp3"

# TTS 요청 및 응답
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# 현재 파일이 실행되고 있는 디렉토리 경로를 얻음
current_directory = os.path.dirname(os.path.abspath(__file__))
current_directory += "/sound"

# 파일을 현재 디렉토리에 저장
file_path = os.path.join(current_directory, file_name)
with open(file_path, "wb") as out:
    out.write(response.audio_content)
    print(f"MP3 파일이 '{file_name}'로 저장되었습니다.")
