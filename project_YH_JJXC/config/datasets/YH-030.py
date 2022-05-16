# dataset settings
dataset_type = 'CommonDataset'
data_root = ''
img_norm_cfg = dict(
    mean=[127, 127, 127], std=[58, 58, 58], to_rgb=True)
crop_size = (240, 240)
ratio_range = (0.4, 0.6)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', reduce_zero_label=False),
    dict(type='Resize', img_scale=None, ratio_range=ratio_range),
    dict(type='RandomRotate', prob=0.5,
         degree=(-180, 180), pad_val=255, seg_pad_val=0),
    dict(type='RandomRotate', prob=0.5,
         degree=(-180, 180), pad_val=0, seg_pad_val=0),
    dict(type='RandomCrop', crop_size=crop_size),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    dict(type='RandomFlip', prob=0.5, direction='vertical'),
    dict(type='PhotoMetricDistortion'),

    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=0),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=None,
        img_ratios=[0.5],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=[
        dict(
            type=dataset_type,
            data_root=data_root,
            test_mode=False,
            classes=['background', 'building'],
            palette=[
                [0, 0, 0],
                [255, 0, 0]
            ],
            img_suffix='.tif',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            img_dir='/mnt/lustrenew2/hetianle/IGSNRR/data/YH/images',
            ann_dir='/mnt/lustrenew2/hetianle/IGSNRR/data/YH/labels',
            pipeline=train_pipeline),
    ],
    val=dict(
        type=dataset_type,
        data_root=data_root,
        test_mode=True,
        classes=['background', 'building'],
        palette=[
            [0, 0, 0],
            [255, 0, 0]
        ],
        img_suffix='.tif',
        seg_map_suffix='.png',
        reduce_zero_label=False,
        img_dir='/mnt/lustrenew2/hetianle/IGSNRR/data/YH/val_images',
        ann_dir='/mnt/lustrenew2/hetianle/IGSNRR/data/YH/val_labels',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        test_mode=True,
        classes=['background', 'building'],
        palette=[
            [0, 0, 0],
            [255, 0, 0]
        ],
        img_suffix='.tif',
        seg_map_suffix='.png',
        reduce_zero_label=False,
        img_dir='/mnt/lustrenew2/hetianle/IGSNRR/data/YH/val_images',
        ann_dir='/mnt/lustrenew2/hetianle/IGSNRR/data/YH/val_labels',
        pipeline=test_pipeline),

)
