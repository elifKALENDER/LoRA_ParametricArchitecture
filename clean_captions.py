from pathlib import Path

DATASET_DIR = Path("dataset/facade_parametric")  # png + txt burada
TRIGGER = "pf_parametric_facade"

for txt_file in DATASET_DIR.glob("*.txt"):
    text = txt_file.read_text(encoding="utf-8").lower()

    # trigger tekrarlarını temizle
    text = text.replace(TRIGGER, "")
    text = text.replace("parametricfacade", "")

    # sadeleştir
    text = text.replace("  ", " ").strip(", ")

    final_caption = f"{TRIGGER}, parametric building facade, {text}"

    txt_file.write_text(final_caption.strip(), encoding="utf-8")
    print("✔ cleaned:", txt_file.name)
