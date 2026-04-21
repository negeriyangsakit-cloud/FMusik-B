import mpv
import os

def main():
    try:
        # Inisialisasi dengan volume default 50%
        player = mpv.MPV(video=False, ytdl=False)
        player.volume = 50 
    except:
        print("[!] Gagal memuat MPV.")
        return

    songs = [f for f in os.listdir('.') if f.endswith(('.mp3', '.MP3'))]
    
    if not songs:
        print("[!] Folder kosong.")
        return

    print("\n" + "="*30)
    print("      FMusik-B PRO v1.2")
    print("="*30)
    
    for i, song in enumerate(songs, 1):
        print(f"[{i}] {song}")

    try:
        pilih = int(input("\nNomor lagu: ")) - 1
        player.play(songs[pilih])
        
        print(f"\n[▶] Playing: {songs[pilih]}")
        print("-" * 30)
        print("KONTROL CEPAT:")
        print("  [p] Pause/Resume  [+] Vol Up")
        print("  [s] Stop          [-] Vol Down")
        print("  [q] Keluar")
        print("-" * 30)

        while True:
            tanya = input(f"Vol: {player.volume}% | CMD > ").lower()
            
            if tanya == 'q' or tanya == 's':
                player.stop()
                break
            elif tanya == 'p':
                player.pause = not player.pause
                print(">> Pause" if player.pause else ">> Resume")
            elif tanya == '+':
                player.volume = min(player.volume + 10, 100)
            elif tanya == '-':
                player.volume = max(player.volume - 10, 0)
                
    except:
        print("[!] Terjadi kesalahan.")

if __name__ == "__main__":
    main()
