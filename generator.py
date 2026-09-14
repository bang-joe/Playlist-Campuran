import os
import re
import requests

# 100% Genuine Vidio Channels (Direct Akamai CDN via Jakarta VPS Proxy)
# Semua logo adalah aset resmi circular PNG langsung dari Thumbor CDN Vidio
VIDIO_CHANNELS = [
    # --- National & News (100% Genuine Vidio Akamai 24 Jam) ---
    {
        "id": "tvri",
        "name": "TVRI HD",
        "logo": "https://thumbor.prod.vidiocdn.com/ot6wuFB7eQyb6RNLO6syHQKcAfU=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6441/528cc9.png"
    },
    {
        "id": "metrotv",
        "name": "Metro TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/60DNnaTD09N05GWdzrWQeEzgJyc=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/777/ea8483.png"
    },
    {
        "id": "btv",
        "name": "BTV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/idJx3fgFpGTBJrOlXrr73eAXmy8=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6165/8c950f.png"
    },
    {
        "id": "garudatv",
        "name": "Garuda TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/aRhv_g5XUCMcGb0tIvirsdYhzZE=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/18162/b4bea2.png"
    },
    {
        "id": "beritasatu",
        "name": "Berita Satu HD",
        "logo": "https://thumbor.prod.vidiocdn.com/-JKk3iTPeveKEwzEcluCSm4lMts=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/18280/c7fc8f.png"
    },
    {
        "id": "jaktv",
        "name": "Jak TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/10BeR50GodPzL51K7estpRcJqgA=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/5415/802b76.png"
    },
    {
        "id": "sinpotv",
        "name": "Sin Po TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/HwIfmxOGLIKB03toopIzIgFbzAo=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/19046/aaa3fa.png"
    },
    {
        "id": "daaitv",
        "name": "DAAI TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/lEx6FCKyVU-Hy4b_dWa-0IXZVyA=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6482/e83fcf.png"
    },
    {
        "id": "nusantaratv",
        "name": "Nusantara TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/lrUKNI0nbOJBhg6OKkH4YqNymLQ=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/7432/bfecbc.png"
    },
    {
        "id": "ajwatv",
        "name": "AJWA TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/Iwam8TZg1IczhRO5BI2xp9QESTs=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/7464/e69965.png"
    },
    {
        "id": "magnatv",
        "name": "Magna TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/hr3l92ltHJXHWqoFDKQZucGOArc=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/7230/7d6bf5.jpg"
    },
    {
        "id": "jtv",
        "name": "JTV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/3p_burlLNh7AoFeSjg3leicGhT0=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/9713/a11faf.png"
    },
    {
        "id": "jawapostv",
        "name": "Jawa Pos TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/eLJ_xPxl6WM1zgoyNjhTdsNlcXc=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/9714/5a2fad.jpg"
    },
    {
        "id": "elshintatv",
        "name": "Elshinta TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/a5BFyVvQ44YvngwwFpzBL5f6ARQ=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/10975/0dc2d8.png"
    },
    {
        "id": "makkahtv",
        "name": "Makkah TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/0k6GGofQ3N1ywnKENFTE80uI5b0=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6852/1047bc.png"
    },
    {
        "id": "dmitv",
        "name": "DMI TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/GR_VdLCahNEVwbTh0W8JIbJaBAI=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/12607/de1855.png"
    },
    {
        "id": "uchanneltv",
        "name": "U-Channel TV HD",
        "logo": "https://thumbor.prod.vidiocdn.com/x7dVSHyViTR5dTvPEMYJ_BlmJM4=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6898/7e119a.png"
    },

    # --- Entertainment, Movies & Music ---
    {
        "id": "citradrama",
        "name": "Citra Drama HD",
        "logo": "https://thumbor.prod.vidiocdn.com/2x4BLTjI91danPP7cyvJGEpaTN8=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/21179/13c032.png"
    },
    {
        "id": "citraplus",
        "name": "Citra Plus HD",
        "logo": "https://thumbor.prod.vidiocdn.com/1DqHbHGTjj8rDTriqI7pvnUSjJY=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/21289/95b5b6.png"
    },
    {
        "id": "tvn",
        "name": "TVN HD",
        "logo": "https://thumbor.prod.vidiocdn.com/mC10k5ouItm5lJ-0hipaSw3FAs8=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6362/dcd434.png"
    },
    {
        "id": "rockaction",
        "name": "Rock Action HD",
        "logo": "https://thumbor.prod.vidiocdn.com/BmgtNM-Chv9nhFT9Yk4j_k-VBHM=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/8121/e9e2b9.png"
    },
    {
        "id": "musica",
        "name": "MUSICA HD",
        "logo": "https://thumbor.prod.vidiocdn.com/9p5kOs_udy6akoXFdYxoVwz4Itk=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/7619/379f71.png"
    },

    # --- International News & Culture ---
    {
        "id": "cna",
        "name": "CNA HD",
        "logo": "https://thumbor.prod.vidiocdn.com/qFWkiN1wkTeqvgffDi7A2VPgu-8=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6411/49242c.png"
    },
    {
        "id": "euronews",
        "name": "Euronews HD",
        "logo": "https://thumbor.prod.vidiocdn.com/3eOT2unns1b3eMS7uMPzJSIlYsI=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6412/c0e105.png"
    },
    {
        "id": "abcaustralia",
        "name": "ABC Australia HD",
        "logo": "https://thumbor.prod.vidiocdn.com/MPzFu1qaq-Eb4TFUuK0ZSRCn4hU=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/7150/2de77e.png"
    },
    {
        "id": "nhkworld",
        "name": "NHK World Japan HD",
        "logo": "https://thumbor.prod.vidiocdn.com/jEN_C5faAOBCyP_FJOXREl0Z40w=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/7968/3f44ff.png"
    },
    {
        "id": "africanews",
        "name": "Africanews HD",
        "logo": "https://thumbor.prod.vidiocdn.com/YlM6ZXMDPBI488_WAyRXHpdcNB8=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/12784/b75a42.png"
    },
    {
        "id": "arirang",
        "name": "Arirang HD",
        "logo": "https://thumbor.prod.vidiocdn.com/V98kFWE8kSX24xbgPmdAn7IWqRQ=/120x120/filters:quality(70)/vidio-web-prod-livestreaming/uploads/livestreaming/square_image/6784/b9cb20.png"
    },
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

    print(f"Sukses memperbarui {target_file}! Terisi {len(VIDIO_CHANNELS)} saluran Vidio murni dengan logo bulat resmi.")

if __name__ == "__main__":
    generate()
