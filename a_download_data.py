import os
from ftplib import FTP

OUTPUT_DIR = 'output'
UNTIL = 2020
if __name__ == '__main__':
    ftp = FTP('ftp.euipo.europa.eu')
    ftp.login('opendata', 'kagar1n')
    ftp.cwd('/Trademark/Full')
    folders = [f for f in ftp.nlst(".") if int(f) <= UNTIL]

    for folder in folders:
        ftp.cwd(folder)
        for file in ftp.nlst('.'):
            print(folder, file)
            output_folder = os.path.join(OUTPUT_DIR, folder)
            os.makedirs(output_folder, exist_ok=True)
            local_file = open(os.path.join(output_folder, file), 'wb')
            ftp.retrbinary('RETR ' + file, local_file.write)
            local_file.close()
        ftp.cwd('..')

    ftp.quit()
