import os
from shutil import copyfile

backup_folder = "backup"


class FileManager:
    def find(self, name, address):
        res = []
        for root, subfolders, files in os.walk(address):
            for file in files:
                if file == name:
                    res.append(root + "/" + file)
        return res

    def create_file(self, name, address):
        try:
            os.mknod(address + "/" + name)
        except FileExistsError:
            pass

    def create_dir(self, name, address):
        try:
            os.makedirs(address + "/" + name)
        except FileExistsError:
            pass

    def delete(self, name, address):
        try:
            self.create_backup()
            # old_path = address + "/" + name
            # new_path = backup_folder + "/" + old_path
            # try:
            #     os.makedirs(backup_folder + "/" + address)
            # except FileExistsError:
            #     pass
            # os.rename(old_path, new_path)
            old_path = os.path.join(address, name)
            old_name = old_path.replace("/", "%")
            new_path = os.path.join(backup_folder, old_name)
            os.rename(old_path, new_path)
        except FileNotFoundError:
            pass

    def restore(self, name):
        # TODO: no idea how to do a time based restoring
        self.create_backup()
        matched = []
        for root, subfolders, files in os.walk(backup_folder):
            for file in files:
                if file.rsplit("%")[-1] == name:
                    matched.append(os.path.join(root, file))
        matched.sort(key=lambda x: os.path.getmtime(x))
        return matched

    def create_backup(self):
        try:
            os.makedirs(backup_folder)
        except FileExistsError:
            pass
