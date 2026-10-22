# ucl-pipeline

Walk-forward Poisson football predictor for league and UEFA fixtures.

V0 is the production model. `python3 -m ucl_pipeline predict` is the Telegram path.

V1 is a regularised Poisson model. Decay 0.0015 and L2 4 are frozen from the 2024–25 validation and are not retuned on 2025–26. V1 shadow runs do not send Telegram. See `docs/v1_run.md`.
