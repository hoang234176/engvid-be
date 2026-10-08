"""Main application entrypoint for EngVid Backend."""

import platform
import socket
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

# ANSI Escape Codes for Terminal Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"


def get_lan_ip() -> str | None:
    """Detect local network IPv4 address.

    Returns:
        str | None: LAN IP address if connected to a network, otherwise None.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Connect to public DNS to determine default network interface
            sock.connect(("8.8.8.8", 80))
            return str(sock.getsockname()[0])
    except OSError:
        return None


def get_mdns_hostname() -> str | None:
    """Retrieve mDNS hostname on macOS (e.g., 'macbook.local').

    Only returns value on Darwin (macOS) systems.

    Returns:
        str | None: Hostname with .local suffix on macOS, None on other OS.
    """
    if platform.system() == "Darwin":
        hostname = socket.gethostname().removesuffix(".local")
        return f"{hostname}.local"
    return None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan context manager for startup and shutdown events."""
    port = 8000
    lan_ip = get_lan_ip()
    mdns_name = get_mdns_hostname()

    print(f"\n{CYAN}{'═' * 60}{RESET}")
    print(f"{BOLD}{GREEN}🚀 EngVid Backend Server Ready:{RESET}")
    print(f"  {YELLOW}➜{RESET}  Local:      {CYAN}http://127.0.0.1:{port}/{RESET}")
    print(f"  {YELLOW}➜{RESET}  Localhost:  {CYAN}http://localhost:{port}/{RESET}")

    if mdns_name:
        print(f"  {YELLOW}➜{RESET}  macOS mDNS: {CYAN}http://{mdns_name}:{port}/{RESET}")

    if lan_ip and lan_ip != "127.0.0.1":
        print(f"  {YELLOW}➜{RESET}  LAN (Wi-Fi): {CYAN}{BOLD}http://{lan_ip}:{port}/{RESET}")

    print(f"\n{BOLD}{BLUE}📚 API Documentation (Swagger UI):{RESET}")
    print(f"  {YELLOW}➜{RESET}  Local:      {CYAN}http://127.0.0.1:{port}/docs{RESET}")
    print(f"  {YELLOW}➜{RESET}  Localhost:  {CYAN}http://localhost:{port}/docs{RESET}")

    if mdns_name:
        print(f"  {YELLOW}➜{RESET}  macOS mDNS: {CYAN}http://{mdns_name}:{port}/docs{RESET}")

    if lan_ip and lan_ip != "127.0.0.1":
        print(f"  {YELLOW}➜{RESET}  LAN (Wi-Fi): {CYAN}{BOLD}http://{lan_ip}:{port}/docs{RESET}")

    print(f"{CYAN}{'═' * 60}{RESET}\n")

    yield


app = FastAPI(
    title="EngVid Backend API",
    description="Backend API services for EngVid platform.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/", tags=["Health"])
async def root() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        dict[str, str]: Basic status message confirming the API is live.
    """
    return {
        "status": "ok",
        "message": "Welcome to EngVid Backend API",
    }
