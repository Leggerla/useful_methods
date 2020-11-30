import os
import random

def random_split(data_path, n_train):
  train_paths = []
  test_paths = []
  for class_path in os.listdir(data_path):
    cur_path = os.path.join(data_path, class_path)
    img_paths = os.listdir(cur_path)
    ids = range(len(img_paths))
    train_ids = random.sample(ids, n_train)
    test_ids = [i for i in ids if i not in train_ids]
    train_paths.extend([os.path.join(cur_path, img_paths[i]) for i in train_ids])
    test_paths.extend([os.path.join(cur_path, img_paths[i]) for i in test_ids])
  return train_paths, test_paths
