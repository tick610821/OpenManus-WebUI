# app.py
from flask import Flask, render_template, request, jsonify,send_from_directory,Response
import mimetypes
import os
import time
from pathlib import Path

app = Flask(__name__)
app.config['WORKSPACE'] = 'workspace'

# 初始化工作目录
os.makedirs(app.config['WORKSPACE'], exist_ok=True)
LOG_FILE = '20250308.log'
FILE_CHECK_INTERVAL = 0.5  # 文件检查间隔（秒）

def get_files_pathlib(root_dir):
    """使用pathlib递归获取文件路径"""
    root = Path(root_dir)
    return [str(path) for path in root.glob('**/*') if path.is_file()]

@app.route('/')
def index():
    return render_template('index.html')


# 文件系统API
@app.route('/api/files', methods=['GET'])
def get_files():
    """获取文件树结构"""

    def list_files(path):
        file_tree = []
        for entry in get_files_pathlib(path):
            #full_path = os.path.join(path, entry)
            full_path = entry
            print(111,full_path)
            if os.path.isdir(full_path):
                file_tree.append({
                    "name": entry,
                    "type": "directory",
                    "children": list_files(full_path),
                    "ext":os.path.splitext(entry)[1].lower()
                })
            else:
                file_tree.append({
                    "name": entry,
                    "type": "file",
                    "path": os.path.relpath(full_path, app.config['WORKSPACE']),
                    "ext": os.path.splitext(os.path.relpath(full_path, app.config['WORKSPACE']))[1].lower()
                })
        return file_tree

    try:
        return jsonify(list_files(app.config['WORKSPACE']))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/file', methods=['POST'])
def get_file():
    """获取文件内容和类型信息"""
    data = request.get_json()
    try:
        file_path = os.path.join(app.config['WORKSPACE'], data['path'])
        if not os.path.isfile(file_path):
            return jsonify({"error": "文件不存在"}), 404

        # 获取文件类型
        mime_type, _ = mimetypes.guess_type(file_path)
        file_type = 'text' if mime_type and mime_type.startswith('text/') else 'binary'

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            return jsonify({
                "content": f.read(),
                "path": data['path'],
                "mime_type": mime_type,
                "file_type": file_type,
                "extension": os.path.splitext(file_path)[1].lower()
            })
    except UnicodeDecodeError:
        return jsonify({"error": "无法解码二进制文件"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/file/<path:filename>')
def serve_file(filename):
    """直接返回文件内容"""
    return send_from_directory(app.config['WORKSPACE'], filename)


@app.route('/api/save', methods=['POST'])
def save_file():
    """保存文件内容"""
    data = request.get_json()
    try:
        file_path = os.path.join(app.config['WORKSPACE'], data['path'])
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data['content'])

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/api/chat-stream', methods=['POST'])
def chat_stream():
    """流式返回日志内容"""

    def generate():
        # 记录初始文件大小
        last_size = 0
        active = True

        while active:
            # 检查文件是否存在
            if not os.path.exists(LOG_FILE):
                yield "日志文件不存在\n"
                break

            # 读取新内容
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                f.seek(last_size)
                new_content = f.read()
                last_size = f.tell()

                if new_content:
                    yield new_content

            # 检查文件是否还在变化
            time.sleep(FILE_CHECK_INTERVAL)
            current_size = os.path.getsize(LOG_FILE)
            active = (current_size != last_size)

        yield "\n[EOF]"

    return Response(generate(), mimetype='text/plain')



if __name__ == '__main__':
    app.run(debug=False)