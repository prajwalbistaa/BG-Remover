from pathlib import Path

from rembg import remove

script_dir = Path(__file__).resolve().parent
input_path = script_dir / "input.jpg"
output_path = script_dir / "output.png"

with input_path.open("rb") as input_img:
    input_data = input_img.read()

output_data = remove(
    input_data,
    providers=["CPUExecutionProvider"],
)

with output_path.open("wb") as output_img:
    output_img.write(output_data)

print("Background removed successfully!")