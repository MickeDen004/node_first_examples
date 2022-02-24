from python_utils import log, read_settings, run, DF_PATH, SETTINGS_JSON
from metadata_utils import FileProcessor

INPUT_PORT = 'input-data-frame'
OUTPUT_PORT = 'output-data-frame'


def main(**kwargs):
    log("Node execution has started")

    log("Reading settings")
    settings = read_settings(SETTINGS_JSON)
    column1 = settings["column1"]["selectedColumn"]
    column2 = settings["column2"]["selectedColumn"]
    new_name = settings["new_name"]["value"]

    log("Reading dataframe")
    file_processor = FileProcessor(df_path=DF_PATH)
    input_df = file_processor.read_df(INPUT_PORT)

    log('Performing calculations')
    new_col = input_df[column1].astype(str)+input_df[column2].astype(str)
    input_df[new_name] = new_col

    log("Saving resulting dataframes")
    file_processor.save_df(input_df, OUTPUT_PORT, **kwargs)

    log("Done.\n")


if __name__ == '__main__':
    run(main)
