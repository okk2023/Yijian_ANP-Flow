import os

# 配置路径
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), '../processes')

# 全局预设参数
GLOBAL_PARAMS = {
    "nets": ["全连接网络 FC", "脉冲卷积网络 SCNN", "脉冲循环网络 SRNN", "脉冲大模型 SpikeFormer"],
    "model_levels": ["异步控制器级", "模块级", "节点级"],
    "debug_levels": ["debug级", "info级", "warn级"],
    "apps": ["MNIST 手写数字集分类", "N-MNIST 类脑手写数字集分类", "Fashion-MNIST 时尚商品分类", "CIFAR-10 图像分类",
             "CIFAR-10-DVS DVS图像分类", "CIFAR-100 图像分类", "ImageNet 图像分类", "Tiny-ImageNet 图像分类"],
}

# Params for TrueAsync Simulation
TA_APP_CSV_DIR_BASE = "/data/zhangjian22/trueasync/"
TA_APP_CSV_DIR_DICT = {
    'MNIST_10_FC_2' : f"{TA_APP_CSV_DIR_BASE}/mnist10.pe2/mnist10.dat",
    'MNIST_10_FC_10' : f"{TA_APP_CSV_DIR_BASE}/mnist10.pe10/mnist10.dat",

    'MNIST_256_FC_4' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe4/mnist256.dat",
    'MNIST_256_FC_9' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe9/mnist256.dat",
    'MNIST_256_FC_16' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe16/mnist256.dat",
    'MNIST_256_FC_25' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe25/mnist256.dat",
    'MNIST_256_CONV_32' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe32.conv",
    'MNIST_256_FC_36' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe36/mnist256.dat",
    'MNIST_256_FC_49' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe49/mnist256.dat",
    'MNIST_256_FC_64' : f"{TA_APP_CSV_DIR_BASE}/mnist256.pe64/mnist256.dat",

    'NMNIST_128_FC_1' : f"{TA_APP_CSV_DIR_BASE}/nmnist128.dat",
    'NMNIST_256_FC_2' : f"{TA_APP_CSV_DIR_BASE}/nmnist256.dat",
    'NMNIST_512_FC_16' : f"{TA_APP_CSV_DIR_BASE}/nmnist512.dat",
    'NMNIST_1024_FC_2' : f"{TA_APP_CSV_DIR_BASE}/nmnist1024.dat",

    # 'FashionMNIST_256_FC_16' : f"{TA_APP_CSV_DIR_BASE}/fashion_mnist.dat",

    # 'DVS128Gesture_1024_AutoSNN16_4' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_16/DVS128Gesture16.dat",
    'DVS128Gesture_512_CONV_1' : f"{TA_APP_CSV_DIR_BASE}/dvs_gesture48.dat",
    # 'DVS128Gesture_512_FC_16' : f"{TA_APP_CSV_DIR_BASE}/dvs_gesture.dat_FC",

    'CIFAR10_None_SpikeFormer_2' : "CIFAR10_None_SpikeFormer_2",

    'CIFAR10_1024_AutoSNN16_16' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_16/CIFAR1016.dat",
    'CIFAR10_1024_AutoSNN128_2' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_128/CIFAR10128.dat",
    'CIFAR10_1024_SpikeSim_240' : f"{TA_APP_CSV_DIR_BASE}/spikesim/cifar1016.dat",

    'CIFAR100_1024_AutoSNN16_1' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_16/CIFAR10016.dat",
    'CIFAR100_1024_AutoSNN128_8' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_128/CIFAR100128.dat",

    # 'CIFAR10DVS_1024_AutoSNN16_2' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_16/CIFAR10DVS16.dat",

    'TinyImageNet_1024_AutoSNN16_32' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_16/data/tiny-imagenet",
    'TinyImageNet_1024_AutoSNN64_8' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_64/Tiny-ImageNet-20064.dat",

    'SVHN_1024_AutoSNN64_8' : f"{TA_APP_CSV_DIR_BASE}/AutoSNN_64/SVHN64.dat",
}

def build_hierarchy():
    """构建四级选择层级结构"""
    hierarchy = {
        'datasets': {},
        'counts': {},
        'net_types': {},
        'numbers': {}
    }

    for key in TA_APP_CSV_DIR_DICT.keys():
        parts = key.split('_')
        if len(parts) != 4:
            continue  # 跳过不符合格式的键

        dataset, count, net_type, number = parts

        # 构建数据集层级
        if dataset not in hierarchy['datasets']:
            hierarchy['datasets'][dataset] = {
                'name': dataset,
                'counts': {}
            }

        # 构建数量层级
        if count not in hierarchy['datasets'][dataset]['counts']:
            hierarchy['datasets'][dataset]['counts'][count] = {
                'name': count,
                'net_types': {}
            }

        # 构建网络类型层级
        if net_type not in hierarchy['datasets'][dataset]['counts'][count]['net_types']:
            hierarchy['datasets'][dataset]['counts'][count]['net_types'][net_type] = {
                'name': net_type,
                'numbers': []
            }

        # 添加编号
        if number not in hierarchy['datasets'][dataset]['counts'][count]['net_types'][net_type]['numbers']:
            hierarchy['datasets'][dataset]['counts'][count]['net_types'][net_type]['numbers'].append(number)

    return hierarchy

if __name__ == "__main__":
    hierarchy = build_hierarchy()
    import json
    print(json.dumps(hierarchy, indent=4, ensure_ascii=False))
    # 输出层级结构
    for dataset, data in hierarchy['datasets'].items():
        print(f"Dataset: {data['name']}")
        for count, count_data in data['counts'].items():
            print(f"  Count: {count_data['name']}")
            for net_type, net_data in count_data['net_types'].items():
                print(f"    Net Type: {net_data['name']}")
                for number in net_data['numbers']:
                    print(f"      Number: {number}")