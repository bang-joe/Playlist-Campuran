import subprocess
import os
import re

# Daftar Saluran Resmi Kategori VIDIO
CHANNELS = [
    {"id": "205-indosiar", "name": "Indosiar HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/indosiar.png"},
    {"id": "204-sctv", "name": "SCTV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/sctv.png"},
    {"id": "206-moji", "name": "Moji HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/moji.png"},
    {"id": "8237-mentari-tv", "name": "Mentari TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/mentaritv.png"},
    {"id": "777-metro-tv", "name": "Metro TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/metrotv.png"},
    {"id": "6441-tvri", "name": "TVRI HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/tvri.png"},
    {"id": "782-antv", "name": "ANTV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/antv.png"},
    {"id": "783-tvone", "name": "tvOne HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/tvone.png"},
    {"id": "1561-rtv", "name": "RTV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/rtv.png"},
    {"id": "18162-garuda-tv", "name": "Garuda TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/garudatv.png"},
    {"id": "6165-btv", "name": "BTV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/btv.png"},
]

def get_stream_url(slug):
    cmd = f'streamlink "https://www.vidio.com/live/{slug}" --stream-url'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    out = res.stdout.strip()
    if out.startswith("http") and ".m3u8" in out:
        return out
    return None

def main():
    print("Mengambil link siaran segar dari Vidio...")
    new_entries = []
    for ch in CHANNELS:
        url = get_stream_url(ch["id"])
        if url:
            print(f"  [BERHASIL] {ch['name']}")
            entry = f'#EXTINF:-1 tvg-id="{ch["name"]}" tvg-name="{ch["name"]}" tvg-logo="{ch["logo"]}" group-title="VIDIO",{ch["name"]}\n{url}'
            new_entries.append(entry)
        else:
            print(f"  [LEWAT] {ch['name']}")

    vidio_block = "# === VIDIO CHANNELS START ===\n" + "\n".join(new_entries) + "\n# === VIDIO CHANNELS END ==="

    target_file = "Tvstream"
    if not os.path.exists(target_file):
        print("File Tvstream tidak ditemukan!")
        return

    with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Perbarui hanya blok VIDIO, channel lama (SPORTS dll) tetap aman dan tidak hilang
    if "# === VIDIO CHANNELS START ===" in content and "# === VIDIO CHANNELS END ===" in content:
        pattern = r"# === VIDIO CHANNELS START ===.*?# === VIDIO CHANNELS END ==="
        updated_content = re.sub(pattern, vidio_block, content, flags=re.DOTALL)
    else:
        if content.startswith("#EXTM3U"):
            lines = content.split("\n", 1)
            updated_content = lines[0] + "\n" + vidio_block + "\n" + (lines[1] if len(lines) > 1 else "")
        else:
            updated_content = "#EXTM3U\n" + vidio_block + "\n" + content

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("File Tvstream sukses diperbarui dengan kategori VIDIO!")

if __name__ == "__main__":
    main()
