"""Write the original November 19 world-news newspaper without network access."""
from pathlib import Path
import os


def main() -> None:
    source = Path(__file__).resolve().with_name("news.jpg")
    image = source.read_bytes()
    if len(image) > 1_048_576:
        raise ValueError("The submitted image exceeds the competition's byte limit")
    if not image.startswith(b"\xff\xd8") or not image.endswith(b"\xff\xd9"):
        raise ValueError("The image is not a complete JPEG")
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    destination.joinpath("entry.png").write_bytes(image)


if __name__ == "__main__":
    main()
