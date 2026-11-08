"""제목 — seeing-calculus

사용법: 이 파일을 단계 폴더로 복사한 뒤 main()만 고친다.
실행:   uv run python <경로>/<파일>.py
결과:   스크립트와 같은 폴더에 <파일이름>.png 저장
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 (Windows 기본 '맑은 고딕'), 마이너스 기호 깨짐 방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

OUT = Path(__file__).with_suffix(".png")


def main() -> None:
    # 예시: 사인 곡선 — 템플릿이 동작하는지 확인용
    x = np.linspace(0, 2 * np.pi, 400)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x, np.sin(x), label="sin x")
    ax.set_title("템플릿 확인: y = sin x")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.3)
    ax.legend()

    fig.tight_layout()
    fig.savefig(OUT, dpi=120)
    print(f"저장: {OUT}")
    plt.show()


if __name__ == "__main__":
    main()
