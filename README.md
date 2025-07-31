# Codex Kids

## 개요 (한국어)

Codex Kids는 어린 학습자가 코딩 개념을 쉽게 이해할 수 있도록 돕는 시각적 프로그래밍 플랫폼입니다. 단계별 실습을 통해 점차 고급 개념을 배우며, 최종적으로 데이터 과학과 인공지능 학습을 준비하도록 설계되었습니다.

자세한 내용은 [기술 계획서](code-kids-technical-plan.md)를 참고하세요.

## 설치

### 백엔드

1. Python 3.10 이상을 설치합니다.
2. 가상 환경을 만들고 의존성을 설치합니다:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 프론트엔드

1. Node.js 18 이상을 설치합니다.
2. 의존성을 설치합니다:

```bash
cd frontend
npm install
```

## 개발

### 서버 실행

백엔드 API를 실행하려면:

```bash
cd backend
uvicorn main:app --reload
```

프론트엔드 개발 서버를 실행하려면:

```bash
cd frontend
npm start
```

### 기여

이 저장소로 풀 리퀘스트를 보내 기여해 주세요.

---

## Overview

Codex Kids is a visual programming platform designed to help young learners discover coding concepts. The project aims to offer hands-on lessons that gradually introduce more advanced topics and ultimately prepare students for data science and AI.

See the [technical plan](code-kids-technical-plan.md) for a full breakdown of the architecture and features.

## Setup

### Backend

1. Install Python 3.10 or newer.
2. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### Frontend

1. Install Node.js (version 18 or newer).
2. Install dependencies:

```bash
cd frontend
npm install
```

## Development

### Running the servers

Start the backend API:

```bash
cd backend
uvicorn main:app --reload
```

Launch the frontend development server:

```bash
cd frontend
npm start
```

### Contributing

Please submit issues and pull requests to this repository. Contributions for both the frontend and backend are welcome.
