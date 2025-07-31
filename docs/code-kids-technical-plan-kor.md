# Codex Kids - 시각적 코딩 교육 플랫폼 통합 기술 상세 기획서

## 1. 프로젝트 개요

### 1.1 프로젝트명
**Codex Kids** - 아이들을 위한 시각적 코딩 학습 플랫폼

### 1.2 프로젝트 목적
데이터과학과 인공지능 분야로 진출할 아이들을 위해, 시각적 요소를 적극 활용한 단계별 코딩 교육 환경을 제공합니다. 단순한 코드 작성을 넘어서, 코드의 동작 원리를 그림과 도표로 이해하고, 다양한 프로그래밍 언어 간의 변환을 통해 폭넓은 사고력을 기를 수 있도록 돕습니다.

### 1.3 핵심 가치
- **시각적 학습**: 추상적인 코딩 개념을 구체적인 그림으로 이해
- **단계적 성장**: 개인 수준에 맞는 맞춤형 학습 경로
- **미래 준비**: 데이터과학/AI 분야로의 자연스러운 연결고리
- **안전한 환경**: 아동 개인정보 보호 및 안전한 학습 환경 제공

## 2. 대상 사용자 및 페르소나

### 2.1 주요 대상
- **1차 대상**: 초등학교 고학년 ~ 중학생 (10-15세)
- **2차 대상**: 교사 및 학부모 (관리자)
- **특징**: 데이터과학, 인공지능 분야에 관심이 있는 학습자
- **기존 경험**: 코딩 경험 무관 (완전 초보자부터 중급자까지)

### 2.2 사용자 페르소나

#### 페르소나 1: 호기심 많은 민지 (12세, 초보자)
- 수학을 좋아하고 패턴 찾기를 즐김
- 복잡한 설명보다는 그림과 예시를 선호
- 성취감을 느낄 수 있는 단계별 학습 원함

#### 페르소나 2: 탐구적인 준호 (14세, 중급자)
- 이미 스크래치나 기초 파이썬 경험 있음
- "왜 이렇게 작동하는가?"에 대한 깊은 궁금증
- 여러 언어의 차이점과 공통점에 관심

#### 페르소나 3: 열정적인 김 선생님 (35세, 교사)
- 정보 교과 담당 교사
- 학생들의 학습 진도 관리 필요
- 평가 도구와 과제 배포 기능 요구

## 3. 핵심 기능 및 기술 구현

### 3.1 적응형 학습 시스템

#### 수준 진단 시스템
```python
# 학습자 수준 평가 알고리즘
class LearnerAssessment:
    def __init__(self):
        self.difficulty_levels = {
            'beginner': {'score_range': (0, 30), 'features': ['visual_blocks', 'step_execution']},
            'elementary': {'score_range': (31, 60), 'features': ['basic_python', 'simple_loops']},
            'intermediate': {'score_range': (61, 80), 'features': ['functions', 'data_structures']},
            'advanced': {'score_range': (81, 100), 'features': ['algorithms', 'optimization']}
        }
    
    def assess_level(self, test_results):
        # 적응형 평가 로직
        score = self.calculate_score(test_results)
        return self.determine_level(score)
```

#### 초보자 모드 - 기술 구현
- **스토리텔링 주석 생성기**
  ```javascript
  // Vue 컴포넌트 예시
  const CommentGenerator = {
    async generateComment(code) {
      // 로컬 처리 우선
      const localComment = this.getLocalComment(code);
      if (localComment) return localComment;
      
      // 복잡한 코드만 AI API 호출
      if (this.isComplexCode(code)) {
        return await this.callCodexAPI(code);
      }
    }
  }
  ```

- **단계별 실행 시각화**
  ```javascript
  // 코드 실행 시각화 엔진
  class ExecutionVisualizer {
    constructor() {
      this.canvas = document.getElementById('visualization');
      this.ctx = this.canvas.getContext('2d');
    }
    
    visualizeStep(line, variables) {
      // 변수 상태를 애니메이션으로 표현
      this.animateVariableChange(variables);
      this.highlightCurrentLine(line);
    }
  }
  ```

#### 중급자 모드 - 언어 변환 엔진
```python
# 언어 간 변환 서비스
class CodeTranslator:
    def __init__(self):
        self.translators = {
            ('python', 'javascript'): PythonToJSTranslator(),
            ('javascript', 'python'): JSToPythonTranslator(),
            ('scratch', 'python'): ScratchToPythonTranslator()
        }
    
    def translate(self, code, from_lang, to_lang):
        translator = self.translators.get((from_lang, to_lang))
        if not translator:
            return self.fallback_to_ai(code, from_lang, to_lang)
        return translator.translate(code)
```

### 3.2 시각적 학습 도구 - 상세 구현

#### 알고리즘 시각화 엔진
```javascript
// D3.js 기반 정렬 알고리즘 시각화
class SortingVisualizer {
  constructor(containerId) {
    this.svg = d3.select(`#${containerId}`)
      .append('svg')
      .attr('width', 800)
      .attr('height', 400);
    
    this.animationSpeed = 1000; // ms
    this.data = [];
  }
  
  async visualizeBubbleSort(array) {
    this.data = array.map((val, idx) => ({value: val, index: idx}));
    
    for (let i = 0; i < array.length - 1; i++) {
      for (let j = 0; j < array.length - i - 1; j++) {
        // 비교할 요소 하이라이트
        await this.highlightElements([j, j + 1], 'comparing');
        
        if (array[j] > array[j + 1]) {
          // 교환 애니메이션
          await this.swapElements(j, j + 1);
          [array[j], array[j + 1]] = [array[j + 1], array[j]];
        }
        
        await this.clearHighlight([j, j + 1]);
      }
      // 정렬된 요소 표시
      await this.markAsSorted(array.length - i - 1);
    }
  }
  
  async swapElements(i, j) {
    const bars = this.svg.selectAll('.bar');
    const bar1 = bars.filter((d, idx) => idx === i);
    const bar2 = bars.filter((d, idx) => idx === j);
    
    return new Promise(resolve => {
      bar1.transition()
        .duration(this.animationSpeed)
        .attr('x', j * 50)
        .on('end', resolve);
      
      bar2.transition()
        .duration(this.animationSpeed)
        .attr('x', i * 50);
    });
  }
}
```

#### 자료구조 시각화 - WebGL 활용
```javascript
// Three.js 기반 트리 구조 시각화
class TreeVisualizer {
  constructor(container) {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer();
    
    container.appendChild(this.renderer.domElement);
    this.nodes = new Map();
    this.edges = [];
  }
  
  createNode(value, position) {
    const geometry = new THREE.SphereGeometry(0.5, 32, 32);
    const material = new THREE.MeshPhongMaterial({color: 0x00ff00});
    const sphere = new THREE.Mesh(geometry, material);
    
    sphere.position.copy(position);
    this.scene.add(sphere);
    
    // 노드 레이블 추가
    const label = this.createTextLabel(value);
    label.position.copy(position);
    this.scene.add(label);
    
    this.nodes.set(value, {mesh: sphere, label: label});
  }
  
  animateInsertion(parentValue, childValue, isLeft) {
    const parent = this.nodes.get(parentValue);
    const childPos = new THREE.Vector3(
      parent.mesh.position.x + (isLeft ? -2 : 2),
      parent.mesh.position.y - 2,
      parent.mesh.position.z
    );
    
    // 노드 생성 애니메이션
    this.createNode(childValue, childPos);
    this.createEdge(parent.mesh.position, childPos);
  }
}
```

### 3.3 협업 및 프로젝트 관리

#### Git 연동 시스템 - 간소화 버전
```python
# 교육용 Git 래퍼
class EduGit:
    def __init__(self, user_id):
        self.user_id = user_id
        self.repo_path = f"/repos/{user_id}"
        
    def simple_commit(self, files, message):
        """학생용 간단한 커밋 인터페이스"""
        # 복잡한 Git 명령을 숨기고 간단한 API 제공
        repo = git.Repo(self.repo_path)
        repo.index.add(files)
        
        # 자동으로 의미있는 커밋 메시지 생성
        if not message:
            message = self.generate_commit_message(files)
        
        repo.index.commit(message)
        return self.create_visual_history()
    
    def create_visual_history(self):
        """커밋 히스토리를 시각적으로 표현"""
        commits = list(self.repo.iter_commits('main', max_count=10))
        return [{
            'id': c.hexsha[:7],
            'message': c.message,
            'timestamp': c.committed_datetime,
            'changes': self.summarize_changes(c)
        } for c in commits]
```

### 3.4 AI 기반 코드 분석 및 피드백

#### 하이브리드 코드 분석 시스템
```python
# FastAPI 엔드포인트
from fastapi import FastAPI, BackgroundTasks
from typing import Optional
import asyncio

app = FastAPI()

class CodeAnalyzer:
    def __init__(self):
        self.local_analyzer = LocalCodeAnalyzer()
        self.ai_analyzer = AICodeAnalyzer()
        self.cache = RedisCache()
    
    async def analyze_code(self, code: str, language: str, user_level: str):
        # 1단계: 캐시 확인
        cache_key = self.generate_cache_key(code, language)
        cached_result = await self.cache.get(cache_key)
        if cached_result:
            return cached_result
        
        # 2단계: 로컬 분석 (빠른 응답)
        local_result = await self.local_analyzer.analyze(code, language)
        
        # 3단계: 복잡도에 따라 AI 분석 결정
        if self.needs_ai_analysis(code, user_level):
            # 비동기로 AI 분석 실행
            asyncio.create_task(self.enhanced_analysis(code, language, cache_key))
            
        return local_result
    
    async def enhanced_analysis(self, code, language, cache_key):
        """백그라운드에서 상세 AI 분석 수행"""
        ai_result = await self.ai_analyzer.analyze(code, language)
        await self.cache.set(cache_key, ai_result, expire=3600)

@app.post("/api/analyze")
async def analyze_code(
    code: str,
    language: str,
    user_level: str,
    background_tasks: BackgroundTasks
):
    analyzer = CodeAnalyzer()
    result = await analyzer.analyze_code(code, language, user_level)
    return {
        "immediate_feedback": result,
        "detailed_analysis_pending": analyzer.needs_ai_analysis(code, user_level)
    }
```

## 4. 기술 스택 및 아키텍처 상세

### 4.1 프론트엔드 아키텍처

#### Vue.js 3 + Nuxt.js 구조
```javascript
// nuxt.config.js
export default {
  ssr: true, // SEO 최적화
  target: 'server',
  
  modules: [
    '@nuxtjs/pwa', // 오프라인 지원
    '@nuxtjs/i18n', // 다국어 지원
    '@nuxtjs/axios',
    '@pinia/nuxt' // 상태 관리
  ],
  
  buildModules: [
    '@nuxt/typescript-build',
    '@nuxtjs/tailwindcss',
    '@nuxtjs/composition-api/module'
  ],
  
  pwa: {
    manifest: {
      name: 'Codex Kids',
      short_name: 'CK',
      theme_color: '#4F46E5'
    },
    workbox: {
      // 오프라인 캐싱 전략
      runtimeCaching: [
        {
          urlPattern: 'https://api.codexkids.com/.*',
          handler: 'NetworkFirst',
          options: {
            cacheName: 'api-cache'
          }
        }
      ]
    }
  }
}
```

#### 컴포넌트 구조
```typescript
// components/CodeEditor/MonacoEditor.vue
<template>
  <div class="code-editor-container">
    <div ref="editorContainer" class="editor"></div>
    <div v-if="showVisualizer" class="visualizer">
      <component :is="currentVisualizer" :code="code" :execution-state="executionState" />
    </div>
  </div>
</template>

<script setup lang="ts">
import * as monaco from 'monaco-editor'
import { ref, onMounted, watch } from 'vue'
import { useCodeAnalysis } from '@/composables/useCodeAnalysis'

const props = defineProps<{
  language: string
  initialCode: string
  userLevel: 'beginner' | 'intermediate' | 'advanced'
}>()

const editorContainer = ref<HTMLElement>()
const code = ref(props.initialCode)
const { analyzeCode, executionState } = useCodeAnalysis()

let editor: monaco.editor.IStandaloneCodeEditor

onMounted(() => {
  // Monaco Editor 설정
  editor = monaco.editor.create(editorContainer.value!, {
    value: code.value,
    language: props.language,
    theme: 'vs-dark',
    minimap: { enabled: false },
    fontSize: 14,
    lineNumbers: props.userLevel !== 'beginner' ? 'on' : 'off',
    glyphMargin: true, // 중단점 표시용
    automaticLayout: true
  })
  
  // 실시간 코드 분석
  editor.onDidChangeModelContent(debounce(() => {
    code.value = editor.getValue()
    analyzeCode(code.value, props.language)
  }, 500))
  
  // 초보자 모드 향상 기능
  if (props.userLevel === 'beginner') {
    setupBeginnerFeatures(editor)
  }
})

function setupBeginnerFeatures(editor: monaco.editor.IStandaloneCodeEditor) {
  // 마우스 호버 시 설명 표시
  monaco.languages.registerHoverProvider(props.language, {
    provideHover: async (model, position) => {
      const word = model.getWordAtPosition(position)
      if (!word) return
      
      const explanation = await getSimpleExplanation(word.word)
      return {
        contents: [{ value: explanation }]
      }
    }
  })
  
  // 자동 완성 간소화
  monaco.languages.registerCompletionItemProvider(props.language, {
    provideCompletionItems: () => {
      return {
        suggestions: getBeginnerSuggestions(props.language)
      }
    }
  })
}
</script>
```

### 4.2 백엔드 아키텍처

#### FastAPI 서버 구조
```python
# main.py
from fastapi import FastAPI, WebSocket, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import redis.asyncio as redis
from sqlalchemy.ext.asyncio import create_async_engine

# 서비스 임포트
from services.code_analyzer import CodeAnalyzer
from services.visualizer import VisualizationEngine
from services.ai_tutor import AITutor
from services.project_manager import ProjectManager

# 전역 리소스 관리
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 리소스 초기화
    app.state.redis = await redis.create_pool("redis://localhost")
    app.state.db_engine = create_async_engine("postgresql+asyncpg://...")
    
    yield
    
    # 종료 시 리소스 정리
    await app.state.redis.close()
    await app.state.db_engine.dispose()

app = FastAPI(lifespan=lifespan)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://codexkids.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket 연결 관리
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        
    async def broadcast_to_group(self, group_id: str, message: dict):
        # 그룹 협업을 위한 메시지 브로드캐스트
        for user_id, connection in self.active_connections.items():
            if self.is_in_group(user_id, group_id):
                await connection.send_json(message)

manager = ConnectionManager()

# 실시간 협업 엔드포인트
@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_json()
            
            if data["type"] == "code_change":
                # 코드 변경사항 다른 사용자에게 전파
                await manager.broadcast_to_group(
                    data["group_id"],
                    {
                        "type": "code_update",
                        "user_id": user_id,
                        "changes": data["changes"]
                    }
                )
            elif data["type"] == "cursor_position":
                # 커서 위치 공유 (실시간 협업)
                await manager.broadcast_to_group(
                    data["group_id"],
                    {
                        "type": "cursor_update",
                        "user_id": user_id,
                        "position": data["position"]
                    }
                )
    except WebSocketDisconnect:
        manager.disconnect(user_id)
```

#### 데이터베이스 모델
```python
# models/database.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    age_group = Column(String(20))  # 'elementary', 'middle', 'high'
    skill_level = Column(String(20), default='beginner')
    
    # 관계
    projects = relationship("Project", back_populates="owner")
    learning_progress = relationship("LearningProgress", back_populates="user")
    
class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    language = Column(String(20))
    code_content = Column(JSON)  # 버전별 코드 저장
    visibility = Column(String(20), default='private')
    
    # 관계
    owner = relationship("User", back_populates="projects")
    collaborators = relationship("ProjectCollaborator", back_populates="project")
    
class LearningProgress(Base):
    __tablename__ = "learning_progress"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    module_id = Column(String(50))
    completion_percentage = Column(Integer, default=0)
    last_accessed = Column(DateTime)
    performance_metrics = Column(JSON)  # 상세 성과 데이터
    
    # 관계
    user = relationship("User", back_populates="learning_progress")

class CodeExecution(Base):
    __tablename__ = "code_executions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(Text)
    language = Column(String(20))
    execution_time = Column(DateTime)
    result = Column(JSON)
    errors = Column(JSON)
    visualization_data = Column(JSON)  # 시각화에 필요한 데이터
```

### 4.3 보안 및 성능 최적화

#### 보안 미들웨어
```python
# middleware/security.py
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
import re

class SecurityMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, secret_key: str):
        super().__init__(app)
        self.secret_key = secret_key
        self.rate_limiter = RateLimiter()
        
    async def dispatch(self, request: Request, call_next):
        # 1. 인증 토큰 검증
        if not self.is_public_endpoint(request.url.path):
            token = request.headers.get("Authorization")
            if not token or not self.verify_token(token):
                raise HTTPException(status_code=401, detail="Unauthorized")
        
        # 2. Rate Limiting
        client_ip = request.client.host
        if not await self.rate_limiter.is_allowed(client_ip):
            raise HTTPException(status_code=429, detail="Too many requests")
        
        # 3. 입력 검증 (코드 인젝션 방지)
        if request.method == "POST":
            body = await request.body()
            if self.contains_malicious_code(body):
                raise HTTPException(status_code=400, detail="Invalid input")
        
        # 4. 응답 헤더 보안 설정
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        
        return response
    
    def contains_malicious_code(self, code: bytes) -> bool:
        # 위험한 패턴 검사
        dangerous_patterns = [
            r'import\s+os',
            r'import\s+subprocess',
            r'__import__',
            r'eval\s*\(',
            r'exec\s*\(',
            r'open\s*\(',
        ]
        
        code_str = code.decode('utf-8', errors='ignore')
        for pattern in dangerous_patterns:
            if re.search(pattern, code_str):
                return True
        return False
```

#### 성능 최적화 - 캐싱 전략
```python
# services/cache_manager.py
from typing import Optional, Any
import json
import hashlib

class CacheManager:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.ttl = {
            'code_analysis': 3600,      # 1시간
            'visualization': 7200,      # 2시간
            'user_progress': 300,       # 5분
            'static_content': 86400     # 24시간
        }
    
    async def get_or_compute(
        self,
        key: str,
        compute_func,
        category: str = 'default'
    ) -> Any:
        # 캐시 확인
        cached = await self.redis.get(key)
        if cached:
            return json.loads(cached)
        
        # 계산 수행
        result = await compute_func()
        
        # 캐시 저장
        ttl = self.ttl.get(category, 1800)
        await self.redis.setex(
            key,
            ttl,
            json.dumps(result)
        )
        
        return result
    
    def generate_key(self, prefix: str, *args) -> str:
        # 일관된 캐시 키 생성
        content = f"{prefix}:" + ":".join(str(arg) for arg in args)
        return hashlib.md5(content.encode()).hexdigest()
```

### 4.4 오프라인 지원 구현

#### Service Worker 설정
```javascript
// static/sw.js
const CACHE_NAME = 'codex-kids-v1';
const urlsToCache = [
  '/',
  '/css/main.css',
  '/js/app.js',
  '/offline.html',
  // 기본 학습 콘텐츠
  '/api/lessons/basic-python.json',
  '/api/lessons/basic-javascript.json'
];

// 설치 이벤트
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// 요청 가로채기
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // 캐시에 있으면 캐시 반환
        if (response) {
          return response;
        }
        
        // 네트워크 요청
        return fetch(event.request)
          .then(response => {
            // 동적 캐싱
            if (event.request.url.includes('/api/lessons/')) {
              const responseToCache = response.clone();
              caches.open(CACHE_NAME)
                .then(cache => {
                  cache.put(event.request, responseToCache);
                });
            }
            return response;
          })
          .catch(() => {
            // 오프라인 폴백
            if (event.request.destination === 'document') {
              return caches.match('/offline.html');
            }
          });
      })
  );
});

// 백그라운드 동기화
self.addEventListener('sync', event => {
  if (event.tag === 'sync-progress') {
    event.waitUntil(syncUserProgress());
  }
});

async function syncUserProgress() {
  const db = await openDB('codex-kids', 1);
  const tx = db.transaction('pending-progress', 'readonly');
  const pendingData = await tx.objectStore('pending-progress').getAll();
  
  for (const data of pendingData) {
    try {
      await fetch('/api/progress/sync', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
      });
      
      // 성공하면 로컬 데이터 삭제
      await db.delete('pending-progress', data.id);
    } catch (error) {
      console.error('동기화 실패:', error);
    }
  }
}
```

## 5. 시각화 엔진 상세 구현

### 5.1 알고리즘 시각화 프레임워크
```typescript
// visualizer/AlgorithmVisualizer.ts
export abstract class AlgorithmVisualizer {
  protected container: HTMLElement;
  protected animationSpeed: number = 1000;
  protected isPaused: boolean = false;
  protected currentStep: number = 0;
  protected steps: VisualizationStep[] = [];
  
  constructor(container: HTMLElement) {
    this.container = container;
    this.setupControls();
  }
  
  abstract async visualize(input: any): Promise<void>;
  
  protected async executeStep(step: VisualizationStep) {
    if (this.isPaused) {
      await this.waitForResume();
    }
    
    // 단계별 실행
    await step.execute();
    
    // 설명 표시
    this.showExplanation(step.explanation);
    
    // 코드 하이라이트
    this.highlightCode(step.codeLines);
    
    // 애니메이션 대기
    await this.delay(this.animationSpeed);
  }
  
  protected setupControls() {
    const controls = document.createElement('div');
    controls.className = 'visualizer-controls';
    
    // 재생/일시정지 버튼
    const playPauseBtn = document.createElement('button');
    playPauseBtn.onclick = () => this.togglePause();
    
    // 속도 조절
    const speedSlider = document.createElement('input');
    speedSlider.type = 'range';
    speedSlider.min = '100';
    speedSlider.max = '2000';
    speedSlider.value = String(this.animationSpeed);
    speedSlider.oninput = (e) => {
      this.animationSpeed = parseInt((e.target as HTMLInputElement).value);
    };
    
    controls.appendChild(playPauseBtn);
    controls.appendChild(speedSlider);
    this.container.appendChild(controls);
  }
}

// 구체적인 구현 예: 이진 탐색 시각화
export class BinarySearchVisualizer extends AlgorithmVisualizer {
  private array: number[] = [];
  private svg: any; // D3 selection
  
  async visualize(input: {array: number[], target: number}) {
    this.array = input.array;
    this.setupVisualization();
    
    let left = 0;
    let right = this.array.length - 1;
    
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      
      // 탐색 범위 표시
      await this.executeStep({
        execute: async () => {
          this.highlightRange(left, right);
          this.highlightMidpoint(mid);
        },
        explanation: `탐색 범위: ${left}~${right}, 중간값: ${mid}`,
        codeLines: [3, 4] // 해당 코드 라인
      });
      
      if (this.array[mid] === input.target) {
        await this.executeStep({
          execute: async () => this.markAsFound(mid),
          explanation: `찾았습니다! 인덱스 ${mid}에 있습니다.`,
          codeLines: [6]
        });
        return;
      }
      
      if (this.array[mid] < input.target) {
        left = mid + 1;
        await this.executeStep({
          execute: async () => this.adjustRange('left', mid + 1),
          explanation: `중간값이 작으므로 오른쪽 탐색`,
          codeLines: [8, 9]
        });
      } else {
        right = mid - 1;
        await this.executeStep({
          execute: async () => this.adjustRange('right', mid - 1),
          explanation: `중간값이 크므로 왼쪽 탐색`,
          codeLines: [11, 12]
        });
      }
    }
    
    await this.executeStep({
      execute: async () => this.markAsNotFound(),
      explanation: `찾을 수 없습니다.`,
      codeLines: [15]
    });
  }
  
  private highlightRange(left: number, right: number) {
    this.svg.selectAll('.array-element')
      .style('opacity', (d: any, i: number) => 
        i >= left && i <= right ? 1 : 0.3
      );
  }
}
```

### 5.2 데이터 시각화 도구
```python
# services/data_visualizer.py
import plotly.graph_objects as go
import pandas as pd
from typing import Dict, Any, List

class DataVisualizer:
    def __init__(self):
        self.theme = {
            'beginner': {
                'colorscale': 'Viridis',
                'font_size': 14,
                'show_grid': True,
                'annotations': True
            },
            'intermediate': {
                'colorscale': 'Plotly3',
                'font_size': 12,
                'show_grid': True,
                'annotations': False
            }
        }
    
    def create_interactive_chart(
        self,
        data: pd.DataFrame,
        chart_type: str,
        user_level: str = 'beginner'
    ) -> Dict[str, Any]:
        """사용자 수준에 맞는 인터랙티브 차트 생성"""
        
        theme = self.theme[user_level]
        
        if chart_type == 'bar':
            fig = self._create_bar_chart(data, theme)
        elif chart_type == 'scatter':
            fig = self._create_scatter_plot(data, theme)
        elif chart_type == 'line':
            fig = self._create_line_chart(data, theme)
        elif chart_type == 'pie':
            fig = self._create_pie_chart(data, theme)
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")
        
        # 초보자를 위한 추가 설명
        if user_level == 'beginner':
            fig.add_annotation(
                text="💡 그래프를 클릭하거나 드래그해보세요!",
                xref="paper", yref="paper",
                x=0.5, y=1.1,
                showarrow=False,
                font=dict(size=12, color="gray")
            )
        
        return fig.to_dict()
    
    def _create_bar_chart(self, data: pd.DataFrame, theme: Dict) -> go.Figure:
        fig = go.Figure(data=[
            go.Bar(
                x=data.index,
                y=data.iloc[:, 0],
                text=data.iloc[:, 0],
                textposition='auto',
                marker_color='lightblue',
                hovertemplate='<b>%{x}</b><br>값: %{y}<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title="막대 그래프",
            xaxis_title="항목",
            yaxis_title="값",
            font=dict(size=theme['font_size']),
            showlegend=False,
            hovermode='x'
        )
        
        return fig
    
    def create_algorithm_complexity_chart(
        self,
        algorithms: List[str],
        complexities: Dict[str, List[int]]
    ) -> Dict[str, Any]:
        """알고리즘 복잡도 비교 차트"""
        
        fig = go.Figure()
        
        n_values = list(range(1, 101))
        
        for algo in algorithms:
            if algo == 'O(1)':
                y_values = [1] * len(n_values)
            elif algo == 'O(log n)':
                y_values = [math.log2(n) for n in n_values]
            elif algo == 'O(n)':
                y_values = n_values
            elif algo == 'O(n log n)':
                y_values = [n * math.log2(n) for n in n_values]
            elif algo == 'O(n²)':
                y_values = [n**2 for n in n_values]
            
            fig.add_trace(go.Scatter(
                x=n_values,
                y=y_values,
                mode='lines',
                name=algo,
                hovertemplate=f'{algo}<br>n=%{{x}}<br>연산=%{{y:.0f}}<extra></extra>'
            ))
        
        fig.update_layout(
            title="알고리즘 시간 복잡도 비교",
            xaxis_title="입력 크기 (n)",
            yaxis_title="연산 횟수",
            yaxis_type="log",
            hovermode='x unified'
        )
        
        return fig.to_dict()
```

## 6. 교육 콘텐츠 관리 시스템

### 6.1 학습 모듈 구조
```python
# models/learning_module.py
from pydantic import BaseModel
from typing import List, Optional, Dict

class LearningObjective(BaseModel):
    id: str
    description: str
    skills: List[str]
    
class CodeExample(BaseModel):
    language: str
    code: str
    explanation: str
    visualization_type: Optional[str]
    
class Exercise(BaseModel):
    id: str
    title: str
    description: str
    starter_code: str
    test_cases: List[Dict[str, Any]]
    hints: List[str]
    solution: str
    
class LearningModule(BaseModel):
    id: str
    title: str
    description: str
    difficulty: str  # beginner, intermediate, advanced
    estimated_time: int  # minutes
    prerequisites: List[str]
    objectives: List[LearningObjective]
    content_blocks: List[Dict[str, Any]]
    examples: List[CodeExample]
    exercises: List[Exercise]
    
    class Config:
        schema_extra = {
            "example": {
                "id": "python-loops-01",
                "title": "파이썬 반복문 기초",
                "description": "for와 while 반복문을 배워봅시다",
                "difficulty": "beginner",
                "estimated_time": 30,
                "prerequisites": ["python-basics-01"],
                "objectives": [
                    {
                        "id": "obj-01",
                        "description": "for 반복문 이해하기",
                        "skills": ["iteration", "sequences"]
                    }
                ],
                "content_blocks": [
                    {
                        "type": "text",
                        "content": "반복문은 같은 작업을 여러 번 실행할 때 사용합니다."
                    },
                    {
                        "type": "interactive_example",
                        "example_id": "for-loop-fruits"
                    }
                ],
                "examples": [
                    {
                        "language": "python",
                        "code": "for fruit in ['사과', '바나나', '딸기']:\n    print(fruit)",
                        "explanation": "리스트의 각 과일을 하나씩 출력합니다",
                        "visualization_type": "step_through"
                    }
                ],
                "exercises": [
                    {
                        "id": "ex-01",
                        "title": "숫자 출력하기",
                        "description": "1부터 10까지 출력하는 프로그램을 작성하세요",
                        "starter_code": "# 여기에 코드를 작성하세요\n",
                        "test_cases": [
                            {"input": "", "expected_output": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"}
                        ],
                        "hints": ["range(1, 11)을 사용해보세요"],
                        "solution": "for i in range(1, 11):\n    print(i)"
                    }
                ]
            }
        }
```

### 6.2 적응형 학습 경로 생성
```python
# services/adaptive_learning.py
import numpy as np
from typing import List, Dict, Tuple
from collections import defaultdict

class AdaptiveLearningEngine:
    def __init__(self):
        self.skill_graph = self._build_skill_graph()
        self.user_model = {}
        
    def _build_skill_graph(self) -> Dict[str, List[str]]:
        """기술 간 선수 관계 그래프 구축"""
        return {
            'variables': [],
            'data_types': ['variables'],
            'operators': ['variables'],
            'conditionals': ['operators', 'data_types'],
            'loops': ['conditionals'],
            'functions': ['loops', 'conditionals'],
            'lists': ['loops', 'variables'],
            'dictionaries': ['lists'],
            'classes': ['functions', 'dictionaries'],
            'algorithms': ['functions', 'lists'],
            'data_structures': ['classes', 'algorithms']
        }
    
    def assess_user_skills(self, user_id: str, test_results: Dict[str, float]) -> Dict[str, float]:
        """사용자 기술 수준 평가"""
        skill_scores = {}
        
        for skill, score in test_results.items():
            # 베이지안 추정을 사용한 실력 평가
            prior = self.user_model.get(user_id, {}).get(skill, 0.5)
            posterior = self._bayesian_update(prior, score)
            skill_scores[skill] = posterior
        
        self.user_model[user_id] = skill_scores
        return skill_scores
    
    def _bayesian_update(self, prior: float, evidence: float, confidence: float = 0.7) -> float:
        """베이지안 업데이트로 실력 추정"""
        likelihood = evidence * confidence + prior * (1 - confidence)
        return likelihood
    
    def generate_learning_path(
        self,
        user_id: str,
        target_skills: List[str],
        current_skills: Dict[str, float]
    ) -> List[Tuple[str, List[str]]]:
        """개인 맞춤형 학습 경로 생성"""
        
        path = []
        learned_skills = set(skill for skill, score in current_skills.items() if score > 0.7)
        
        # 목표 기술까지의 최단 경로 찾기
        for target in target_skills:
            if target in learned_skills:
                continue
                
            # BFS로 선수 과목 찾기
            prerequisites = self._find_prerequisites(target, learned_skills)
            
            # 난이도 순으로 정렬
            prerequisites.sort(key=lambda x: self._estimate_difficulty(x))
            
            for prereq in prerequisites:
                if prereq not in [p[0] for p in path]:
                    modules = self._get_modules_for_skill(prereq, user_id)
                    path.append((prereq, modules))
            
            # 목표 기술 추가
            modules = self._get_modules_for_skill(target, user_id)
            path.append((target, modules))
        
        return path
    
    def _find_prerequisites(self, skill: str, learned: set) -> List[str]:
        """필요한 선수 기술 찾기"""
        prerequisites = []
        to_check = [skill]
        visited = set()
        
        while to_check:
            current = to_check.pop(0)
            if current in visited:
                continue
            visited.add(current)
            
            if current in self.skill_graph:
                for prereq in self.skill_graph[current]:
                    if prereq not in learned:
                        prerequisites.append(prereq)
                        to_check.append(prereq)
        
        return list(set(prerequisites))
    
    def _get_modules_for_skill(self, skill: str, user_id: str) -> List[str]:
        """기술 학습을 위한 모듈 추천"""
        user_level = self.user_model.get(user_id, {}).get('level', 'beginner')
        
        # 데이터베이스에서 해당 기술과 레벨에 맞는 모듈 조회
        modules = self._query_modules(skill, user_level)
        
        # 사용자 선호도에 따라 정렬
        preferences = self._get_user_preferences(user_id)
        modules.sort(key=lambda m: self._score_module(m, preferences), reverse=True)
        
        return modules[:3]  # 상위 3개 모듈 반환
```

## 7. 실시간 협업 시스템

### 7.1 협업 세션 관리
```typescript
// services/CollaborationService.ts
import { io, Socket } from 'socket.io-client';
import * as Y from 'yjs';
import { WebrtcProvider } from 'y-webrtc';
import { MonacoBinding } from 'y-monaco';

export class CollaborationService {
  private socket: Socket;
  private ydoc: Y.Doc;
  private provider: WebrtcProvider;
  private binding: MonacoBinding | null = null;
  private awareness: any;
  
  constructor(private sessionId: string, private userId: string) {
    this.socket = io('wss://api.codexkids.com');
    this.ydoc = new Y.Doc();
    
    // WebRTC 피어 연결 설정
    this.provider = new WebrtcProvider(sessionId, this.ydoc, {
      signaling: ['wss://api.codexkids.com/signal'],
      password: null,
      awareness: {
        user: {
          name: this.userId,
          color: this.generateUserColor()
        }
      }
    });
    
    this.awareness = this.provider.awareness;
    this.setupEventListeners();
  }
  
  connectToEditor(editor: any) {
    const yText = this.ydoc.getText('code');
    
    this.binding = new MonacoBinding(
      yText,
      editor.getModel(),
      new Set([editor]),
      this.awareness
    );
    
    // 커서 위치 공유
    this.awareness.on('change', () => {
      this.updateCursors();
    });
  }
  
  private updateCursors() {
    const states = this.awareness.getStates();
    
    states.forEach((state, clientId) => {
      if (clientId !== this.awareness.clientID) {
        const user = state.user;
        const cursor = state.cursor;
        
        if (cursor) {
          this.renderRemoteCursor(user, cursor);
        }
      }
    });
  }
  
  private renderRemoteCursor(user: any, cursor: any) {
    // Monaco Editor에 다른 사용자의 커서 표시
    const decoration = {
      range: new monaco.Range(
        cursor.line,
        cursor.column,
        cursor.line,
        cursor.column
      ),
      options: {
        className: `remote-cursor-${user.name}`,
        hoverMessage: { value: `${user.name}의 커서` },
        afterContentClassName: `remote-cursor-flag-${user.name}`,
        afterContent: user.name.substring(0, 2)
      }
    };
    
    // 기존 decoration 업데이트
    this.updateDecoration(user.name, decoration);
  }
  
  // 음성 채팅 기능
  async startVoiceChat() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    
    const peer = new SimplePeer({
      initiator: true,
      stream: stream,
      trickle: false
    });
    
    peer.on('signal', (data) => {
      this.socket.emit('voice-signal', {
        sessionId: this.sessionId,
        signal: data
      });
    });
    
    peer.on('stream', (remoteStream) => {
      const audio = new Audio();
      audio.srcObject = remoteStream;
      audio.play();
    });
    
    this.socket.on('voice-signal', (data) => {
      peer.signal(data.signal);
    });
  }
  
  // 화면 공유
  async shareScreen() {
    const stream = await navigator.mediaDevices.getDisplayMedia({
      video: true,
      audio: false
    });
    
    this.socket.emit('screen-share', {
      sessionId: this.sessionId,
      streamId: stream.id
    });
    
    stream.getVideoTracks()[0].onended = () => {
      this.socket.emit('screen-share-end', {
        sessionId: this.sessionId
      });
    };
  }
  
  // 코드 리뷰 기능
  addComment(lineNumber: number, comment: string) {
    const commentData = {
      id: this.generateId(),
      userId: this.userId,
      lineNumber,
      comment,
      timestamp: new Date().toISOString(),
      resolved: false
    };
    
    this.socket.emit('add-comment', {
      sessionId: this.sessionId,
      comment: commentData
    });
  }
  
  private generateUserColor(): string {
    const colors = [
      '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A',
      '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1F5'
    ];
    return colors[Math.floor(Math.random() * colors.length)];
  }
}
```

## 8. 평가 및 피드백 시스템

### 8.1 자동 코드 평가기
```python
# services/code_evaluator.py
import ast
import asyncio
from typing import Dict, List, Any, Tuple
import pylint.lint
from io import StringIO
import sys

class CodeEvaluator:
    def __init__(self):
        self.sandbox_executor = SandboxExecutor()
        self.style_checker = StyleChecker()
        self.complexity_analyzer = ComplexityAnalyzer()
        
    async def evaluate_submission(
        self,
        code: str,
        language: str,
        test_cases: List[Dict[str, Any]],
        exercise_id: str
    ) -> Dict[str, Any]:
        """제출된 코드 종합 평가"""
        
        evaluation_result = {
            'passed': False,
            'score': 0,
            'test_results': [],
            'style_score': 0,
            'complexity_score': 0,
            'feedback': [],
            'suggestions': []
        }
        
        # 1. 구문 검사
        syntax_check = self.check_syntax(code, language)
        if not syntax_check['valid']:
            evaluation_result['feedback'].append({
                'type': 'error',
                'message': f"구문 오류: {syntax_check['error']}",
                'line': syntax_check.get('line', 0)
            })
            return evaluation_result
        
        # 2. 테스트 케이스 실행
        test_results = await self.run_test_cases(code, test_cases, language)
        evaluation_result['test_results'] = test_results
        
        passed_tests = sum(1 for t in test_results if t['passed'])
        test_score = (passed_tests / len(test_cases)) * 100
        
        # 3. 코드 스타일 검사
        style_result = await self.style_checker.check(code, language)
        evaluation_result['style_score'] = style_result['score']
        evaluation_result['feedback'].extend(style_result['issues'])
        
        # 4. 복잡도 분석
        complexity_result = self.complexity_analyzer.analyze(code, language)
        evaluation_result['complexity_score'] = complexity_result['score']
        
        # 5. 종합 점수 계산
        evaluation_result['score'] = self.calculate_final_score(
            test_score,
            style_result['score'],
            complexity_result['score']
        )
        
        evaluation_result['passed'] = evaluation_result['score'] >= 70
        
        # 6. 개선 제안 생성
        suggestions = await self.generate_suggestions(
            code,
            test_results,
            style_result,
            complexity_result,
            exercise_id
        )
        evaluation_result['suggestions'] = suggestions
        
        return evaluation_result
    
    def check_syntax(self, code: str, language: str) -> Dict[str, Any]:
        """구문 검사"""
        if language == 'python':
            try:
                ast.parse(code)
                return {'valid': True}
            except SyntaxError as e:
                return {
                    'valid': False,
                    'error': str(e),
                    'line': e.lineno
                }
        # 다른 언어 지원 추가
        
    async def run_test_cases(
        self,
        code: str,
        test_cases: List[Dict[str, Any]],
        language: str
    ) -> List[Dict[str, Any]]:
        """샌드박스에서 테스트 케이스 실행"""
        
        results = []
        for i, test_case in enumerate(test_cases):
            result = await self.sandbox_executor.execute(
                code,
                test_case['input'],
                language,
                timeout=5.0  # 5초 제한
            )
            
            passed = result['output'].strip() == test_case['expected_output'].strip()
            
            test_result = {
                'test_id': i,
                'passed': passed,
                'input': test_case['input'],
                'expected': test_case['expected_output'],
                'actual': result['output'],
                'error': result.get('error'),
                'execution_time': result.get('execution_time', 0)
            }
            
            if not passed and not result.get('error'):
                # 차이점 분석
                diff = self.analyze_output_difference(
                    test_case['expected_output'],
                    result['output']
                )
                test_result['difference'] = diff
            
            results.append(test_result)
        
        return results
    
    def calculate_final_score(
        self,
        test_score: float,
        style_score: float,
        complexity_score: float
    ) -> float:
        """가중치를 적용한 최종 점수 계산"""
        weights = {
            'test': 0.6,      # 60%
            'style': 0.2,     # 20%
            'complexity': 0.2  # 20%
        }
        
        return (
            test_score * weights['test'] +
            style_score * weights['style'] +
            complexity_score * weights['complexity']
        )
    
    async def generate_suggestions(
        self,
        code: str,
        test_results: List[Dict],
        style_result: Dict,
        complexity_result: Dict,
        exercise_id: str
    ) -> List[Dict[str, str]]:
        """AI 기반 개선 제안 생성"""
        
        suggestions = []
        
        # 테스트 실패에 대한 힌트
        failed_tests = [t for t in test_results if not t['passed']]
        if failed_tests:
            hint = await self.generate_test_hint(code, failed_tests[0], exercise_id)
            suggestions.append({
                'type': 'test_hint',
                'title': '테스트 통과 힌트',
                'content': hint
            })
        
        # 스타일 개선 제안
        if style_result['score'] < 80:
            suggestions.append({
                'type': 'style',
                'title': '코드 스타일 개선',
                'content': self.get_style_improvement_tips(style_result['issues'])
            })
        
        # 복잡도 개선 제안
        if complexity_result['score'] < 70:
            suggestions.append({
                'type': 'complexity',
                'title': '코드 단순화',
                'content': '코드가 복잡합니다. 함수로 분리하거나 더 간단한 방법을 시도해보세요.'
            })
        
        # 모범 답안과 비교
        exemplar = await self.get_exemplar_solution(exercise_id)
        if exemplar and self.is_significantly_different(code, exemplar):
            suggestions.append({
                'type': 'alternative',
                'title': '다른 접근 방법',
                'content': '다른 방법으로도 해결할 수 있습니다. 힌트를 참고해보세요!'
            })
        
        return suggestions

class SandboxExecutor:
    """안전한 코드 실행 환경"""
    
    async def execute(
        self,
        code: str,
        input_data: str,
        language: str,
        timeout: float = 5.0
    ) -> Dict[str, Any]:
        if language == 'python':
            return await self._execute_python(code, input_data, timeout)
        # 다른 언어 지원
    
    async def _execute_python(
        self,
        code: str,
        input_data: str,
        timeout: float
    ) -> Dict[str, Any]:
        """Docker 컨테이너에서 Python 코드 실행"""
        
        import docker
        import time
        
        client = docker.from_env()
        
        # 안전한 실행 환경 설정
        container_config = {
            'image': 'python:3.9-slim',
            'command': ['python', '-c', code],
            'stdin_open': True,
            'detach': True,
            'mem_limit': '128m',
            'cpu_quota': 50000,  # CPU 사용량 제한
            'network_disabled': True,  # 네트워크 차단
            'read_only': True,
            'tmpfs': {'/tmp': 'size=10M,mode=1777'}  # 임시 쓰기 공간
        }
        
        try:
            container = client.containers.create(**container_config)
            container.start()
            
            # 입력 전달
            if input_data:
                container.attach_socket().send(input_data.encode())
            
            # 실행 시간 측정
            start_time = time.time()
            exit_code = container.wait(timeout=timeout)
            execution_time = time.time() - start_time
            
            # 출력 수집
            output = container.logs(stdout=True, stderr=False).decode()
            error = container.logs(stdout=False, stderr=True).decode()
            
            return {
                'output': output,
                'error': error if error else None,
                'exit_code': exit_code['StatusCode'],
                'execution_time': execution_time
            }
            
        except Exception as e:
            return {
                'output': '',
                'error': str(e),
                'exit_code': -1,
                'execution_time': timeout
            }
        finally:
            try:
                container.remove(force=True)
            except:
                pass
```

## 9. 모니터링 및 분석 시스템

### 9.1 학습 분석 대시보드
```python
# services/analytics.py
from datetime import datetime, timedelta
import pandas as pd
from typing import Dict, List, Any

class LearningAnalytics:
    def __init__(self, db_session):
        self.db = db_session
        
    async def generate_student_report(
        self,
        student_id: str,
        period: str = 'week'
    ) -> Dict[str, Any]:
        """학생 개인 학습 리포트 생성"""
        
        end_date = datetime.now()
        if period == 'week':
            start_date = end_date - timedelta(days=7)
        elif period == 'month':
            start_date = end_date - timedelta(days=30)
        
        # 학습 시간 통계
        study_time = await self.calculate_study_time(student_id, start_date, end_date)
        
        # 완료한 모듈
        completed_modules = await self.get_completed_modules(student_id, start_date, end_date)
        
        # 코드 제출 통계
        submission_stats = await self.analyze_submissions(student_id, start_date, end_date)
        
        # 실력 향상 추이
        skill_progress = await self.track_skill_progress(student_id, start_date, end_date)
        
        # 학습 패턴 분석
        learning_patterns = await self.analyze_learning_patterns(student_id)
        
        return {
            'student_id': student_id,
            'period': {
                'start': start_date.isoformat(),
                'end': end_date.isoformat()
            },
            'summary': {
                'total_study_time': study_time['total_minutes'],
                'daily_average': study_time['daily_average'],
                'modules_completed': len(completed_modules),
                'exercises_solved': submission_stats['total_solved'],
                'success_rate': submission_stats['success_rate']
            },
            'skill_progress': skill_progress,
            'learning_patterns': learning_patterns,
            'recommendations': await self.generate_recommendations(student_id, skill_progress)
        }
    
    async def analyze_learning_patterns(self, student_id: str) -> Dict[str, Any]:
        """학습 패턴 분석"""
        
        # 최근 30일 데이터
        sessions = await self.get_learning_sessions(student_id, days=30)
        
        df = pd.DataFrame(sessions)
        
        # 요일별 학습 패턴
        df['weekday'] = pd.to_datetime(df['timestamp']).dt.day_name()
        weekday_pattern = df.groupby('weekday')['duration'].mean().to_dict()
        
        # 시간대별 학습 패턴
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        hourly_pattern = df.groupby('hour')['duration'].mean().to_dict()
        
        # 가장 생산적인 시간대
        productive_hours = df.groupby('hour')['score'].mean().nlargest(3).index.tolist()
        
        # 학습 지속성
        consecutive_days = self.calculate_streak(df)
        
        return {
            'weekday_pattern': weekday_pattern,
            'hourly_pattern': hourly_pattern,
            'productive_hours': productive_hours,
            'current_streak': consecutive_days,
            'preferred_difficulty': self.analyze_difficulty_preference(df)
        }
    
    async def generate_teacher_dashboard(
        self,
        teacher_id: str,
        class_id: str
    ) -> Dict[str, Any]:
        """교사용 학급 전체 분석 대시보드"""
        
        students = await self.get_class_students(class_id)
        
        # 학급 전체 통계
        class_stats = {
            'total_students': len(students),
            'active_today': 0,
            'average_progress': 0,
            'struggling_students': [],
            'top_performers': []
        }
        
        student_data = []
        for student in students:
            progress = await self.get_student_progress(student['id'])
            student_data.append({
                'id': student['id'],
                'name': student['name'],
                'progress': progress['overall_progress'],
                'last_active': progress['last_active'],
                'current_module': progress['current_module'],
                'help_needed': progress['struggling_topics']
            })
            
            # 오늘 활동한 학생
            if progress['last_active'].date() == datetime.now().date():
                class_stats['active_today'] += 1
            
            # 도움 필요 학생
            if progress['overall_progress'] < 50:
                class_stats['struggling_students'].append(student['name'])
        
        # 평균 진도율
        class_stats['average_progress'] = sum(s['progress'] for s in student_data) / len(student_data)
        
        # 상위 수행자
        student_data.sort(key=lambda x: x['progress'], reverse=True)
        class_stats['top_performers'] = [s['name'] for s in student_data[:3]]
        
        # 주제별 이해도
        topic_mastery = await self.analyze_class_topic_mastery(class_id)
        
        return {
            'class_id': class_id,
            'timestamp': datetime.now().isoformat(),
            'class_stats': class_stats,
            'students': student_data,
            'topic_mastery': topic_mastery,
            'recommendations': self.generate_class_recommendations(topic_mastery)
        }
```

## 10. 성능 최적화 및 확장성

### 10.1 로드 밸런싱 및 캐싱
```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - api1
      - api2
      - api3
  
  api1:
    build: ./backend
    environment:
      - INSTANCE_ID=1
      - REDIS_URL=redis://redis:6379
      - DATABASE_URL=postgresql://user:pass@postgres:5432/codexkids
    depends_on:
      - redis
      - postgres
  
  api2:
    build: ./backend
    environment:
      - INSTANCE_ID=2
      - REDIS_URL=redis://redis:6379
      - DATABASE_URL=postgresql://user:pass@postgres:5432/codexkids
    depends_on:
      - redis
      - postgres
  
  api3:
    build: ./backend
    environment:
      - INSTANCE_ID=3
      - REDIS_URL=redis://redis:6379
      - DATABASE_URL=postgresql://user:pass@postgres:5432/codexkids
    depends_on:
      - redis
      - postgres
  
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
  
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: codexkids
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  code_executor:
    build: ./sandbox
    privileged: true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    deploy:
      replicas: 5

volumes:
  redis_data:
  postgres_data:
```

### 10.2 모니터링 설정
```python
# monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge
import time
from functools import wraps

# 메트릭 정의
request_count = Counter(
    'codexkids_requests_total',
    'Total requests',
    ['method', 'endpoint', 'status']
)

request_duration = Histogram(
    'codexkids_request_duration_seconds',
    'Request duration',
    ['method', 'endpoint']
)

active_users = Gauge(
    'codexkids_active_users',
    'Number of active users'
)

code_executions = Counter(
    'codexkids_code_executions_total',
    'Total code executions',
    ['language', 'status']
)

api_calls = Counter(
    'codexkids_api_calls_total',
    'External API calls',
    ['api_name', 'status']
)

def track_request_metrics(func):
    """API 엔드포인트 메트릭 추적 데코레이터"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = await func(*args, **kwargs)
            status = 'success'
        except Exception as e:
            status = 'error'
            raise
        finally:
            duration = time.time() - start_time
            
            # 메트릭 기록
            request_count.labels(
                method=kwargs.get('request').method,
                endpoint=func.__name__,
                status=status
            ).inc()
            
            request_duration.labels(
                method=kwargs.get('request').method,
                endpoint=func.__name__
            ).observe(duration)
        
        return result
    
    return wrapper

# Grafana 대시보드 설정
GRAFANA_DASHBOARD = {
    "dashboard": {
        "title": "Codex Kids Monitoring",
        "panels": [
            {
                "title": "Request Rate",
                "targets": [
                    {
                        "expr": "rate(codexkids_requests_total[5m])"
                    }
                ]
            },
            {
                "title": "Response Time",
                "targets": [
                    {
                        "expr": "histogram_quantile(0.95, codexkids_request_duration_seconds)"
                    }
                ]
            },
            {
                "title": "Active Users",
                "targets": [
                    {
                        "expr": "codexkids_active_users"
                    }
                ]
            },
            {
                "title": "Code Execution Success Rate",
                "targets": [
                    {
                        "expr": "rate(codexkids_code_executions_total{status='success'}[5m]) / rate(codexkids_code_executions_total[5m])"
                    }
                ]
            }
        ]
    }
}
```

## 11. 배포 및 CI/CD

### 11.1 GitHub Actions 워크플로우
```yaml
# .github/workflows/deploy.yml
name: Deploy Codex Kids

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r backend/requirements.txt
        pip install pytest pytest-asyncio pytest-cov
    
    - name: Run tests
      env:
        DATABASE_URL: postgresql://postgres:test@localhost/test
        REDIS_URL: redis://localhost:6379
      run: |
        pytest backend/tests --cov=backend --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
  
  build-and-deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker images
      run: |
        docker build -t codexkids/api:${{ github.sha }} ./backend
        docker build -t codexkids/frontend:${{ github.sha }} ./frontend
    
    - name: Push to registry
      env:
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
      run: |
        echo $DOCKER_PASSWORD | docker login -u codexkids --password-stdin
        docker push codexkids/api:${{ github.sha }}
        docker push codexkids/frontend:${{ github.sha }}
    
    - name: Deploy to Kubernetes
      env:
        KUBE_CONFIG: ${{ secrets.KUBE_CONFIG }}
      run: |
        echo "$KUBE_CONFIG" | base64 -d > kubeconfig
        export KUBECONFIG=kubeconfig
        
        kubectl set image deployment/api api=codexkids/api:${{ github.sha }}
        kubectl set image deployment/frontend frontend=codexkids/frontend:${{ github.sha }}
        
        kubectl rollout status deployment/api
        kubectl rollout status deployment/frontend
```

### 11.2 Kubernetes 배포 설정
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: codexkids-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: codexkids-api
  template:
    metadata:
      labels:
        app: codexkids-api
    spec:
      containers:
      - name: api
        image: codexkids/api:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: codexkids-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: codexkids-secrets
              key: redis-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5

---
apiVersion: v1
kind: Service
metadata:
  name: codexkids-api
spec:
  selector:
    app: codexkids-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: LoadBalancer

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: codexkids-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: codexkids-api
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

## 12. 보안 강화 조치

### 12.1 아동 개인정보 보호
```python
# security/child_protection.py
from cryptography.fernet import Fernet
import hashlib
from typing import Dict, Any
import re

class ChildDataProtection:
    def __init__(self, encryption_key: bytes):
        self.cipher = Fernet(encryption_key)
        self.pii_patterns = {
            'phone': re.compile(r'\d{3}-\d{4}-\d{4}'),
            'email': re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'),
            'address': re.compile(r'\d+\s+[\w\s]+(?:street|st|avenue|ave|road|rd|lane|ln)', re.I),
            'korean_rrn': re.compile(r'\d{6}-[1-4]\d{6}')  # 주민등록번호
        }
    
    def sanitize_user_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """민감한 개인정보 제거 또는 암호화"""
        sanitized = data.copy()
        
        # 필수 정보만 유지
        allowed_fields = ['username', 'age_group', 'school_grade', 'learning_preferences']
        
        # 불필요한 필드 제거
        for key in list(sanitized.keys()):
            if key not in allowed_fields:
                del sanitized[key]
        
        # 사용자명 검증 (실명 사용 금지)
        if 'username' in sanitized:
            if self._contains_real_name(sanitized['username']):
                sanitized['username'] = self._generate_safe_username()
        
        return sanitized
    
    def encrypt_sensitive_data(self, data: str) -> str:
        """민감한 데이터 암호화"""
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """암호화된 데이터 복호화"""
        return self.cipher.decrypt(encrypted_data.encode()).decode()
    
    def _contains_real_name(self, username: str) -> bool:
        """실명 포함 여부 검사"""
        # 한국 성씨 목록
        korean_surnames = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
        
        for surname in korean_surnames:
            if username.startswith(surname):
                return True
        
        # 영문 이름 패턴
        if re.match(r'^[A-Z][a-z]+\s+[A-Z][a-z]+$', username):
            return True
        
        return False
    
    def _generate_safe_username(self) -> str:
        """안전한 사용자명 생성"""
        import random
        
        adjectives = ['즐거운', '신나는', '멋진', '활발한', '똑똑한']
        nouns = ['코더', '탐험가', '개발자', '창작자', '발명가']
        
        return f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(100, 999)}"
    
    def audit_log_access(self, user_id: str, accessed_data: str, purpose: str):
        """데이터 접근 감사 로그"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': hashlib.sha256(user_id.encode()).hexdigest(),
            'data_type': accessed_data,
            'purpose': purpose,
            'ip_address': self._get_client_ip()
        }
        
        # 감사 로그 저장 (별도 보안 스토리지)
        self._store_audit_log(log_entry)
```

### 12.2 콘텐츠 필터링
```python
# security/content_filter.py
from typing import List, Dict, Tuple
import re

class ContentModerator:
    def __init__(self):
        self.load_filter_lists()
        
    def load_filter_lists(self):
        """부적절한 콘텐츠 필터 목록 로드"""
        self.inappropriate_words = set()  # 욕설, 비속어 등
        self.personal_info_patterns = []  # 개인정보 패턴
        self.suspicious_patterns = []     # 의심스러운 패턴
        
        # 실제 구현에서는 파일이나 DB에서 로드
        
    def moderate_content(
        self,
        content: str,
        content_type: str = 'text'
    ) -> Tuple[bool, List[str]]:
        """콘텐츠 검토"""
        issues = []
        
        # 텍스트 콘텐츠 검사
        if content_type == 'text':
            # 부적절한 언어 검사
            if self._contains_inappropriate_language(content):
                issues.append('inappropriate_language')
            
            # 개인정보 포함 검사
            if self._contains_personal_info(content):
                issues.append('personal_info')
            
            # 외부 링크 검사
            if self._contains_unsafe_links(content):
                issues.append('unsafe_links')
        
        # 코드 콘텐츠 검사
        elif content_type == 'code':
            if self._contains_malicious_code(content):
                issues.append('malicious_code')
        
        is_safe = len(issues) == 0
        return is_safe, issues
    
    def _contains_inappropriate_language(self, text: str) -> bool:
        """부적절한 언어 포함 여부 검사"""
        text_lower = text.lower()
        
        for word in self.inappropriate_words:
            if word in text_lower:
                return True
        
        return False
    
    def _contains_personal_info(self, text: str) -> bool:
        """개인정보 포함 여부 검사"""
        # 전화번호 패턴
        if re.search(r'\d{3}-\d{4}-\d{4}', text):
            return True
        
        # 이메일 패턴
        if re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text):
            return True
        
        # 주소 패턴
        if re.search(r'(시|구|동|로|길)\s*\d+', text):
            return True
        
        return False
    
    def _contains_unsafe_links(self, text: str) -> bool:
        """안전하지 않은 링크 포함 여부 검사"""
        # URL 추출
        urls = re.findall(r'https?://[^\s]+', text)
        
        safe_domains = [
            'codexkids.com',
            'github.com',
            'python.org',
            'wikipedia.org'
        ]
        
        for url in urls:
            domain = re.search(r'https?://([^/]+)', url)
            if domain:
                domain_name = domain.group(1).lower()
                if not any(safe in domain_name for safe in safe_domains):
                    return True
        
        return False
    
    def _contains_malicious_code(self, code: str) -> bool:
        """악성 코드 패턴 검사"""
        dangerous_patterns = [
            r'import\s+os',
            r'import\s+subprocess',
            r'import\s+socket',
            r'__import__',
            r'eval\s*\(',
            r'exec\s*\(',
            r'compile\s*\(',
            r'open\s*\([^)]*[\'"]w[\'"]',  # 파일 쓰기
            r'requests\.(?:get|post)',       # HTTP 요청
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                return True
        
        return False
```

## 13. 결론

이 통합 기술 상세 기획서는 Codex Kids 플랫폼의 전체적인 기술 구현 방안을 제시합니다. 주요 특징은 다음과 같습니다:

1. **교육 효과 극대화**: 시각적 학습 도구와 적응형 학습 시스템으로 개인별 맞춤 교육
2. **기술적 우수성**: 최신 웹 기술과 AI를 활용한 혁신적인 학습 경험
3. **안전성**: 철저한 보안과 개인정보 보호로 안전한 학습 환경 제공
4. **확장성**: 마이크로서비스 아키텍처와 클라우드 네이티브 설계로 성장 가능
5. **실용성**: Git 연동, 프로젝트 관리 등 실제 개발 환경과 유사한 경험 제공

이 플랫폼을 통해 아이들이 즐겁게 코딩을 배우면서도 미래의 데이터 과학자와 AI 전문가로 성장할 수 있는 튼튼한 기초를 다질 수 있을 것입니다.
