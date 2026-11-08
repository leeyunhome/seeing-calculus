# seeing-calculus

스티븐 스트로가츠의 『Infinite Powers』(한국어판 『무한의 힘』)를 읽고,
목차 순서대로 미적분의 핵심 개념을 여러 프로그래밍 언어로 시각화하는 개인 학습 프로젝트입니다.

- 진행 계획: [PLAN.md](PLAN.md)
- 사용 언어: Python, JavaScript(p5.js · D3 · Three.js · WebAudio), C, C++, C#, GLSL

## 실행 방법

```bash
uv sync                                   # 처음 한 번: Python 3.12 + numpy, matplotlib 설치
uv run python ch01_infinity/.../xxx.py    # Python 예제 (결과 png는 같은 폴더에 저장)
```

- `.html` 예제: 브라우저로 파일을 열면 바로 실행됩니다 (p5.js 등은 CDN에서 불러옴).
- 새 단계는 [templates/](templates/)의 템플릿을 복사해서 시작합니다.

## 고지

이 저장소는 책을 읽은 독자의 개인 학습 기록이며, 저자 및 출판사와 무관합니다.
책의 본문·그림은 포함하지 않으며, 모든 코드와 그림은 직접 작성한 것입니다.
책 내용이 궁금하다면 정식 출간본을 참고해 주세요.

## 라이선스

[MIT](LICENSE)
