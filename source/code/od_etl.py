from tqdm import tqdm
import requests
import os
import logging
import tarfile


class ODETL:

    def __init__(self, local_path, file_name='ALOI_withoutdupl_norm.arff'):
        self.logger = logging.getLogger(ODETL.__name__)
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(ch)
        self.logger.info('\nINITIALIZING...')
        self.local_path = local_path
        self.file_name = file_name
        self.logger.info('INITIALIZATION HAS BEEN COMPLETED')

    def get_raw_data(self, url):
        file_name = url.split('/')[-1]
        if not os.path.exists(os.path.join(self.local_path, file_name)):
            self.logger.info('ARCHIVE FILE HAS NOT BEEN DOWNLOADED YET')
            if not os.path.exists(self.local_path):
                self.logger.info('CREATE LOCAL DIRECTORY')
                os.mkdir(self.local_path)
            self.logger.info('START DOWNLOADING ARCHIVE FILE')
            response = requests.get(url, stream=True)
            with open(os.path.join(self.local_path, file_name), "wb") as handle:
                for data in tqdm(response.iter_content()):
                    handle.write(data)
            self.logger.info('ARCHIVE FILE DOWNLOADING HAS BEEN COMPLETED')
            # ==========================================================================================================
            if not os.path.exists(os.path.join(self.local_path, 'unzipped')):
                self.logger.info('ARCHIVE FILE HAS NOT BEEN UNZIPPED YET')
                self.logger.info('UNZIP ARCHIVE FILE')
                with tarfile.open(os.path.join(self.local_path, file_name), 'r:gz') as _tar:
                    for member in tqdm(_tar):
                        if member.isdir():
                            continue
                        fname = member.name.rsplit('/', 1)[1]
                        _tar.makefile(member, os.path.join(self.local_path, fname))
                self.logger.info('ARCHIVE FILE HAS BEEN UNZIPPED')
                open(os.path.join(self.local_path, 'unzipped'), 'a').close()
            # ==========================================================================================================
        else:
            self.logger.info('ARCHIVE FILE HAS BEEN ALREADY DOWNLOADED')
            # ==========================================================================================================
            if not os.path.exists(os.path.join(self.local_path, 'unzipped')):
                self.logger.info('ARCHIVE FILE HAS NOT BEEN UNZIPPED YET')
                self.logger.info('UNZIP ARCHIVE FILE')
                with tarfile.open(os.path.join(self.local_path, file_name), 'r:gz') as _tar:
                    for member in tqdm(_tar):
                        if member.isdir():
                            continue
                        fname = member.name.rsplit('/', 1)[1]
                        _tar.makefile(member, os.path.join(self.local_path, fname))
                self.logger.info('ARCHIVE FILE HAS BEEN UNZIPPED')
                open(os.path.join(self.local_path, 'unzipped'), 'a').close()
            # ==========================================================================================================
            else:
                self.logger.info('ARCHIVE FILE HAS BEEN ALREADY UNZIPPED')
