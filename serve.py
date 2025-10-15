#!/usr/bin/env python3
"""Startet einen einfachen lokalen Webserver für die Projektdateien."""

from __future__ import annotations

import argparse
import contextlib
import socket
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Startet einen lokalen HTTP-Server für die Suche.",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Hostname oder IP, auf der der Server lauscht (Standard: 127.0.0.1).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port, auf dem der Server erreichbar ist (Standard: 8000).",
    )
    parser.add_argument(
        "--directory",
        default=None,
        help="Basisverzeichnis für die Dateien. Standard ist das Projektverzeichnis.",
    )
    return parser.parse_args()


def pretty_host(host: str) -> str:
    if host != "0.0.0.0":
        return host

    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
        try:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
        except OSError:
            return "localhost"


def main() -> None:
    args = parse_args()

    root_dir = (
        Path(args.directory).expanduser().resolve()
        if args.directory
        else Path(__file__).parent.resolve()
    )

    if not root_dir.exists():
        raise SystemExit(f"Verzeichnis nicht gefunden: {root_dir}")

    handler = partial(SimpleHTTPRequestHandler, directory=str(root_dir))
    server = ThreadingHTTPServer((args.host, args.port), handler)

    host_display = pretty_host(args.host)
    print(f"Serving {root_dir} unter http://{host_display}:{args.port}/ (Ctrl+C zum Beenden)")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer beendet.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
