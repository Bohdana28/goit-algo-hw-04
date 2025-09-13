import argparse
from pathlib import Path
import shutil

def parse_args():
    """Отримує аргументи командного рядка"""
    parser = argparse.ArgumentParser(description="Копіювання файлів і сортування за розширенням")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("-o", "--output", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def recursive_copy(source: Path, output: Path):
    """Рекурсивно копіює файли і сортує за розширенням"""
    for el in source.iterdir():
        try:
            if el.is_dir():
                recursive_copy(el, output)  # рекурсія для піддиректорій
            elif el.is_file():
                ext = el.suffix[1:] if el.suffix else "no_extension"
                target_dir = output / ext
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(el, target_dir)
                print(f"Скопійовано: {el} -> {target_dir}")
        except Exception as e:
            print(f"Помилка з файлом {el}: {e}")

def main():
    args = parse_args()
    
    if not args.source.exists() or not args.source.is_dir():
        print(f"Вихідна директорія не існує: {args.source}")
        return
    
    recursive_copy(args.source, args.output)
    print("Копіювання завершено!")

if __name__ == "__main__":
    main()