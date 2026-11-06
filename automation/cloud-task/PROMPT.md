<!-- Paste everything below this line into the cloud scheduled task's prompt. -->
Run today's answer-first daily deep research session in this repository.

1. Read `CLAUDE.md`, `docs/method.md` and **`docs/deep_run.md`**.
2. Execute `docs/deep_run.md` Phases 0–9 in order, as the **orchestrator**:
   delegate the work to the 5 subagents in `.claude/agents/` (miner, generator,
   verifier, prior-art-hunter, skeptic), and run verifier and prior-art-hunter
   in parallel. Keep their scoring blind to each other.
3. Budget: **140 minutes**. Use the whole budget. Don't stop at the first
   plausible question, and run round 2 if there's no consensus hit.
4. The goal is a question that is genuinely new. Anything already stated in
   OEIS, Wikipedia, MathWorld, papers or Prime Curios is not a hit.
5. Write every finding to the repo (all candidates including failures, all
   search logs, skeptic notes, scores, scripts, plus the log, leaderboard, pool
   and open-problem updates). Then commit and **push directly to `main`**
   (`git pull --rebase origin main && git push origin HEAD:main`). If main
   rejects the push, push to `claude/daily-<date>` and note it in the daily log.
6. Always commit and push, even on a MISS or a partial run
   (`daily: <A> — PARTIAL: <reason>`).

Success = a new folder in `discoveries/` and an updated `docs/daily_log.md` on
`main`, with three independent scores for every candidate that reached scoring.
