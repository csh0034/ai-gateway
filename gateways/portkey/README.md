# Portkey

가드레일·관측·라우팅을 한 게이트웨이로 묶는 OSS AI Gateway (2026.3 완전 OSS화).

## 강점

- **운영 안전성**: 가드레일, PII 리덕션, jailbreak 탐지, 감사로그가 게이트웨이 레이어에 내장.
- **모드 선택 자유**: Hosted (api.portkey.ai) 또는 Self-hosted 모두 지원.
- Python·TS 네이티브 SDK 모두 제공.

## 두 가지 사용 모드

| 모드 | 키 | 비고 |
|---|---|---|
| Hosted | `PORTKEY_API_KEY` + virtual key | 가장 간단. 회원가입 후 대시보드에서 virtual key 생성. |
| Self-hosted | `baseURL` 자체 endpoint + 게이트웨이 헤더 | OSS 컨테이너 띄우고 그쪽으로 트래픽. |

본 예제는 **Hosted 모드** 기준입니다.

## 설치 & 환경변수

### Python

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### TypeScript

```bash
cd typescript
npm install
cp .env.example .env
```

## 실행

- Python: `python chat.py`
- TypeScript: `npm start`

## 참고 링크

- 공식 문서: https://portkey.ai/docs
- GitHub (Gateway OSS): https://github.com/Portkey-AI/gateway
- Virtual Keys: https://portkey.ai/docs/product/ai-gateway/virtual-keys
