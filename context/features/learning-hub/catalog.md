# Learning Hub Content Manifest

Status: `implemented baseline and CMS workflow`; editorial review remains operational

Owner: website/backend content and admin CMS

Review policy: verify every outbound URL and cost/certificate label before
publication; re-review at least every 180 days

The 22-program baseline was cross-checked on 2026-08-02 against the official
UTY program list at `https://uty.ac.id/`. The corrected direct OpenLearn
bookkeeping, psychology, adolescent-mental-health, teacher-development, and
reflective-practice sources were checked against the provider's official
course pages on the same date. The seed records that frozen date instead of
pretending every future seed execution is a new editorial review.

## Taxonomy baseline

### Clusters

1. `computing-data` — software, information systems, health informatics,
   computer engineering, data science, and digital education.
2. `engineering-built-environment` — architecture, civil, electrical,
   industrial engineering, spatial planning, and built-environment tools.
3. `business-finance-tourism` — accounting, management, entrepreneurship,
   finance, and destination tourism.
4. `psychology-education` — psychology, counseling, educational practice,
   English education, and educational technology.
5. `communication-language-global` — communication, English/language,
   international relations, media, and public-facing work.

### UTY program mapping

| Slug                                 | Program                           | Primary cluster               |
| ------------------------------------ | --------------------------------- | ----------------------------- |
| `uty-d3-sistem-informasi`            | D3 Sistem Informasi               | computing-data                |
| `uty-arsitektur`                     | S1 Arsitektur                     | engineering-built-environment |
| `uty-teknik-sipil`                   | S1 Teknik Sipil                   | engineering-built-environment |
| `uty-informatika`                    | S1 Informatika                    | computing-data                |
| `uty-informatika-medis`              | S1 Informatika Medis              | computing-data                |
| `uty-sistem-informasi`               | S1 Sistem Informasi               | computing-data                |
| `uty-teknik-komputer`                | S1 Teknik Komputer                | computing-data                |
| `uty-teknik-elektro`                 | S1 Teknik Elektro                 | engineering-built-environment |
| `uty-teknik-industri`                | S1 Teknik Industri                | engineering-built-environment |
| `uty-sains-data`                     | S1 Sains Data                     | computing-data                |
| `uty-pwk`                            | S1 Perencanaan Wilayah dan Kota   | engineering-built-environment |
| `uty-d3-akuntansi`                   | D3 Akuntansi                      | business-finance-tourism      |
| `uty-ilmu-komunikasi`                | S1 Ilmu Komunikasi                | communication-language-global |
| `uty-pendidikan-bahasa-inggris`      | S1 Pendidikan Bahasa Inggris      | psychology-education          |
| `uty-pendidikan-teknologi-informasi` | S1 Pendidikan Teknologi Informasi | psychology-education          |
| `uty-bimbingan-konseling`            | S1 Bimbingan dan Konseling        | psychology-education          |
| `uty-manajemen`                      | S1 Manajemen                      | business-finance-tourism      |
| `uty-psikologi`                      | S1 Psikologi                      | psychology-education          |
| `uty-sastra-inggris`                 | S1 Sastra Inggris                 | communication-language-global |
| `uty-s1-akuntansi`                   | S1 Akuntansi                      | business-finance-tourism      |
| `uty-ilmu-hubungan-internasional`    | S1 Ilmu Hubungan Internasional    | communication-language-global |
| `uty-destinasi-pariwisata`           | D4 Destinasi Pariwisata           | business-finance-tourism      |

Cross-tags are allowed for adjacent fields. Every program also receives the
universal skills tag.

## Seed composition

The first published baseline contains:

- 35 catalog items: four courses, one certification, one toolkit, and one
  career snapshot per cluster;
- 5 learning paths, one per cluster;
- 10 mini-projects, two per cluster;
- bilingual Indonesian/English metadata;
- no time-bound opportunity until an administrator provides a verified expiry
  date.

The five learning paths are:

- `computing-data-path`;
- `engineering-built-environment-path`;
- `business-finance-tourism-path`;
- `psychology-education-path`;
- `communication-language-global-path`.

Each path contains two source resources and one mini-project as a short
starter sequence. The same cluster exposes its career snapshot and toolkit as
separate cards.

## Source families

The editorial seed should prefer specific official course pages, not generic
platform homepages. Candidate source families include Microsoft Learn, Cisco
Networking Academy, Autodesk Learning, QGIS Documentation, British Council
LearnEnglish, HubSpot Academy, OpenLearn, HP LIFE, Dicoding, and Google
Skillshop. Cost and certificate claims are recorded separately and never
inferred from the provider name.

`duration_minutes` is the suggested first-session budget used by the local
time filter, not a claim about total provider course duration. Certification
items distinguish free learning material from an examination that may have a
separate fee.
