# YouTube 영상 다운로드 도구

이 프로젝트는 `yt-dlp`를 사용해 **본인이 권리를 가진 영상** 또는 다운로드가 허용된 영상을 저장하는 간단한 CLI 예시입니다.

## 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 사용법

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

옵션:

- `-o, --output-dir`: 저장 경로 (기본값: `downloads`)
- `-f, --format`: yt-dlp 포맷 선택자

예시:

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -o my_videos -f "best"
```

## 주의

- 저작권 및 플랫폼 이용약관을 반드시 준수하세요.
- 허가 없이 타인의 저작물을 다운로드/재배포하지 마세요.
