from flask import Flask, render_template, send_from_directory,Response
import os
import mimetypes
import time

app = Flask(__name__)

# 设置本地文件夹路径
UPLOAD_FOLDER = 'workspace'
app.config['WORKSPACE'] = UPLOAD_FOLDER
LOG_FILE = '20250308.log'
FILE_CHECK_INTERVAL = 0.5  # 文件检查间隔（秒）

@app.route('/')
def index():
    files = os.listdir(app.config['WORKSPACE'])
    return render_template('index.html', files=files)

@app.route('/file/<filename>')
def file(filename):
    file_path = os.path.join(app.config['WORKSPACE'], filename)
    if os.path.isfile(file_path):
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type and mime_type.startswith('text/'):
            if mime_type == 'text/html':
                return send_from_directory(app.config['WORKSPACE'], filename)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                return render_template('code.html', filename=filename, content=content)
        elif mime_type == 'application/pdf':
            return send_from_directory(app.config['WORKSPACE'], filename)
        # elif mime_type in ['application/vnd.ms-powerpoint',
        #                    'application/vnd.openxmlformats-officedocument.presentationml.presentation']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='ppt')
        # elif mime_type in ['application/msword',
        #                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='word')
        # elif mime_type in ['application/vnd.ms-excel',
        #                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='excel')
        # elif mime_type in ['application/vnd.ms-powerpoint',
        #                    'application/vnd.openxmlformats-officedocument.presentationml.presentation']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='ppt')
        # elif mime_type in ['application/msword',
        #                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='word')
        # elif mime_type in ['application/vnd.ms-excel',
        #                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='excel')

        else:
            return send_from_directory(app.config['WORKSPACE'], filename)
    else:
        return "File not found", 404

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
    app.run(debug=True)
