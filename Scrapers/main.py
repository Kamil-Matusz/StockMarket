import subprocess

def run_scripts(script_paths):
    for script_path in script_paths:
        print(f"Uruchamiam skrypt: {script_path}")
        try:
            subprocess.run(['python', script_path], check=True)
            print(f"Skrypt {script_path} zakończony.")
        except subprocess.CalledProcessError as e:
            print(f"Wystąpił błąd podczas uruchamiania skryptu: {script_path}")
            print(e)

def main():
    scripts_to_run = ['cryptocurrency_scraper.py', 'cryptostockmarket_scraper.py', 'metals_scraper.py', 'nft_scraper.py', 'etf_scraper.py']
    run_scripts(scripts_to_run)

if __name__ == "__main__":
    main()
