# Lab 6 — Path Comparison

## 1. Benchmark Results

| Path | Correct | Abstain OK | p50 ms | Max ms |
|---|---:|---:|---:|---:|
| deterministic | 9/25 | 7/7 | 0.0 | 0.6 |
| retrieval | 21/25 | 6/7 | 0.0 | 0.0 |
| llm (stub) | 21/25 | 6/7 | 0.1 | 2.3 |

## 2. Analysis

The retrieval and LLM (stub) paths achieved 21/25 correct answers (84%), outperforming the deterministic path, which achieved 9/25.

After fixing the intent router, question E23 was correctly routed to the knowledge base instead of the fee calculator. The assistant now answers the tuition rate question with 450,000 VND per credit from source F26#1.

The remaining retrieval and LLM failures are E13, E14, E15, and E19. The abstain score is 6/7, meaning one expected refusal case is still not handled correctly.

## 3. Next Improvement

I would investigate E19 first because it is a remaining failure shared by the retrieval and LLM paths. I would also review the refusal behavior to improve the abstain score from 6/7 to 7/7.