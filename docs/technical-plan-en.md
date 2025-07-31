# Codex Kids - Technical Plan (English Summary)

This document summarizes the key points of `code-kids-technical-plan.md` to help English-speaking contributors understand the project.

## 1. Project Overview

Codex Kids is a visual coding education platform aimed at children ages 10-15. It provides step-by-step lessons with diagrams and visual aids to explain coding concepts. The goal is to build a strong foundation for future studies in data science and AI while maintaining a safe learning environment.

### Core Values
- **Visual Learning**: Understand abstract concepts through graphics.
- **Progressive Growth**: Personalized learning paths based on level.
- **Future Ready**: Bridges to data science and AI topics.
- **Safety**: Protects children's data and provides a secure environment.

## 2. Architecture

The system uses modern web technologies with a focus on scalability and maintainability.

### Frontend
- Built with **Vue.js 3** and **Nuxt.js** for server-side rendering and SEO.
- Uses TypeScript, TailwindCSS, and Pinia for state management.
- Provides a Monaco-based code editor with beginner-friendly features and live analysis.

### Backend
- Implemented with **FastAPI**.
- Manages resources like Redis and PostgreSQL via async context managers.
- Provides services such as code analysis, visualization, AI tutoring, and project management.

## 3. Key Features

1. **Interactive Code Editor**: Real-time feedback and visualizations help learners understand code behavior.
2. **Adaptive Learning**: Exercises and tutorials adjust to the user's skill level.
3. **Gamified Progression**: Challenges, badges, and projects encourage continued learning.
4. **Safety and Moderation**: Content filters and secure project sandboxing ensure a safe environment.
5. **Scalability**: Microservice-friendly design and cloud-native deployment support growth.

## 4. Conclusion

Codex Kids combines visual tools, modern web tech, and AI-powered guidance to create an engaging coding platform for young learners.
