import site
import os
import shutil
import quanturf_logo
os.system("pip install jupyterlab_templates")
os.system("jupyter labextension install jupyterlab_templates")
os.system("jupyter serverextension enable --py jupyterlab_templates")

site_package_dir=site.getsitepackages()
if len(site_package_dir) == 1:
    logo_code=quanturf_logo.logo_js()
    os.chdir(site_package_dir)
    site_package_dir=' '.join(site_package_dir)
    os.chdir("../")
    os.chdir("../")
    env_dir=os.getcwd()
    src_file_path=os.path.join(env_dir,"share","jupyter","labextensions","jupyterlab_templates","static","568.a78b0ab164b288ecdc23.js")
    src_file_path = src_file_path.replace(os.sep, '/')
    src_file=open(src_file_path,"w")
    src_file.write(logo_code)
    src_file.close()

if len(site_package_dir) >= 2:
    logo_code=quanturf_logo.logo_js()
    os.chdir(site_package_dir[1])
    os.chdir("../")
    os.chdir("../")
    env_dir=os.getcwd()
    src_file_path=os.path.join(env_dir,"share","jupyter","labextensions","jupyterlab_templates","static","568.a78b0ab164b288ecdc23.js")
    src_file_path = src_file_path.replace(os.sep, '/')
    src_file=open(src_file_path,"w")
    src_file.write(logo_code)
    src_file.close()

def main():
    print("Running Jupyter platform!")
    out = site.getsitepackages()
    if len(out) == 1:
        str_out = out
        out1 = ' '.join(str_out)
        filename = os.path.join(out1, "quanturf", "jupyter_notebook_config.py")
        filename2 = filename.replace(os.sep, '/')
        filename3 = os.path.join(
            out1, "jupyterlab_templates/templates/jupyterlab_templates/")
        src_file = os.path.join(out1, "quanturf", "quanturf.ipynb")
        src_path = src_file
        dst_path = filename3.replace(os.sep, '/')
        shutil.copy(src_path, dst_path)
        os.system("jupyter lab --config=" + filename2)
    if len(out) >= 2:
        str_out = out[1]
        filename = os.path.join(str_out, "quanturf",
                                "jupyter_notebook_config.py")
        filename2 = filename.replace(os.sep, '/')
        filename3 = os.path.join(
            str_out, "jupyterlab_templates/templates/jupyterlab_templates/")
        filename3 = os.path.join(
            str_out, "jupyterlab_templates/templates/jupyterlab_templates/")
        src_file = os.path.join(str_out, "quanturf", "quanturf.ipynb")
        src_path = src_file
        dst_path = filename3.replace(os.sep, '/')
        shutil.copy(src_path, dst_path)
        os.system("jupyter lab --config=" + filename2)


if __name__ == "__main__":
    main()


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
