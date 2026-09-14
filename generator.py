import os
import re
import requests

# Daftar Saluran Resmi Kategori VIDIO (Dynamic Master Proxy Jakarta VPS 202.155.18.227)
VIDIO_CHANNELS = [
    {"id": "metrotv", "name": "Metro TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/metrotv.png"},
    {"id": "kompastv", "name": "Kompas TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/kompastv.png"},
    {"id": "indosiar", "name": "Indosiar HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/indosiar.png"},
    {"id": "btv", "name": "BTV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/btv.png"},
    {"id": "garudatv", "name": "Garuda TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/garudatv.png"},
    {"id": "beritasatu", "name": "Berita Satu HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/beritasatu.png"},
    {"id": "jaktv", "name": "Jak TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/jaktv.png"},
    {"id": "sinpotv", "name": "Sin Po TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/sinpotv.png"},
    {"id": "daaitv", "name": "DAAI TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/daaitv.png"},
    {"id": "nusantaratv", "name": "Nusantara TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/nusantaratv.png"},
    {"id": "ajwatv", "name": "Ajwa TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/ajwatv.png"},
    {"id": "magnatv", "name": "Magna TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/magnatv.png"},
    {"id": "jtv", "name": "JTV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/jtv.png"},
    {"id": "jawapostv", "name": "Jawa Pos TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/jawapostv.png"},
    {"id": "makkahtv", "name": "Makkah TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/makkahtv.png"},
    {"id": "cnnindonesia", "name": "CNN Indonesia HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/cnnindonesia.png"},
    {"id": "cnbcindonesia", "name": "CNBC Indonesia HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/cnbcindonesia.png"},
    {"id": "cna", "name": "CNA HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/cna.png"},
    {"id": "euronews", "name": "Euronews HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/euronews.png"},
    {"id": "abcaustralia", "name": "ABC Australia HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/abcaustralia.png"},
    {"id": "nhkworld", "name": "NHK World Japan HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/nhkworld.png"},
    {"id": "dmitv", "name": "DMI TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/dmitv.png"},
    {"id": "africanews", "name": "Africanews HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/africanews.png"},
    {"id": "arirang", "name": "Arirang HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/arirang.png"},
]

SERVER_URL = "http://202.155.18.227:8080/live"

def main():
    print("Memperbarui daftar saluran kategori VIDIO...")
    new_entries = []
    for ch in VIDIO_CHANNELS:
        ch_id = ch["id"]
        ch_name = ch["name"]
        ch_logo = ch["logo"]
        stream_url = f"{SERVER_URL}/{ch_id}.m3u8"
        
        entry = (
            f'#EXTINF:-1 tvg-id="{ch_name}" tvg-name="{ch_name}" tvg-logo="{ch_logo}" group-title="VIDIO",{ch_name}\\n'
            f'#EXTVLCOPT:http-referrer=https://www.vidio.com/\\n'
            f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36\\n'
            f'{stream_url}'
        )
        new_entries.append(entry)

    vidio_block = "# === VIDIO CHANNELS START ===\\n" + "\\n\\n".join(new_entries) + "\\n# === VIDIO CHANNELS END ==="

    target_file = "Tvstream"
    if not os.path.exists(target_file):
        r = requests.get("https://raw.githubusercontent.com/bang-joe/Playlist-Campuran/refs/heads/main/Tvstream")
        content = r.text
    else:
        with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

    # Hanya memperbarui blok VIDIO, saluran kategori lain tetap utuh
    if "# === VIDIO CHANNELS START ===" in content and "# === VIDIO CHANNELS END ===" in content:
        pattern = r"# === VIDIO CHANNELS START ===.*?# === VIDIO CHANNELS END ==="
        updated_content = re.sub(pattern, vidio_block, content, flags=re.DOTALL)
    else:
        if content.startswith("#EXTM3U"):
            lines = content.split("\\n", 1)
            updated_content = lines[0] + "\\n" + vidio_block + "\\n" + (lines[1] if len(lines) > 1 else "")
        else:
            updated_content = "#EXTM3U\\n" + vidio_block + "\\n" + content

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("File Tvstream sukses diperbarui dengan saluran VIDIO permanen!")

if __name__ == "__main__":
    main()
