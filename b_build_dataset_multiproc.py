import os
import json
from zipfile import ZipFile
import shutil
import xmltodict
from uuid import uuid4
from multiprocessing import Pool
from itertools import chain

PATH = '../Full/'
OUTPUT_PATH = '../output'
OUTPUT_SUB_PATH = 'images'


def process(moment):
    output_data = list()
    n_exceptions = 0
    n_correct = 0
    last_exception_uri = ""
    moment_path = os.path.join(PATH, moment)
    zip_files = os.listdir(moment_path)
    unzip_folders = list()
    for zip_file in zip_files:
        zip_file_path = os.path.join(moment_path, zip_file)
        if '.zip' not in zip_file_path:
            continue
        try:
            with ZipFile(zip_file_path, 'r') as zip_obj:
                if "PIC" in zip_file_path and "Diff" not in PATH:
                    zip_obj.extractall(os.path.split(zip_file_path[:-4])[0])
                    unzipped = set([os.path.split(str(file))[0].split("/")[0] for file in zip_obj.NameToInfo.keys()])
                    unzip_folders.extend(list(map(lambda x: os.path.join(moment_path, x), unzipped)))
                else:
                    unzip_folder = zip_file_path[:-4]
                    zip_obj.extractall(unzip_folder)
                    unzip_folders.append(unzip_folder)
        except:
            print("Zip error", zip_file_path)
    folder_files = os.listdir(moment_path)
    for folder_file in folder_files:
        if '.zip' in folder_file or 'PIC' in folder_file:
            continue
        folder_file = os.path.join(moment_path, folder_file)
        for root, dirs, files in os.walk(folder_file):
            for file in files:
                file = os.path.join(root, file)
                with open(file, encoding='utf-8') as fin:
                    exception = False
                    id, uri, vienna_codes, txt = None, None, None, None
                    try:
                        doc = xmltodict.parse(fin.read())
                        id = doc['Transaction']['TradeMarkTransactionBody']['TransactionContentDetails'][
                            'TransactionIdentifier']
                        uri = doc['Transaction']['TradeMarkTransactionBody']['TransactionContentDetails'][
                            'TransactionData']['TradeMarkDetails']['TradeMark']['MarkImageDetails']['MarkImage'][
                            'MarkImageURI']
                        vienna_codes = doc['Transaction']['TradeMarkTransactionBody']['TransactionContentDetails'][
                            'TransactionData']['TradeMarkDetails']['TradeMark']['MarkImageDetails']['MarkImage'][
                            'MarkImageCategory']['CategoryCodeDetails']['CategoryCode']
                        txt = doc['Transaction']['TradeMarkTransactionBody']['TransactionContentDetails'][
                            'TransactionData']['TradeMarkDetails']['TradeMark']['WordMarkSpecification'][
                            'MarkVerbalElementText']
                    except:
                        pass
                    exception = None in (id, uri, vienna_codes)
                    if not exception:
                        try:
                            uri = os.path.join(moment_path, uri[7:])
                            uri = os.path.join(os.path.dirname(uri), os.listdir(os.path.dirname(uri))[0])
                            file = f"{uuid4()}{os.path.splitext(uri)[1]}"
                            shutil.move(uri, os.path.join(OUTPUT_PATH, OUTPUT_SUB_PATH, file))
                            output_data.append({"file": file, "text": txt, "vienna_codes": vienna_codes,
                                                'year': moment})
                            n_correct = n_correct + 1
                        except:
                            last_exception_uri = uri
                            n_exceptions = n_exceptions + 1
    print(moment, n_exceptions, last_exception_uri, n_correct)
    # Clean unzipped folder
    try:
        for unzip_folder in unzip_folders:
            shutil.rmtree(unzip_folder)
    except:
        print("Exception removing")
    with open(os.path.join(OUTPUT_PATH, f'output_{moment}.json'), 'w', encoding='utf-8') as fout:
        json.dump(output_data, fout)


if __name__ == '__main__':
    os.makedirs(os.path.join(OUTPUT_PATH, OUTPUT_SUB_PATH), exist_ok=True)

    with Pool(processes=4) as p:
        p.map(process, os.listdir(PATH))

