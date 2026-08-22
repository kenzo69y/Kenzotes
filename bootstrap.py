import base64
import io
import runpy
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS_DIR = ROOT / "package_parts"
RUNTIME_DIR = ROOT / ".runtime"

parts = sorted(PARTS_DIR.glob("part*.b64"))
if not parts:
    raise RuntimeError("Package parts tidak ditemukan.")

payload_b64 = "".join(part.read_text(encoding="utf-8").strip() for part in parts)
payload = base64.b64decode(payload_b64)

if RUNTIME_DIR.exists():
    shutil.rmtree(RUNTIME_DIR)
RUNTIME_DIR.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(io.BytesIO(payload)) as archive:
    archive.extractall(RUNTIME_DIR)

bot_dir = RUNTIME_DIR / "OpencloseAdminBot"
bot_file = bot_dir / "bot.py"
if not bot_file.exists():
    raise RuntimeError("bot.py tidak ditemukan setelah extract package.")

sys.path.insert(0, str(bot_dir))
runpy.run_path(str(bot_file), run_name="__main__")
