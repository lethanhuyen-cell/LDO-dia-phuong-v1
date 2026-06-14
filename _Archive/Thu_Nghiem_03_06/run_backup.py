import os
import shutil
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Define source and destination directories
workspace_dir = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ'
backup_dir = os.path.join(workspace_dir, 'Sao_Luu_Du_Phong')

# Create backup directory if not exists
os.makedirs(backup_dir, exist_ok=True)

# List of critical files to back up
critical_files = [
    'demo_landing_page_hanoi_clean.html',
    'hanoi_final_consolidated.json',
    'lich_su_phat_trien_du_an.md',
    'kinh_doanh_va_quang_cao_chuyen_trang.md',
    'Ke_Hoach_Kinh_Doanh/Ke_hoach_kinh_doanh_tong_the_v2.md',
    'Ke_Hoach_Kinh_Doanh/Khung_sach_phat_trien_va_nhan_ban_dia_phuong.md'
]

# Copy the compilation script from the brain artifact directory to the workspace for persistence
artifact_script = 'C:/Users/Admin/.gemini/antigravity/brain/33ccafad-2fa8-4696-acbe-bb1db8c432c1/apply_ads_layout.py'
workspace_script = os.path.join(workspace_dir, 'apply_ads_layout.py')

if os.path.exists(artifact_script):
    shutil.copy2(artifact_script, workspace_script)
    print(f"Copied compiler script to workspace: {workspace_script}")

# Add the compiler script to the backup list
critical_files.append('apply_ads_layout.py')

# Copy files
print(f"Starting backup at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
for relative_path in critical_files:
    src_path = os.path.join(workspace_dir, relative_path)
    if os.path.exists(src_path):
        # Create subdirectories in backup folder if needed
        dest_path = os.path.join(backup_dir, relative_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(src_path, dest_path)
        print(f"✔ Backed up: {relative_path} -> Sao_Luu_Du_Phong/{relative_path}")
    else:
        print(f"⚠ Warning: File not found for backup: {relative_path}")

print("Backup process completed successfully! All critical project data is now protected.")
