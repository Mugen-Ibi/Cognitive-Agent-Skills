# Cognitive Agent Skills

[English](README.md)

複数の選択肢や問題設定の不確かさを、行動に移せる判断へ整理するSkillです。ユーザーの判断負担を減らし、実行を依頼された場合は、許可された範囲で成果物の完成まで進めます。

v3では固定された思考手順を廃止し、成果・判断基準・完了条件を中心にしました。Lite／Standard／High Precisionは残しますが、モデルや推論エフォートの設定を変更する機能ではありません。

| 深度 | 用途 |
|---|---|
| Lite | 容易にやり直せる選択。通常は追加資料を読まず回答 |
| Standard | 複数の制約やトレードオフがある判断 |
| High Precision | 重大な影響、変更の難しさ、監査可能性が求められる判断 |

単純な編集や説明では自動起動を求めません。明示的に「Cognitive Routerで比較して」「High Precisionで研究方法を監査して」と依頼できます。レビューの依頼だけで実装権限を広げることはありません。

## 構成

- `.agents/plugins/marketplace.json`：マーケットプレイス定義
- `plugins/cognitive-agent-skills/.codex-plugin/plugin.json`：Plugin定義
- `plugins/cognitive-agent-skills/skills/cognitive-router/`：Skillと必要時に読む参照資料
- `evals/cases.json`：行動評価ケース
- `scripts/validate.py`：パッケージ整合性検証

既存の導入先は `Mugen-Ibi/Cognitive-Agent-Skills` です。利用環境ごとの導入手順・対応状況は公開前に公式資料と実機で確認してください。リポジトリの更新だけでは導入済みSkillは更新されません。

## 検証

```bash
python3 scripts/validate.py
```

この検証は構造の整合性を確認します。判断品質の向上を証明するものではありません。

[設計](docs/ARCHITECTURE.md)・[評価方法](docs/EVALUATION.md)・[移行](docs/MIGRATION.md)・[検証結果](docs/VALIDATION-REPORT.md)

バージョン：`3.0.0`。ライセンス：[Apache-2.0](LICENSE)。
