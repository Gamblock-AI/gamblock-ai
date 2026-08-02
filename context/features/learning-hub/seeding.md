# Learning Hub Seeder Contract

Status: `implemented`

Scope: public baseline content only

## Production behavior

`SeedProductionDefaults` calls `SeedLearningHubDefaults` after schema migration.
The production path must not call `SeedUsers`, create demo activity, or create
student progress/EXP.

The production path calls only public education/social defaults and the
Learning Hub seed; demo users and activity remain development-only.

## Idempotency rules

- Use immutable stable IDs/slugs for clusters, programs, items, and paths.
- Insert only missing records.
- Never overwrite an existing administrator-managed record.
- Never delete seed records during rerun.
- Create seed revisions only when the item is absent.
- Execute the complete baseline transactionally.
- Use the frozen source-review date from the curated baseline; never replace it
  with the date on which a deployment happens to run the seed.
- The dedicated `seed-learning-hub` command logs only aggregate inserted and
  skipped counts; it never logs item titles, URLs, users, or progress.

## Baseline counts

- 5 clusters;
- 22 UTY programs;
- 35 catalog items;
- 5 paths;
- 10 mini-projects.

Development-only seed commands may create demo users and demo activity, but
they must remain separate from production defaults.
