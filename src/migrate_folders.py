import os
import shutil

BASE_DIR = "/Users/hojin/dev/jinysite/l01.linux/src"
MAPPINGS = [
    # (Source, TargetFolder)
    # Chapter 1
    ("01_intro/prologue/linux", "01_intro/01_2_history"),
    ("01_intro/prologue", "01_intro/01_1_prologue"),
    ("01_intro/xwindow", "01_intro/01_3_xwindow"),
    
    # Chapter 2
    ("02_setup/setup/virtual", "02_setup/02_1_virtual"),
    ("02_setup/setup/ubuntu", "02_setup/02_2_ubuntu"),
    ("02_setup/setup/rocky", "02_setup/02_3_rocky"),

    # Chapter 3
    ("03_system/system/file", "03_filesystem/03_1_fhs"),
    ("03_system/system/disk", "03_filesystem/03_2_disk"),

    # Chapter 4
    ("03_system/system/boot", "04_kernel/04_1_boot"),
    ("03_system/system/kernal.md", "04_kernel/04_2_structure"),
    ("03_system/system/process", "04_kernel/04_3_process"),

    # Chapter 5
    ("03_system/shell", "05_shell/05_1_intro"),
    ("04_command/command", "05_shell/05_2_terminal"),

    # Chapter 6
    ("04_command/start/user", "06_permission/06_1_user"),
    ("03_system/system/ownership", "06_permission/06_2_ownership"),
    ("03_system/system/permit", "06_permission/06_3_permission"),

    # Chapter 7
    ("03_system/system/package/index.md", "07_package/07_1_manager"),
    ("03_system/system/package", "07_package/07_1_manager"),
    ("03_system/system/package/apt", "07_package/07_2_apt"),
    ("03_system/system/package/dnf", "07_package/07_3_dnf"),
    ("03_system/system/compile", "07_package/07_4_compile"),

    # Chapter 8
    ("04_command/start/edit", "08_editor/08_1_vim"),
    ("04_command/start/pipe", "08_editor/08_2_pipe"),
    ("04_command/start/redirection", "08_editor/08_3_redirect"),

    # Chapter 9
    ("04_command/network", "09_network/09_1_structure"),
    ("03_system/system/ip", "09_network/09_2_ip"),
    ("03_system/system/remote", "09_network/09_3_remote"),

    # Chapter 10
    ("05_basic_server/demon/systemctl.md", "10_daemon/10_2_systemd"),
    ("05_basic_server/demon", "10_daemon/10_1_concept"),
    ("05_basic_server/server", "10_daemon/10_3_service"),

    # Chapter 11
    ("06_web_server/web/apache", "11_webserver/11_2_apache"),
    ("06_web_server/web/nginx", "11_webserver/11_3_nginx"),
    ("06_web_server/web", "11_webserver/11_1_intro"),

    # Chapter 12
    ("07_ext_server/database/mysql", "12_database/12_2_mysql"),
    ("07_ext_server/database", "12_database/12_1_intro"),
    ("07_ext_server/dev", "12_database/12_3_webdb"),

    # Chapter 13
    ("03_system/system/monitor", "13_monitoring/13_1_system"),
    ("03_system/system/schedule", "13_monitoring/13_2_cron"),

    # Chapter 14
    ("03_system/system/backup", "14_troubleshoot/14_1_backup"),
    ("09_troubleshoot/22_recovery", "14_troubleshoot/14_2_recovery"),
    ("09_troubleshoot/23_security", "14_troubleshoot/14_3_security")
]

os.chdir(BASE_DIR)

print("Starting migration...")

for src, dst in MAPPINGS:
    dst_dir = os.path.join(BASE_DIR, dst)
    dst_img_dir = os.path.join(dst_dir, "img")
    
    os.makedirs(dst_img_dir, exist_ok=True)
    
    src_path = os.path.join(BASE_DIR, src)
    
    # Check if source exists
    if not os.path.exists(src_path):
        # Maybe it has .md extension
        if not src_path.endswith('.md') and os.path.exists(src_path + '.md'):
            src_path = src_path + '.md'
        else:
            continue
            
    # If source is a file
    if os.path.isfile(src_path):
        target_file = os.path.join(dst_dir, "index.md")
        if not os.path.exists(target_file):
            shutil.copy2(src_path, target_file)
    
    # If source is a directory
    elif os.path.isdir(src_path):
        # Look for index.md
        index_src = os.path.join(src_path, "index.md")
        if os.path.exists(index_src):
            target_file = os.path.join(dst_dir, "index.md")
            if not os.path.exists(target_file):
                shutil.copy2(index_src, target_file)
        else:
            # Look for any single .md file
            md_files = [f for f in os.listdir(src_path) if f.endswith('.md')]
            if len(md_files) == 1:
                target_file = os.path.join(dst_dir, "index.md")
                if not os.path.exists(target_file):
                    shutil.copy2(os.path.join(src_path, md_files[0]), target_file)
        
        # Copy images
        src_img_dir = os.path.join(src_path, "img")
        if os.path.exists(src_img_dir) and os.path.isdir(src_img_dir):
            for img_file in os.listdir(src_img_dir):
                src_i = os.path.join(src_img_dir, img_file)
                dst_i = os.path.join(dst_img_dir, img_file)
                if os.path.isfile(src_i) and not os.path.exists(dst_i):
                    shutil.copy2(src_i, dst_i)

print("Migration completed.")
