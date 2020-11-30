import os
import random

def random_split(data_path, n_train):
  train_paths = []
  test_paths = []
  classes_paths = os.listdir(data_path)
  class_ids = range(len(classes_paths))
  for class_id in class_ids:
    class_path = classes_paths[class_id]
    cur_path = os.path.join(data_path, class_path)
    img_paths = os.listdir(cur_path)
    ids = range(len(img_paths))
    train_ids = random.sample(ids, n_train)
    test_ids = [i for i in ids if i not in train_ids]
    train_paths.extend([(os.path.join(cur_path, img_paths[i]), class_id) for i in train_ids])
    test_paths.extend([(os.path.join(cur_path, img_paths[i]), class_id) for i in test_ids])
  return train_paths, test_paths

from torch.utils.data import Dataset

class MyDataset(Dataset):
    
    def __init__(self, data, open_method=None, transform=None):

        self.data = data
        self.len_dataset = len(self.data)
        self.open_method = open_method
        self.transform = transform
    
    def __len__(self):
        return self.len_dataset
    
    def __getitem__(self, idx):

        X, y = self.data[idx]
        if self.open_method:
          X = self.open_method(X)
        if self.transform:
          X = self.transform(X)
        
        return X, y
