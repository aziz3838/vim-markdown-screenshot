import subprocess
import tempfile
import vim


# Constants
IMG_DIR = '/img/'
ALT_TEXT = 'img'


def take_screenshot():

    img_path = tempfile.NamedTemporaryFile(prefix='', suffix='.png',
                                           dir=IMG_DIR, delete=False).name
    cmd = "gnome-screenshot -a -f " + img_path
    subprocess.call(cmd, shell=True)
    tag = '![%s](%s)' % (ALT_TEXT, img_path)
    vim.command("normal a" + ' ' + tag + ' ')
