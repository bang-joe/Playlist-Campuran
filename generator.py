import os
import re
import requests

# 100% Genuine Vidio Channels (Direct Akamai CDN via Jakarta VPS Tokenizer)
VIDIO_CHANNELS = [
    # Platinum Sports & Asian Games
    {"id": "brisuperleague", "name": "BRI Super League (Liga 1)", "logo": "https://thumbor.prod.vidiocdn.com/live/22207.png"},
    {"id": "laliga", "name": "La Liga", "logo": "https://thumbor.prod.vidiocdn.com/live/22057.png"},
    {"id": "asiangames1", "name": "Asian Games 1", "logo": "https://thumbor.prod.vidiocdn.com/live/22240.png"},
    {"id": "asiangames2", "name": "Asian Games 2", "logo": "https://thumbor.prod.vidiocdn.com/live/22241.png"},
    {"id": "wta", "name": "WTA Tennis", "logo": "https://thumbor.prod.vidiocdn.com/live/20564.png"},
    {"id": "championstv1", "name": "Champions TV 1 (UCL/UEL)", "logo": "https://thumbor.prod.vidiocdn.com/live/6685.png"},
    {"id": "championstv2", "name": "Champions TV 2 (UCL/UEL)", "logo": "https://thumbor.prod.vidiocdn.com/live/6686.png"},
    {"id": "championstv3", "name": "Champions TV 3 (UCL/UEL)", "logo": "https://thumbor.prod.vidiocdn.com/live/6786.png"},
    {"id": "championstv5", "name": "Champions TV 5", "logo": "https://thumbor.prod.vidiocdn.com/live/9182.png"},
    {"id": "championstv6", "name": "Champions TV 6", "logo": "https://thumbor.prod.vidiocdn.com/live/9183.png"},
    {"id": "championsgolf1", "name": "Champions Golf 1", "logo": "https://thumbor.prod.vidiocdn.com/live/18189.png"},
    {"id": "championsgolf2", "name": "Champions Golf 2", "logo": "https://thumbor.prod.vidiocdn.com/live/18190.png"},
    {"id": "championsfight", "name": "Champions Fight", "logo": "https://thumbor.prod.vidiocdn.com/live/20216.png"},

    # National & News (100% Genuine Vidio Akamai 24 Jam)
    {"id": "metrotv", "name": "Metro TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/metrotv.png"},
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
    {"id": "elshintatv", "name": "Elshinta TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/elshinta.png"},
    {"id": "makkahtv", "name": "Makkah TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/makkahtv.png"},
    {"id": "dmitv", "name": "DMI TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/dmitv.png"},
    {"id": "uchanneltv", "name": "U-Channel TV HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/uchannel.png"},

    # Entertainment, Movies & Music
    {"id": "citradrama", "name": "Citra Drama HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/citradrama.png"},
    {"id": "citraplus", "name": "Citra Plus HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/citraplus.png"},
    {"id": "citramuslim", "name": "Citra Muslim HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/citramuslim.png"},
    {"id": "tvn", "name": "TVN HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/tvn.png"},
    {"id": "rockaction", "name": "Rock Action HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/rockaction.png"},
    {"id": "musica", "name": "MUSICA HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/musica.png"},

    # International News
    {"id": "cna", "name": "CNA HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/cna.png"},
    {"id": "euronews", "name": "Euronews HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/euronews.png"},
    {"id": "abcaustralia", "name": "ABC Australia HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/abcaustralia.png"},
    {"id": "nhkworld", "name": "NHK World Japan HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/nhkworld.png"},
    {"id": "africanews", "name": "Africanews HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/africanews.png"},
    {"id": "arirang", "name": "Arirang HD", "logo": "https://raw.githubusercontent.com/AqFad2811/indonesia-iptv/refs/heads/main/logo/arirang.png"},
]

SERVER_URL = "http://202.155.18.227:8080/live"

def generate():
    new_entries = []
    for ch in VIDIO_CHANNELS:
        ch_id = ch["id"]
        ch_name = ch["name"]
        ch_logo = ch["logo"]
        stream_url = f"{SERVER_URL}/{ch_id}.m3u8"
        
        entry = (
            f'#EXTINF:-1 tvg-id="{ch_name}" tvg-name="{ch_name}" tvg-logo="{ch_logo}" group-title="VIDIO",{ch_name}\n'
            f'#EXTVLCOPT:http-referrer=https://www.vidio.com/\n'
            f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36\n'
            f'{stream_url}'
        )
        new_entries.append(entry)

    vidio_block = "# === VIDIO CHANNELS START ===\n" + "\n\n".join(new_entries) + "\n# === VIDIO CHANNELS END ==="

    target_file = "Tvstream"
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        r = requests.get("https://raw.githubusercontent.com/bang-joe/Playlist-Campuran/refs/heads/main/Tvstream")
        content = r.text

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

    print(f"Success! Updated {target_file} with {len(VIDIO_CHANNELS)} authentic Vidio channels.")

if __name__ == "__main__":
    generate()
