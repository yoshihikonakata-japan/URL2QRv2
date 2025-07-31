#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL2QRv2: Batch QR-code generator for URLs.
Outputs vector QR codes in .svg, .eps, and .ai formats at a fixed size of 413×413 pixels.

Dependencies:
    pip install segno reportlab

Usage:
    python URL2QRv2.py [-i input_file] [-o output_dir] [-e error_level]
"""

import argparse
import logging
import math
from pathlib import Path

import segno

# デフォルトの入出力パスを定義
INPUT_FILE = Path(r"C:\pyQR\URL_List_v2\URL_List.txt")
OUTPUT_DIR = Path(r"C:\pyQR\QR_generate_v2")
# 出力サイズとフォーマット
SIZE = 413  # 画像サイズ (ピクセル)
FORMATS = ['svg', 'eps', 'ai']


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch-generate vector QR codes (.svg, .eps, .ai) from URLs."
    )
    parser.add_argument(
        "-i", "--input", type=Path,
        default=INPUT_FILE,
        help="Input text file with one URL per line."
    )
    parser.add_argument(
        "-o", "--output", type=Path,
        default=OUTPUT_DIR,
        help="Directory to save generated QR code files."
    )
    parser.add_argument(
        "-e", "--error-level", choices=["l", "m", "q", "h"],
        default="m",
        help="QR code error correction level."
    )
    return parser.parse_args()


def extract_code(url: str, length: int = 4) -> str:
    """
    URLの末尾から指定文字数を切り出してファイル名のベースとする。
    """
    cleaned = url.rstrip("/#!")
    return cleaned[-length:].upper()


def generate_qr_images(
    url: str,
    size: int,
    error_level: str,
    output_dir: Path,
) -> None:
    code = extract_code(url)
    qr = segno.make_qr(url, error=error_level)

    # 枠付きモジュール数を元にスケールを計算
    border = 4
    module_count, _ = qr.symbol_size()
    total_modules = module_count + border * 2
    scale = max(math.floor(size / total_modules), 1)

    for fmt in FORMATS:
        # AI 対応: PDF 互換出力を .ai 拡張子で保存
        if fmt == 'ai':
            kind = 'pdf'
            ext = 'ai'
        else:
            kind = fmt
            ext = fmt
        filename = f"{code}_{size}x{size}.{ext}"
        out_path = output_dir / filename
        try:
            qr.save(out_path, kind=kind, scale=scale, border=border)
            logging.info("Generated %s", out_path)
        except Exception as e:
            logging.error("Failed to generate %s: %s", out_path, e)


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    input_file: Path = args.input
    output_dir: Path = args.output
    error_level: str = args.error_level

    if not input_file.exists():
        logging.error("Input file not found: %s", input_file)
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    with input_file.open(encoding="utf-8") as f:
        for line in f:
            url = line.strip()
            if not url:
                continue
            generate_qr_images(url, SIZE, error_level, output_dir)


if __name__ == "__main__":
    main()
