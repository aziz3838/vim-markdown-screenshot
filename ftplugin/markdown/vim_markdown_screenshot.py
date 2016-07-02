import subprocess
import tempfile
import vim


# Default Constants
IMG_DIR = '/tmp/'
TAG_ALT_TEXT = 'img'


def get_global_variables():
    '''
    Returns screenshot global variables if set; otherwise,
    it returns the default values of:
        screenshot_img_dir:     '/tmp/'
        screenshot_tag_img_dir:  defaults to screenshot_img_dir
        screenshot_tag_alt_text: 'img'
    '''
    # screenshot_img_dir
    if int(vim.eval('exists("g:screenshot_img_dir")')):
        img_dir = vim.eval("g:screenshot_img_dir")
    else:
        img_dir = IMG_DIR

    # screenshot_tag_img_dir
    if int(vim.eval('exists("g:screenshot_tag_img_dir")')):
        tag_img_dir = vim.eval("g:screenshot_tag_img_dir")
    else:
        tag_img_dir = img_dir

    # screenshot_tag_alt_text
    if int(vim.eval('exists("g:screenshot_tag_alt_text")')):
        tag_alt_text = vim.eval("g:screenshot_tag_alt_text")
    else:
        tag_alt_text = TAG_ALT_TEXT

    return img_dir, tag_img_dir, tag_alt_text


def take_screenshot():
    '''
    Takes the screenshot, stores it, and inserts formatted markdown tag
    into buffer.
    '''
    # Get variables
    img_dir, tag_img_dir, tag_alt_text = get_global_variables()
    # Get path/name for new screenshot
    img_path = tempfile.NamedTemporaryFile(prefix='', suffix='.png',
                                           dir=img_dir, delete=False).name
    # Take the screenshot
    cmd = "gnome-screenshot -a -f " + img_path
    subprocess.call(cmd, shell=True)
    # Format the markdown tag
    image_filename = img_path.split('/')[-1]
    tag = '![%s](%s)' % (tag_alt_text, tag_img_dir+image_filename)
    # Insert the tag into buffer
    vim.command("normal! a" + tag + '\n\n')
