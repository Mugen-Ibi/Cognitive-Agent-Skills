# v1全面レビュー

[English](REVIEW.md)

レビュー日：2026-09-05
対象：repository構造、Skill動作、routing、環境互換性、配布、検証、documentation、保守性。

## 総合結論

中核思想は妥当でした。結果の重大性、可逆性、複雑性、不確実性、根拠の必要性から厳密さを選び、最初の問題設定を疑い、人間が判断できる大きさへ圧縮する設計は維持すべきです。一方、v1は認知protocolのprototypeとしては有効でも、現在のChat／Work／Plugin環境へ配布できる完成したpackageではありませんでした。

決定的な問題は、SkillとPluginを代替関係として扱っていたことです。現在のplatformでは、Skillがworkflowを実装し、Pluginがそれを配布します。v2は認知protocolをSkillとして維持し、skills-only Pluginで包みます。

## 指摘事項

| 重要度 | v1の問題 | 影響 | v2での対応 |
|---|---|---|---|
| 高 | Plugin manifestと導入可能なpackageがない | repositoryはPluginではなく、意図したChat／Work配布経路を持たない | 正規のPlugin rootに`.codex-plugin/plugin.json`を追加 |
| 高 | Routerが任意の兄弟Skill呼び出しに依存 | hostによって動作が変わり、fallback意味論も重複 | 単一Skill＋local referenceへ統合 |
| 高 | 決定的検証と行動evalがない | 構造・routing regressionを検出できない | validator、CI、評価case、合格基準を追加 |
| 中 | 4つの似たSkill descriptionがactive | 暗黙起動の競合とdiscovery metadata負荷 | activeな起動面を1つに削減 |
| 中 | protocol意味論が複数fileとfallbackに存在 | Routerと子protocolが乖離し得る | entrypointと各modeの正本referenceを一つに限定 |
| 中 | SkillのUI metadataがない | 発見・明示起動のUXが弱い | `agents/openai.yaml`を追加 |
| 中 | 導入説明が一般的なSkill対応を仮定 | Chat／Work／Plugin／CLI／desktop／IDEの差を説明できない | platform別architectureとmigration guideを追加 |
| 中 | 破壊的変更の扱いがない | 利用者が移行影響を予測できない | Plugin versionを`2.0.0`にし、changelogを追加 |
| 未決 | License未選択 | 外部再利用条件が不明 | owner判断として維持し、未決事項に明記 |

## 維持した強み

- 常に最大推論ではなく、必要十分な厳密さを選ぶ。
- 実行中にescalation／downgradeする。
- ユーザーの最初の問題設定を仮説として扱う。
- 発見、再定義、反証、検証、圧縮をmodelへ委譲する。
- 価値判断、risk受容、不可逆なcommitmentを人間に残す。
- High Precisionではchain-of-thoughtを公開せず、監査可能な根拠区分を示す。
- mixed modeの移行にreadiness gateを設け、初期の発想を未検証のまま最終成果物として扱わない。

## 主要なprotocol変更

- Routerは点数計算より先に重大なoverride条件を判定します。
- 単純な実行作業には暗黙起動しない境界をdescriptionへ追加しました。
- 初期状態では一つのmodeだけを読み、分離可能な構成要素だけmixed modeを許可します。
- Evidence disciplineを条件付きreferenceとして分離し、直接検査・一次資料・検証停止条件を明示しました。
- High Precisionにdecision-ready gateを追加し、厳密さと出力量を分離しました。

## 残る不確実性

- 暗黙起動の品質はmodelとhostに依存し、repository validationだけでは証明できません。
- Public Plugin Directoryへの受理にはplatform側の提出・reviewが必要です。
- 製品面の対応状況は変化し得るため、公開前にOpenAI公式documentationを再確認する必要があります。
- 行動evalはbaselineです。推測で増やすのではなく、実利用で観測した失敗から拡張すべきです。

## 推奨

v2をmain architectureとして採用します。各modeを個別Skill chipとして選びたいという実測上の需要が、起動競合と意味論の乖離riskを上回らない限り、3つの子Skillをactiveな兄弟Skillとして復活させるべきではありません。必要になった場合は、protocol本文を複製せず、明示起動専用の薄いadapterとして追加するのが妥当です。
