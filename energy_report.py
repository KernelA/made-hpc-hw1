import pathlib

import pandas as pd
from pandas_profiling import ProfileReport
import hydra


@hydra.main(config_path="configs", config_name="eda_energy")
def main(config):
    out_file = pathlib.Path(config.path_to_output)
    out_file.parent.mkdir(exist_ok=True, parents=True)

    data = pd.read_csv(config.path_to_input, engine="c", encoding="utf-8")

    report = ProfileReport(data)
    report.to_file(str(out_file))


if __name__ == "__main__":
    main()
