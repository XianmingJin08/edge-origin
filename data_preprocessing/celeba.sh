mkdir datasets
python ./scripts/flist.py --path ../edge-connect/img_align_celeba/img_align_celeba --output ./datasets/celeba_train.flist
python ./scripts/flist.py --path ../edge-connect/data/celeba/test --output ./datasets/celeba_test.flist
python ./scripts/flist.py --path ../edge-connect/data/celeba/eval --output ./datasets/celeba_eval.flist
python ./scripts/flist.py --path ../edge-connect/mask/testing_mask_dataset --output ./datasets/mask_test.flist
python ./data_preprocessing/create_mask_test.py --path ../edge-connect/mask/testing_mask_dataset --output ./datasets/mask_test_same_size.flist
