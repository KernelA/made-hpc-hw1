import pathlib
from xml.etree import ElementTree
import csv

import hydra


@hydra.main(config_path="configs", config_name="convert")
def main(config):
    out_file = pathlib.Path(config.path_to_output)
    out_file.parent.mkdir(exist_ok=True, parents=True)

    with open(config.path_to_input, "r", encoding="utf-8") as raw_file:
        raw_table = raw_file.read()

    root = ElementTree.fromstring(raw_table)

    with open(out_file, "w", encoding="utf-8", newline="") as out_file:
        writer = csv.writer(out_file)

        row = []

        for header_elem in root.findall("./thead//th"):
            raw_text = header_elem.text.strip()
            if raw_text in ("Sum", "#1", "#500"):
                raw_text += "_GFlop/s"
            row.append(raw_text)

        writer.writerow(row)

        row.clear()

        for row_elem in root.findall("./tbody/tr"):
            for cell_elem in row_elem.findall("./td"):
                try:
                    value = float(cell_elem.text.replace(",", ""))
                    row.append(str(value))
                except ValueError:
                    row.append(cell_elem.text.strip())

            writer.writerow(row)
            row.clear()


if __name__ == "__main__":
    main()
