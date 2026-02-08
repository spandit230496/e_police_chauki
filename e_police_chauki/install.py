import os
import subprocess
import frappe


def after_install():
    install_requirements()


def install_requirements():

    app_path = frappe.get_app_path("e_police_chauki")
    requirements_file = os.path.join(app_path, "requirements.txt")

    if os.path.exists(requirements_file):
        frappe.logger().info("Installing requirements...")

        subprocess.check_call([
            "pip",
            "install",
            "-r",
            requirements_file
        ])

        frappe.logger().info("Requirements installed successfully.")
    else:
        frappe.logger().warning("requirements.txt not found!")
