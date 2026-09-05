# Cognitive Agent Skills

[English](README.md)

誤ったときのコストに応じて分析の厳密さを調整する、Human–AI認知システムです。

Version 2では、正本となる単一の`cognitive-router` Skillをskills-only Pluginとして配布します。SkillはLite／Standard／High Precisionを選択し、選択したプロトコルだけを読み込み、人間が判断できる大きさに圧縮した結果を返します。これは従来の4 Skill間ディスパッチ構成を置き換える破壊的変更です。

## なぜSkillとPluginを組み合わせるのか

- **Skillが実装本体です。** `SKILL.md`とreferencesが認知ワークフローを定義します。
- **Pluginが配布境界です。** 対応するChatGPT Chat／Work／Codex環境へ、一つの単位として導入・共有できます。
- **単一の適応型Skillが競合を防ぎます。** 兄弟Skill呼び出しへの依存をなくし、暗黙起動の競合とメタデータの常駐コストを減らします。
- **Skill単体でも移植できます。** Codex CLI／IDEでは、Plugin内の`cognitive-router`ディレクトリをstandalone Skillとして利用できます。

外部サービスを必要としないため、MCP serverは同梱していません。ホスト環境で利用可能なツールや根拠を使い、新しい認証・運用境界を増やさない設計です。

## 3つのモード

| モード | 適した用途 | 基本動作 |
|---|---|---|
| Lite | 低コストでやり直しやすい質問・発想 | 短い再定義と健全性確認 |
| Standard | 複数ステップと実質的なトレードオフ | 探索、反証、検証、実行、監査 |
| High Precision | 重大・不可逆・出版・ガバナンス用途 | 根拠マップ、独立再定義、敵対的レビュー、独立監査 |

Routerは一つの依頼の分離可能な部分に別々のモードを適用でき、実際のリスクが判明した時点でエスカレーション／ダウングレードします。

## リポジトリ構造

```text
plugins/cognitive-agent-skills/
├── .codex-plugin/plugin.json
└── skills/cognitive-router/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── routing.md
        ├── lite.md
        ├── standard.md
        ├── high-precision.md
        └── evidence.md
docs/
├── ARCHITECTURE.md
├── EVALUATION.md
├── MIGRATION.md
├── RELEASE.md
├── REVIEW.md
└── VALIDATION-REPORT.md
evals/cases.json
scripts/validate.py
```

## 使い方

Pluginを導入後、通常どおり依頼するか、同梱Skillを明示的に指定します。

```text
Cognitive Routerを使って、この移行計画を評価し、適切な進め方を提案してください。
```

必要な厳密さが分かっている場合は、モードを指定できます。

```text
Cognitive RouterをHigh Precisionモードで使い、この投稿予定の研究方法を監査してください。
```

通常の出力は、結論、根拠、前提、トレードオフ、不確実性、次の行動を示します。内部のchain-of-thoughtは出力しません。

## ローカル開発での導入

リポジトリをcloneし、対応するローカルmarketplaceまたはPlugin開発フローで`plugins/cognitive-agent-skills`をPlugin rootとして指定します。

Codexでstandalone Skillとして利用する場合は、次のディレクトリをユーザーまたはrepository scopeのSkillsディレクトリへコピーまたはリンクします。

```text
plugins/cognitive-agent-skills/skills/cognitive-router
```

standalone SkillとPluginでは対応する製品面が異なります。配布前に[アーキテクチャ](docs/ARCHITECTURE.md)と最新のOpenAI公式ドキュメントを確認してください。

## 検証

```bash
python3 scripts/validate.py
```

Plugin manifest、Skill frontmatter、UI metadata、内部リンク、protocol一覧、評価ケースのschema、廃止したv1構造を検査します。CIでも同じcommandを実行します。

行動評価用ケースと手動手順は[評価ガイド](docs/EVALUATION.md)にあります。

v1の全指摘と対応状況は[全面レビュー](docs/REVIEW.ja.md)にあります。

実行した検証、forward test、修正内容、残る制約は[検証report](docs/VALIDATION-REPORT.md)にあります。

## v1からの移行

Version 2は、package構造と呼び出し方法を変更します。個別の`cognitive-lite`、`cognitive-standard`、`cognitive-high-precision`は、`cognitive-router`が選択するprotocol referenceへ統合されました。詳しくは[移行ガイド](docs/MIGRATION.md)を参照してください。

## 状態とライセンス

Plugin manifestのversionは`2.0.0`です。ライセンスは未選択で、著作権はrepository ownerに帰属します。外部再配布や、明示的な利用条件を必要とするcontribution受け入れの前にライセンスを選択・追加してください。
