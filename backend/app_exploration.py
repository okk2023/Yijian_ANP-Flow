from flask import Flask, render_template, request, jsonify, Blueprint
import sys
sys.path.append('./backend')
from params import *
import subprocess

blueprint = Blueprint('exploration', __name__)

@blueprint.route('/')
def exploration_homepage():
    return render_template('exploration.html', params=GLOBAL_PARAMS)

@blueprint.route('/run_task1', methods=['POST'])
def run_task1():
    # 获取用户选择的参数
    param1 = request.form.get('param1')
    param2 = request.form.get('param2')
    param3 = request.form.get('param3')

    # 验证参数是否合法
    if (param1 not in GLOBAL_PARAMS["param1"] or
            param2 not in GLOBAL_PARAMS["param2"] or
            param3 not in GLOBAL_PARAMS["param3"]):
        return jsonify({'success': False, 'error': '无效参数'})

    try:
        # 构建命令 - 根据实际.sh脚本需求调整
        command = f"bash {os.path.join(SCRIPTS_DIR, 'task1.sh')} {param1} {param2} {param3}"

        # 运行脚本
        result = subprocess.run(command, shell=True,
                                capture_output=True,
                                text=True,
                                cwd=SCRIPTS_DIR)

        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})