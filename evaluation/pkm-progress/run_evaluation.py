#!/usr/bin/env python3
"""Collect reproducible PKM prototype evidence and create an Indonesian PDF.

All outputs are aggregate/hash-only. Put device JSONL evidence under
``private/`` (ignored by Git) and run the component validator before sharing a
report. This runner never uploads browsing or participant data.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pdf_report import write_a4_pdf


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "output"
TARGETS = json.loads((HERE / "targets.json").read_text(encoding="utf-8"))


def command_result(name: str, command: list[str], cwd: Path, timeout: int = 240) -> dict[str, Any]:
    started = time.monotonic()
    environment = os.environ.copy()
    environment.setdefault("GOCACHE", "/tmp/gamblock-go-cache")
    try:
        completed = subprocess.run(command, cwd=cwd, env=environment, text=True, capture_output=True, timeout=timeout, check=False)
        output = (completed.stdout + "\n" + completed.stderr).strip()
        result = {
            "name": name,
            "status": "passed" if completed.returncode == 0 else "failed",
            "return_code": completed.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "command": command,
            "working_directory": str(cwd.relative_to(ROOT)),
            "output_sha256": __import__("hashlib").sha256(output.encode()).hexdigest(),
        }
        if completed.returncode != 0 and "Read-only file system" in output:
            result["status"] = "blocked_environment"
            result["reason"] = "Flutter SDK cache is read-only in this workspace; the test process could not start."
        return result
    except subprocess.TimeoutExpired as error:
        output = ((error.stdout or "") + "\n" + (error.stderr or "")).strip()
        return {
            "name": name, "status": "failed", "return_code": None,
            "duration_seconds": round(time.monotonic() - started, 3), "command": command,
            "working_directory": str(cwd.relative_to(ROOT)),
            "output_sha256": __import__("hashlib").sha256(output.encode()).hexdigest(),
            "reason": f"timeout after {timeout} seconds",
        }


def skipped(name: str, reason: str) -> dict[str, Any]:
    return {"name": name, "status": "pending", "reason": reason}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def detection_checks(metrics: dict[str, Any]) -> dict[str, bool]:
    detection = TARGETS["detection"]
    return {
        "accuracy": metrics["accuracy"] >= detection["accuracy_min"],
        "precision": metrics["precision"] >= detection["precision_min"],
        "recall": metrics["recall"] >= detection["recall_min"],
        "f1_score": metrics["f1_score"] >= detection["f1_score_min"],
        "false_positive_rate": metrics["false_positive_rate"] <= detection["false_positive_rate_max"],
    }


def run_component_tests(enabled: bool, include_flutter: bool) -> list[dict[str, Any]]:
    if not enabled:
        return [skipped("code_tests", "Not requested; run with --run-code-tests.")]
    results = [
        command_result("model_evidence_unit", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], ROOT / "gamblock-ai-model"),
        command_result("runtime_projection_unit", [sys.executable, "-m", "unittest", "discover", "-s", str(HERE), "-p", "test_runtime_projection.py"], ROOT),
        command_result("extension_passive_sensor_unit", ["npm", "test"], ROOT / "browser_extension"),
        command_result("website_recovery_accountability_unit", ["npm", "test", "--", "hooks/use-approval.test.tsx", "hooks/use-accountability.test.tsx", "lib/recovery/runtime.test.ts"], ROOT / "gamblock-ai-website"),
        command_result("backend_approval_grant_recovery_unit", ["go", "test", "./internal/service", "-run", "Test(ProtectionGrantSigner_SignsDeviceBoundES256Grant|Accountability_CreateApprovalRequestAndResolve|Admin_EmergencyKeyGenerateAndValidate|ReflectionService)"], ROOT / "gamblock-ai-backend"),
        command_result("client_python_contract_unit", [sys.executable, "-m", "unittest", "discover", "-s", "test/scripts", "-p", "*test.py"], ROOT / "gamblock_ai_apps"),
    ]
    if include_flutter:
        results.append(command_result("flutter_pattern_interrupt_unit", ["flutter", "test", "test/features/pattern_interrupt/pattern_interrupt_screen_test.dart"], ROOT / "gamblock_ai_apps"))
    else:
        results.append(skipped("flutter_pattern_interrupt_unit", "Run with --include-flutter on a writable Flutter SDK installation."))
    results.append(skipped("android_instrumented_runtime", "Requires a connected Android device and an explicitly approved device test run."))
    results.append(skipped("windows_service_runtime", "Requires a Windows VM/device; not executable on this Linux workspace."))
    return results


def device_evidence() -> dict[str, Any]:
    files = sorted((HERE / "private").glob("*.jsonl")) if (HERE / "private").exists() else []
    if not files:
        return {
            "status": "pending",
            "reason": "No local Phase 4 JSONL export is present. Legacy Android documentation is not treated as raw reproducible evidence.",
            "legacy_documented_android": {"successful_samples": 31, "median_ms": 115.57, "p95_ms": 142.85, "raw_export_available": False},
        }
    report_path = OUTPUT / "phase4_latency.json"
    result = command_result("phase4_latency_gate", [sys.executable, "scripts/phase4_latency_report.py", *[str(path) for path in files], "--output", str(report_path)], ROOT / "gamblock_ai_apps")
    result["evidence_files"] = len(files)
    if report_path.exists():
        result["report"] = load_json(report_path)
    return result


def as_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def pdf_lines(report: dict[str, Any]) -> list[str]:
    model = report["model_evidence"]
    projection = report["runtime_projection"]
    model_metrics = model["evaluation"]["all_test_rows"]
    deployed = projection["evaluation"]["deployed_hybrid"]
    dataset = model["dataset"]
    lines = [
        "RINGKASAN PENGUJIAN KEMAJUAN GAMBLOCK-AI",
        f"Dibuat otomatis: {report['generated_at']}",
        "Dokumen ini memperbarui ringkasan pengujian kemajuan dengan bukti agregat/hash-only yang dapat direproduksi.",
        "",
        "1. Status klaim dan metode",
        "Evaluasi model memakai snapshot prediksi model dan replay offline jalur extension -> payload terbatas -> Hybrid-v2 Windows. Replay tidak mengklaim browser, service Windows, aksi Back, maupun Pattern Interrupt sudah terverifikasi di perangkat fisik.",
        f"Maturitas bukti model snapshot: {model['evidence_maturity']}; audit dataset: {'lulus' if model['audit']['passed'] else 'belum lengkap'}.",
        f"Maturitas proyeksi deployment: {projection['evidence_maturity']}; fixture kontrak: {projection['fixture_contract']['passed']}/{projection['fixture_contract']['samples']} lulus.",
        "",
        "2. Jumlah dan pembagian dataset dari codebase",
        f"Data mentah: {dataset['raw']['total_rows']:,} baris (judi {dataset['raw']['judi_rows']:,}; non-judi {dataset['raw']['non_judi_rows']:,}).",
        f"Set bersih: {dataset['clean']['rows']:,} baris. Train: {dataset['train']['rows']:,} (judi {dataset['train']['label_counts'].get('1', 0):,}; non-judi {dataset['train']['label_counts'].get('0', 0):,}).",
        f"Test final: {dataset['test']['rows']:,} (judi {dataset['test']['label_counts'].get('1', 0):,}; non-judi {dataset['test']['label_counts'].get('0', 0):,}).",
        f"Validasi tuning tercatat: {dataset['validation_during_tuning']['rows']:,} baris (judi 670; non-judi 1.404); model final kemudian difit ulang pada seluruh train.",
        f"Kebocoran: ID train/test {dataset['train_test_id_overlap_count']}; URL sama {dataset['train_test_url_overlap_count']}; hostname persis sama {dataset['train_test_exact_host_overlap_count']}. Baris mentah tanpa jejak clean: {dataset['lineage_gap_rows']}.",
        "",
        "3. Tabel 4.4 - target dan capaian pengujian klasifikasi",
        "Metrik | Target | Snapshot prediksi penuh (historis) | Proyeksi deployment extension/Windows aktif | Status proyeksi",
    ]
    names = [("Akurasi", "accuracy", "accuracy_min"), ("Presisi", "precision", "precision_min"), ("Recall", "recall", "recall_min"), ("F1-score", "f1_score", "f1_score_min")]
    for label, metric, target in names:
        lines.append(f"{label} | >= {as_pct(TARGETS['detection'][target])} | {as_pct(model_metrics[metric])} | {as_pct(deployed[metric])} | {'LULUS' if report['deployment_target_checks'][metric] else 'BELUM LULUS'}")
    lines.append(f"False Positive Rate | <= {as_pct(TARGETS['detection']['false_positive_rate_max'])} | {as_pct(model_metrics['false_positive_rate'])} | {as_pct(deployed['false_positive_rate'])} | {'LULUS' if report['deployment_target_checks']['false_positive_rate'] else 'BELUM LULUS'}")
    confusion = deployed['confusion_matrix']
    lines.append(f"Konfusi deployment: TP {confusion['tp']}, TN {confusion['tn']}, FP {confusion['fp']}, FN {confusion['fn']}; 2.592 HTML test diproyeksikan. Set tanpa hostname overlap: {projection['evaluation']['exact_host_isolated_deployed_hybrid']['samples']}.")
    lines.extend([
        "",
        "4. Performa, platform, dan Pattern Interrupt",
        "Artefak ONNX: %.3f MiB; batas < 5 MiB: %s." % (model['artifacts']['onnx']['mib'], 'lulus' if model['artifacts']['onnx']['under_5_mib'] else 'belum lulus'),
        "Kontrak Pattern Interrupt dikodekan pada Android, Flutter, dan Windows: 7 detik (rentang target 5-10 detik).",
        "Gate latensi: p95 input-ke-intervensi harus < 200 ms, sedikitnya 30 sampel sukses per grup platform/perangkat/skenario/browser/build, tanpa kegagalan blok/visibility.",
        f"Bukti perangkat saat ini: {report['device_evidence']['status']}. {report['device_evidence'].get('reason', '')}",
        "Dokumentasi Android terdahulu melaporkan 31 sampel, median 115,57 ms, p95 142,85 ms, tetapi ekspor JSONL mentah tidak tersedia sehingga tidak dipromosikan menjadi bukti reproduktif.",
        "Windows/browser physical trace: pending.",
        "",
        "5. Pengujian kode yang dieksekusi",
    ])
    for test in report['code_tests']:
        detail = test.get('reason', f"durasi {test.get('duration_seconds', 0)} dtk")
        lines.append(f"- {test['name']}: {test['status'].upper()} ({detail})")
    lines.extend([
        "",
        "6. Batasan yang wajib dicantumkan dalam laporan",
        (
            "Proyeksi deployment artefak aktif lulus seluruh target numerik. Ini tetap bukti replay offline dan bukan klaim bahwa runtime browser/Windows telah tervalidasi di perangkat fisik."
            if report["deployment_target_passed"]
            else "Proyeksi deployment belum lulus seluruh target numerik; jangan mengklaim target sistem deployment tercapai."
        ),
        "Dataset card belum memiliki sumber, tanggal koleksi, lisensi/legal basis, dan governance pelabelan. Split bukan group-by-domain final dan memiliki dua hostname yang sama antara train/test.",
        "Tidak ada URL mentah, DOM mentah, screenshot, riwayat browsing, atau data partisipan dalam artefak JSON/PDF ini.",
        "",
        "Lokasi penyimpanan yang dipilih",
        "Harness lintas-repositori disimpan di umbrella evaluation/pkm-progress karena menggabungkan model, extension, client, backend, dan website. Kontrak/runtime evidence tetap berada di gamblock_ai_apps; audit data/artifak tetap di gamblock-ai-model. Tidak diperlukan submodule baru.",
    ])
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT)
    parser.add_argument("--run-code-tests", action="store_true")
    parser.add_argument("--include-flutter", action="store_true")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    model_path = output / "model_evidence.json"
    projection_path = output / "runtime_projection.json"
    model_command = command_result("model_evidence", [sys.executable, "scripts/evaluate_model_evidence.py", "--output", str(model_path)], ROOT / "gamblock-ai-model")
    projection_command = command_result("runtime_projection", [sys.executable, str(HERE / "runtime_projection.py"), "--output", str(projection_path)], ROOT, timeout=360)
    if model_command["status"] != "passed" or projection_command["status"] != "passed":
        raise SystemExit("Cannot create summary: model evidence or runtime projection did not complete.")
    model = load_json(model_path)
    projection = load_json(projection_path)
    deployment_checks = detection_checks(projection["evaluation"]["deployed_hybrid"])
    report = {
        "schema_version": 1,
        "report_kind": "gamblock_pkm_progress_evidence",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "targets": TARGETS,
        "model_evidence_command": model_command,
        "runtime_projection_command": projection_command,
        "model_evidence": model,
        "runtime_projection": projection,
        "deployment_target_checks": deployment_checks,
        "deployment_target_passed": all(deployment_checks.values()),
        "code_tests": run_component_tests(args.run_code_tests, args.include_flutter),
        "device_evidence": device_evidence(),
        "privacy": {"raw_url_or_dom_emitted": False, "participant_data_emitted": False},
    }
    json_path = output / "evidence.json"
    pdf_path = output / "ringkasan-pengujian-kemajuan.pdf"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_a4_pdf(pdf_path, pdf_lines(report))
    print(json.dumps({"json": str(json_path), "pdf": str(pdf_path), "deployment_target_passed": report["deployment_target_passed"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
