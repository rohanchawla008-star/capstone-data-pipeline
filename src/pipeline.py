import subprocess
import sys

scripts = [
    "src/load_data.py",
    "src/transform_data.py",
    "src/visualization.py"
]

for script in scripts:
    print(f"\nRunning {script}...\n")

    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

print("\nPipeline execution complete.")