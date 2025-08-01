from flask import Flask, render_template, jsonify, Blueprint, request
import sys
sys.path.append('./backend')
from params import *
import subprocess
import threading

blueprint = Blueprint('simulation', __name__)

@blueprint.route('/')
def simulation_homepage():
    return render_template('simulation.html', hierarchy=build_hierarchy(), params=GLOBAL_PARAMS)

from collections import deque
output_buffer = deque(maxlen=1000)  # 限制最大行数防止内存耗尽
process = None

def run_command(cloud_model_path, save_path):
    global process, output_buffer
    sbtMain = 'trueasync.ANP_ST.ANP_ST_top_App' if 'SpikeFormer' in cloud_model_path else "trueasync.example.NoCExample"
    try:
        process = subprocess.Popen(['/bin/bash', '/home/zhangjian22/anchain/processes/simulate.sh', sbtMain, cloud_model_path, '/data/zhangjian22/gnn/dataset/tmp.json'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True)

        # 实时读取输出
        for line in iter(process.stdout.readline, ''):
            output_buffer.append(line.strip())

    except Exception as e:
        output_buffer.append(f"Error: {str(e)}")
    finally:
        process = None

@blueprint.route('/start', methods=['POST'])
def start_process():
    # 获取用户选择的参数
    model_level = request.form.get('model-level')
    debug_level = request.form.get('debug-level')
    save_path = request.form.get('save-path')
    cloud_model_key = request.form.get('cloud_model_path')

    # 验证参数是否合法
    if (model_level not in GLOBAL_PARAMS["model_levels"] or
            debug_level not in GLOBAL_PARAMS["debug_levels"] or
                cloud_model_key not in TA_APP_CSV_DIR_DICT.keys()):
        return jsonify({'success': False, 'error': f'无效参数: {model_level}, {debug_level}, {cloud_model_key}'})

    cloud_model_path = TA_APP_CSV_DIR_DICT[cloud_model_key]
    global process
    if process is not None:
        return jsonify({'status': 'error', 'message': 'Process already running'})

    # 清空缓冲区
    output_buffer.clear()

    # 在新线程中运行命令
    thread = threading.Thread(target=run_command(cloud_model_path, save_path))
    thread.daemon = True
    thread.start()

    return jsonify({'status': 'success'})

@blueprint.route('/stop', methods=['POST'])
def stop_process():
    global process
    if process is not None:
        process.terminate()
        process = None
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'No process running'})

@blueprint.route('/get_output')
def get_output():
    # 返回所有缓冲的输出
    return jsonify({'output': list(output_buffer)})

# @blueprint.route('/')
# def index():
#     hierarchy = build_hierarchy()
#     return render_template('hierarchy.html', hierarchy=hierarchy)

@blueprint.route('/get_counts/<dataset>')
def get_counts(dataset):
    hierarchy = build_hierarchy()
    counts = hierarchy['datasets'].get(dataset, {}).get('counts', {})
    return jsonify({'counts': list(counts.keys())})

@blueprint.route('/get_net_types/<dataset>/<count>')
def get_net_types(dataset, count):
    hierarchy = build_hierarchy()
    net_types = hierarchy['datasets'].get(dataset, {}).get('counts', {}).get(count, {}).get('net_types', {})
    return jsonify({'net_types': list(net_types.keys())})

@blueprint.route('/get_numbers/<dataset>/<count>/<net_type>')
def get_numbers(dataset, count, net_type):
    hierarchy = build_hierarchy()
    numbers = hierarchy['datasets'].get(dataset, {}).get('counts', {}).get(count, {}).get('net_types', {}).get(net_type, {}).get('numbers', [])
    return jsonify({'numbers': numbers})

@blueprint.route('/get_path/<dataset>/<count>/<net_type>/<number>')
def get_path(dataset, count, net_type, number):
    key = f"{dataset}_{count}_{net_type}_{number}"
    path = TA_APP_CSV_DIR_DICT.get(key, "Not found")
    return jsonify({'path': path})
